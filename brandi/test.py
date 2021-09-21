import typing as t
from gunicorn.app.wsgiapp import WSGIApplication
from brandi.brandi import Brandi


class TestBrandiApp(WSGIApplication):
    def __init__(self, app: Brandi, options: t.Optional[t.Dict[str, t.Any]] = None) -> None:
        self.app = app
        self.options = options or {}
        super().__init__()

    def load_config(self):
        config = {
            key: value for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.app

    def run(self):
        return super().run()