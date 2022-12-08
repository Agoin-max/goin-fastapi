import databases, sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+pymysql://root:12345678@127.0.0.1/fastapi"

db = databases.Database(DATABASE_URL)
Base = declarative_base()


# class User(Base):
#     __tablename__ = "user"
#     id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, comment="ID")
#     name = sqlalchemy.Column(sqlalchemy.String(32))
#     password = sqlalchemy.Column(sqlalchemy.String(64))


engine = create_engine(
    DATABASE_URL, encoding='utf8', echo=True
)

# metadata.create_all(engine)
# Base.metadata.create_all(engine)

