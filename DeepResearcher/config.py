# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     GROQ_API_KEY:str
#     MONGO_URI:str
#     DB_NAME:str
#     UserMemory:str


#     class Config:
#         env_file = ".env"

# settings = Settings()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str
    MONGO_URI: str
    DB_NAME: str
    UserMemory: str

    class Config:
        env_file = ".env"

settings = Settings()

# Debug print
print("Loaded settings:")
print("MONGO_URI:", settings.MONGO_URI)
print("DB_NAME:", settings.DB_NAME)
print("UserMemory:", settings.UserMemory)