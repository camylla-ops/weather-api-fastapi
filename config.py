from pydantic_settings import BaseSettings
from pydantic import Field, HttpUrl, validator
from functools import lru_cache
import os

class Settings(BaseSettings):
    """Configurações da aplicação"""
    # OpenWeatherMap
    openweathermap_api_key: str = Field(
        ...,
        env='OPENWEATHERMAP_API_KEY',
        description='Chave de API do OpenWeatherMap'
    )
    openweather_base_url: HttpUrl = Field(
        "http://api.openweathermap.org/data/2.5/weather",
        description='URL base da API do OpenWeatherMap'
    )
    
    # Cache
    cache_ttl: int = Field(
        default=300,
        env='CACHE_TTL',
        description='Tempo de vida do cache em segundos'
    )

    # API
    api_title: str = "API de Previsão do Tempo"
    api_description: str = "API para consulta de dados meteorológicos usando OpenWeatherMap"
    api_version: str = "1.0.0"

    @validator('openweathermap_api_key')
    def validate_api_key(cls, v):
        # Remove espaços em branco e verifica se a chave tem um formato válido
        v = v.strip()
        if not v or len(v) < 20:  # Chaves OpenWeatherMap geralmente têm 32 caracteres
            raise ValueError('Chave API inválida ou não configurada')
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    """Retorna as configurações da aplicação (cached)"""
    return Settings() 