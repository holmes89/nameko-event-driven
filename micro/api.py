import json

from nameko.web.handlers import http
from nameko.events import EventDispatcher


class API:
    name = 'api'

    dispatch = EventDispatcher()

    @http('GET', '/hello')
    def get_method(self):
        return json.dumps({'hello': 'world'})

    @http('POST', '/hello')
    def do_post(self, request):
        name = request.get_data(as_text=True)
        self.dispatch("say_hello", name)
        return json.dumps({'hello': name})
