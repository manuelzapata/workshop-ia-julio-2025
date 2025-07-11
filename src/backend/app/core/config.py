from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    environment: str = 'development'
    api_prefix: str = '/api/v1'

    model_config = ConfigDict(env_file='.env')

settings = Settings() 