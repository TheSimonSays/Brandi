import typing as t
from brandi.app import App


class Brandi(App):
    default_config = {
        'APP_ENV': 'development',
        'APP_DEBUG': False,
        'STATIC_FOLDER': '/static',
        'TEMPLATE_FOLDER': '/templates'
    }

    def __init__(
        self,
        app_name: str,
        static_folder: t.Optional[str] = None,
        templates_folder: t.Optional[str] = None
    ) -> None:
        self.configure_app(self.default_config)
        self.init_context(self)
        self.app_name = app_name
        self.static_folder = static_folder or self.config['STATIC_FOLDER']
        self.templates_folder = templates_folder or self.config['TEMPLATE_FOLDER']

    def __call__(self, environe: t.Dict[str, t.Any], start_response: t.Any) -> t.Any:
        """
        Brandi entry point
        :param environ: dict of wsgi environ
        :param start_response: point of entry mod_wsgi 
        """
        self.init_request_handler(environe, start_response)
        return self.request_handler.request_dispatch()
