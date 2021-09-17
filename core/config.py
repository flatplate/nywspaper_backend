import os

config = {
    "DATABASE_URL": "postgresql://postgres:123123123u@localhost:5432/postgres"
}

config_init = False

def init_config():
    global config_init
    config_init = True
    for key in config:
        if os.getenv(key):
            config[key] = os.getenv(key)

def get_config():
    if not config_init:
        init_config()
    return config