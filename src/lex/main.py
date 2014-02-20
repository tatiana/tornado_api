"""
Lex starter and main loop.
"""
from tornado.web import Application, StaticFileHandler, URLSpec
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.log import app_log
from tornado.options import define, options, parse_command_line

from lex import settings
from lex.handlers import HealthcheckHandler, NewsHandler, RootHandler, VersionHandler


ROUTES = [
    URLSpec(r'/?', RootHandler),
    URLSpec(r'/healthcheck/?', HealthcheckHandler),
    URLSpec(r'/version/?', VersionHandler),
    URLSpec(r'/recommendation/?', NewsHandler),
    URLSpec(r'/docs/?(.*)', StaticFileHandler, {'path': settings.HTML_PATH, 'default_filename': 'index.html'}),
    URLSpec(r'/_static/?(.*)', StaticFileHandler, {'path': settings.STATIC_PATH})
]


# Options
define("debug", default=settings.DEBUG, help="Enable or disable debug", type=bool)
define("port", default=settings.PORT, help="Run app on the given port", type=int)

# Temporary routes for serving HTML while Tsuru doesn't support a better way
# to serve static files. Eg. Nginx or other.
define("template_path", default=settings.HTML_PATH, help="Path where HTML doc files are", type=str)
define("static_path", default=settings.STATIC_PATH, help="Path where doc static files are ", type=str)


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
