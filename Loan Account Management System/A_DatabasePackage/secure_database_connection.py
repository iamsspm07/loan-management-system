from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus


# CONFIGURATION PARAMETERS
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "loan_management"
DB_USER = "postgres"
DB_PASSWORD = quote_plus("Ozaki8")
DB_ECHO = False

# DATABASE CONNECTION URL PARAMETERS: POSTGRESQL
DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ENGINE GATEWAY/BRIDGE:
ENGINE = create_engine(
    DATABASE_URL,
    echo=DB_ECHO,
    pool_pre_ping=True
)

# DATABASE CONNECTION SESSION
sessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=ENGINE
)

# ESTABLISHED CONNECTION
def loan_jwt_database_connection():
    database = sessionLocal()
    try:
        yield database
    finally:
        database.close()

# CONNECTING PYTHON CLASS WITH DATABASE TABLE

BASE = declarative_base()
