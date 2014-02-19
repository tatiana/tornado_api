"""
Lex starter and main loop.
"""
from tornado.web import Application, URLSpec
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.log import app_log
from tornado.options import define, options, parse_command_line

from lex import settings
from lex.handlers import HealthcheckHandler, NewsHandler


ROUTES = [
    URLSpec(r'/healthcheck/?', HealthcheckHandler),
    URLSpec(r'/recommendation/?', NewsHandler),
]


# Options
define("debug", default=settings.DEBUG, help="Enable or disable debug", type=bool)
define("port", default=settings.PORT, help="Run app on the given port", type=int)


def create_app():
    """
    Create Lex instance of tornado.web.Application.
    """
    return Application(ROUTES, **options.as_dict())


def main():  # pragma: no cover
    """
    Run lex main loop.
    """
    parse_command_line()
    app_log.info("Lex is running!")
    application = create_app()
    server = HTTPServer(application)
    server.listen(options['port'])
    io_loop = IOLoop.instance()
    io_loop.start()


if __name__ == '__main__':
    main()
else:
    application = create_app()
