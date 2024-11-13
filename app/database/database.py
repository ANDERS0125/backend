# database.py
from sqlmodel import create_engine, SQLModel, Session

# Database connection URL
postgres_file_name = "fastapi"
postgres_url = f"postgresql://postgres:12345678@localhost:5432/{postgres_file_name}"

# Create database engine
engine = create_engine(postgres_url, echo=True)

# Initialize database tables
def init_db():
    SQLModel.metadata.create_all(engine)

# Dependency to provide a database session
def get_session():
    with Session(engine) as session:
        yield session