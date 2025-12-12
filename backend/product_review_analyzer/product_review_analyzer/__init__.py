from pyramid.config import Configurator
from .db import includeme as db_includeme
from .routes import includeme as routes_includeme

def main(global_config, **settings):
    config = Configurator(settings=settings)

    config.add_renderer("json", "pyramid.renderers.json_renderer_factory")
    config.add_tween("product_review_analyzer.settings.cors_tween_factory")

    db_includeme(config)
    routes_includeme(config)

    config.scan()
    return config.make_wsgi_app()
