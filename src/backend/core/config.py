from pydantic import BaseSettings

class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    environment: str = 'development'
    api_prefix: str = '/api/v1'

    class Config:
        env_file = '.env'

settings = Settings() 