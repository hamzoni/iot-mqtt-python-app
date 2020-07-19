class BaseContainer:
    __instance__ = None

    @classmethod
    def container(cls):
        if cls.__instance__ is None:
            cls.__instance__ = cls()
        return cls.__instance__
