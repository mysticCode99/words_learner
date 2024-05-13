

class Engine_Singltone():
    """sumary_line"""
    INSTANCE = None
    LANGUAGE = None
    LANGUAGES = {}

    @classmethod
    def get_instance(cls):
        """sumary_line"""
        if not cls.INSTANCE:
            cls.INSTANCE = super(cls, Engine_Singltone).__new__(cls)
        return cls.INSTANCE
    
    @classmethod
    def get_current_lang(cls) -> str:
        """sumary_line"""
        return cls.LANGUAGE
    
    @classmethod
    def set_lang(cls, lang:str) -> None:
        """sumary_line"""
        cls.LANGUAGE = lang
        if lang not in cls.LANGUAGES.keys():
            cls.LANGUAGES[lang] = []
    
    @classmethod
    def add_word(cls, word):
        """sumary_line"""
        cls.LANGUAGES[cls.LANGUAGE].append(word)

    @classmethod
    def get_last_ten_words(cls):
        """sumary_line"""
        return sorted(cls.LANGUAGES[cls.LANGUAGE], key=lambda w: w.last_time, reverse=True)[:10]
    
    @classmethod
    def get_words(cls):
        """sumary_line"""
        return cls.LANGUAGES[cls.LANGUAGE]