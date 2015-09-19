from sqlalchemy_fp import setup_reflective_engine
from os import environ
from time import sleep

sleep(5)

connstring = "postgresql://{0}:{1}@db".format(
    environ["DB_USER"],
    environ["DB_PASSWORD"]
)

classname_tablename_dict = {
    "User": "users"
}

models, with_session = setup_reflective_engine(
    classname_tablename_dict,
    connstring
)

assert hasattr(models, "User")
