class Context:
    current_app: object

    @classmethod
    def init_curent_app_context(cls, obj: object):
        cls.current_app = obj
