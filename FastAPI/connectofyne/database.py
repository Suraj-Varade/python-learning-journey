import databases
import sqlalchemy
from config import config

metadata = sqlalchemy.MetaData()  ## holds all tables, columns - schemas


user_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("confirmed", sqlalchemy.Boolean, default=False),
)


post_table = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("post_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("content", sqlalchemy.String),
    sqlalchemy.Column(
        "user_id", sqlalchemy.ForeignKey("users.user_id"), nullable=False
    ),
)

like_table = sqlalchemy.Table(
    "likes",
    metadata,
    sqlalchemy.Column("like_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "post_id", sqlalchemy.ForeignKey("posts.post_id"), nullable=False
    ),
    sqlalchemy.Column(
        "user_id", sqlalchemy.ForeignKey("users.user_id"), nullable=False
    ),
)

comment_table = sqlalchemy.Table(
    "comments",
    metadata,
    sqlalchemy.Column("comment_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "post_id", sqlalchemy.ForeignKey("posts.post_id"), nullable=False
    ),
    sqlalchemy.Column("comment", sqlalchemy.String),
    sqlalchemy.Column(
        "user_id", sqlalchemy.ForeignKey("users.user_id"), nullable=False
    ),
)

engine = sqlalchemy.create_engine(
    config.DATABASE_URL, connect_args={"check_same_thread": False}
)
## helps identifying the type of database, sqlite, postgres

metadata.create_all(engine)
## creates the engine with all tables and columns. (based on metadata)

database = databases.Database(
    config.DATABASE_URL, force_rollback=config.DB_FORCE_ROLL_BACK
)

## databases module returns the database object that we can use.
