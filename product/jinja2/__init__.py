import itertools
import json
from urllib.parse import quote

from jinja2.ext import Extension
from martor.templatetags.martortags import safe_markdown
from statici18n.templatetags.statici18n import inlinei18n

from . import registry

registry.function('str', str)
registry.filter('markdown', safe_markdown)
registry.filter('str', str)
registry.filter('json', json.dumps)
registry.filter('urlquote', quote)
registry.filter('roundfloat', round)
registry.function('inlinei18n', inlinei18n)


@registry.function
def counter(start=1):
    return itertools.count(start).__next__


class JINJA2Extension(Extension):
    def __init__(self, env):
        super(JINJA2Extension, self).__init__(env)
        env.globals.update(registry.globals)
        env.filters.update(registry.filters)
        env.tests.update(registry.tests)
