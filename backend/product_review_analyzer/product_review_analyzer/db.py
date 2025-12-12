from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from pyramid.events import NewRequest

from .models import Base

def includeme(config):
    settings = config.get_settings()
    engine = engine_from_config(settings, prefix="sqlalchemy.")

    # create session factory
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

    # attach to registry
    config.registry.db_session_factory = SessionLocal
    Base.metadata.bind = engine

    # add request.dbsession
    def add_dbsession(event):
        request = event.request
        request.dbsession = SessionLocal()

        def cleanup(request):
            try:
                request.dbsession.close()
            except Exception:
                pass

        request.add_finished_callback(cleanup)

    config.add_subscriber(add_dbsession, NewRequest)
