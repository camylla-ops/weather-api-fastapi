from fastapi import FastAPI, Query, status
import logging
from typing import Annotated

from config import get_settings
from models import WeatherResponse
from weather import WeatherService

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Carrega configurações
settings = get_settings()

# Inicializa serviços
weather_service = WeatherService(settings)

# Inicializa a aplicação FastAPI
app = FastAPI(
    title="API de Previsão do Tempo",
    description="API para consulta de dados meteorológicos usando OpenWeatherMap",
    version="1.0.0"
)

@app.get(
    "/weather",
    response_model=WeatherResponse,
    status_code=status.HTTP_200_OK,
    responses={
        404: {"description": "Cidade não encontrada"},
        500: {"description": "Erro interno do servidor"}
    }
)
async def get_weather(
    city: Annotated[
        str,
        Query(
            description="Nome da cidade para consulta",
            min_length=2,
            max_length=100,
            example="São Paulo"
        )
    ]
):
    """
    Retorna dados meteorológicos para uma cidade específica.
    
    - **city**: Nome da cidade (ex: São Paulo, Rio de Janeiro)
    
    Os dados são cacheados por 5 minutos para reduzir chamadas à API externa.
    """
    logger.info(f"Consultando previsão do tempo para: {city}")
    return await weather_service.get_weather(city)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 