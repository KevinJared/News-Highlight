import os

class Config:
    NEWS_SOURCE_BASE_URL = 'https://newsapi.org/v1/sources?category={}&language=en'
    NEWS_ARTICLE_API_BASE_URL = 'https://newsapi.org/v1/articles?source={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}