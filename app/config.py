from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    database_url: str = "sqlite:///./linkedin.db"
    linkedin_access_token: str = ""
    linkedin_person_urn: str = ""
    daily_post_hour: int = 9
    daily_post_minute: int = 0
    timezone: str = "Asia/Kolkata"
    auto_publish: bool = False

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
