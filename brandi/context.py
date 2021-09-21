class Context:
    """
    A temporary class
    I should think of something better
    """
    current_app: object

    @classmethod
    def init_curent_app_context(cls, obj: object):
        cls.current_app = obj
