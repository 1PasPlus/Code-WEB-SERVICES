from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, DateTime

# Database connection string
db_string = "postgresql://root:root@localhost:5432/postgres"

# Create engine
engine = create_engine(db_string)

# Create metadata
metadata = MetaData()

# Define User table
user_table = Table(
    'User', metadata,
    Column('id', Integer, primary_key=True),
    Column('firstname', String(100), unique=True, nullable=False),
    Column('lastname', String(100), unique=True, nullable=False),
    Column('age', Integer, nullable=False),
    Column('email', String(100), unique=True, nullable=False),
    Column('job', String(100), nullable=False)
)

# Define Application table
application_table = Table(
    'Application', metadata,
    Column('id', Integer, primary_key=True),
    Column('appname', String(100), unique=True, nullable=False),
    Column('username', String(100), unique=True, nullable=False),
    Column('lastconnection', DateTime, nullable=False),
    Column('user_id', Integer, ForeignKey('User.id'), nullable=False)
)

# Create tables
metadata.create_all(engine)
