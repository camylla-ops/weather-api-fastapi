from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

class WeatherResponse(BaseModel):
    """Modelo de resposta para dados meteorológicos"""
    cidade: str = Field(
        ...,
        example="São Paulo",
        description="Nome da cidade consultada"
    )
    temperatura: float = Field(
        ...,
        example=25.6,
        description="Temperatura atual em graus Celsius",
        ge=-50,
        le=50
    )
    temperatura_min: float = Field(
        ...,
        example=23.2,
        description="Temperatura mínima em graus Celsius",
        ge=-50,
        le=50
    )
    temperatura_max: float = Field(
        ...,
        example=27.8,
        description="Temperatura máxima em graus Celsius",
        ge=-50,
        le=50
    )
    umidade: int = Field(
        ...,
        example=65,
        description="Umidade relativa do ar em porcentagem",
        ge=0,
        le=100
    )
    descricao: str = Field(
        ...,
        example="céu limpo",
        description="Descrição do clima em português"
    )
    atualizado_em: str = Field(
        ...,
        example="2024-02-20 14:30:45",
        description="Data e hora da última atualização"
    )

    @validator('temperatura_max')
    def max_temp_must_be_greater(cls, v, values):
        if 'temperatura_min' in values and v < values['temperatura_min']:
            raise ValueError('temperatura_max deve ser maior que temperatura_min')
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "cidade": "São Paulo",
                "temperatura": 25.6,
                "temperatura_min": 23.2,
                "temperatura_max": 27.8,
                "umidade": 65,
                "descricao": "céu limpo",
                "atualizado_em": "2024-02-20 14:30:45"
            }
        } 