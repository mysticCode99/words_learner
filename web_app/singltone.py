
from typing import Self

class Config_Provider():
    DATABASE_PATH = '/tmp/flsite.db'
    DEBUG = True
    SECRET_KEY = 'sdfvresdbvrscrw85w7rsfv68w4rv'
    __INSTANCE = None

    def __new__(cls) -> Self:
        if not cls.__INSTANCE:
            cls.__INSTANCE = super(cls, Config_Provider).__new__(cls)
        return cls.__INSTANCE

    @classmethod
    def get_instance(cls):
        if not cls.__INSTANCE:
            cls.__INSTANCE = super(cls, Config_Provider).__new__(cls)
        return cls.__INSTANCE

    @classmethod
    def get_top_bar_buttons(cls) -> list:
        """ Returns top bar buttons list """
        return [
            { 
                "name" : "Home",
                "href" : "index"
            }
        ]

    @classmethod
    def get_top_bar_buttons_html(cls) -> str:
        """ Returns top bar buttons list """
        for btn in cls.get_top_bar_buttons():
            pass
        