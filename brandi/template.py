import typing as t
from mako.lookup import TemplateLookup
from mako.template import Template
from brandi.context import Context


def render_template(template: str, **context) -> t.Any:
    templates_folder = Context.current_app.templates_folder
    lookup = TemplateLookup(directories=[templates_folder])
    template = lookup.get_template(template)
    return template.render(**context)


def render_template_string(html_string: str, **context) -> t.Any:
    template = Template(html_string)
    return template.render(**context)
