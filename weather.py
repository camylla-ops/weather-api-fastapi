from datetime import datetime
import httpx
from fastapi import HTTPException, status
from cachetools import TTLCache

from models import WeatherResponse
from config import Settings

class WeatherService:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.cache = TTLCache(maxsize=100, ttl=settings.cache_ttl)

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """Converte temperatura de Kelvin para Celsius"""
        return round(kelvin - 273.15, 1)

    async def get_weather(self, city: str) -> WeatherResponse:
        """
        Obtém dados meteorológicos para uma cidade.
        
        Args:
            city: Nome da cidade para consulta
            
        Returns:
            WeatherResponse: Dados meteorológicos formatados
        """
        # Normaliza o nome da cidade
        city = city.strip()

        # Verifica se os dados estão em cache
        if city in self.cache:
            return self.cache[city]

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                # Parâmetros para a requisição à API OpenWeatherMap
                params = {
                    'q': city,
                    'appid': self.settings.openweathermap_api_key,
                    'lang': 'pt_br',
                    'units': 'metric'  # Já retorna em Celsius
                }

                # Faz a requisição à API
                response = await client.get(
                    str(self.settings.openweather_base_url),
                    params=params
                )
                response.raise_for_status()
                
                weather_data = response.json()
                
                # Formata os dados para nossa resposta
                formatted_data = WeatherResponse(
                    cidade=city,
                    temperatura=float(weather_data['main']['temp']),
                    temperatura_min=float(weather_data['main']['temp_min']),
                    temperatura_max=float(weather_data['main']['temp_max']),
                    umidade=weather_data['main']['humidity'],
                    descricao=weather_data['weather'][0]['description'],
                    atualizado_em=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                )

                # Salva no cache
                self.cache[city] = formatted_data
                
                return formatted_data

        except httpx.TimeoutException:
            raise HTTPException(
                status_code=status.HTTP_504_GATEWAY_TIMEOUT,
                detail="Tempo limite excedido ao consultar serviço externo"
            )
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Cidade não encontrada"
                )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao consultar API externa: {str(e)}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro inesperado: {str(e)}"
            ) 