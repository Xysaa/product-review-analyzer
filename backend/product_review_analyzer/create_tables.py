from pyramid.paster import get_appsettings, setup_logging
from sqlalchemy import engine_from_config
from product_review_analyzer.models import Base

if __name__ == "__main__":
    setup_logging("development.ini")
    settings = get_appsettings("development.ini")
    engine = engine_from_config(settings, prefix="sqlalchemy.")
    Base.metadata.create_all(engine)
    print("Tables created.")
