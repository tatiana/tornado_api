"""
Lex starter and main loop.
"""

from argparse import ArgumentParser

from tornado import web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

from lex import settings
from lex.handlers import HealthcheckHandler


ROUTES = [
    web.URLSpec(r'/healthcheck/?', HealthcheckHandler),
]


class Application(web.Application):
    """
    Lex application
    """
    def __init__(self, debug=False):
        # self.initialize_connections()
        super(Application, self).__init__(ROUTES, debug=debug)

    # def initialize_connections(self):
    #     pass


def main(args):  # pragma: no cover
    """
    Run lex main loop.
    """
    application = Application(debug=args.debug)
    server = HTTPServer(application)
    server.listen(settings.SERVER_PORT)
    io_loop = IOLoop.instance()
    io_loop.start()


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('-d', '--debug', action='store_const', const=True, default=settings.DEBUG, help='debug mode')
    args = parser.parse_args()
    main(args)
else:
    application = Application()
