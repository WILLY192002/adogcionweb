class Config:
    SECRET_KEY = "BItWeNAt1T^SkvhUI*S^"

class developmentConfig(Config):
  DEBUG = True

config = {'development': developmentConfig}

