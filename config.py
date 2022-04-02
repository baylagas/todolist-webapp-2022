class BaseConfig(object):
    # sqlite:////tmp/test.db
    # postgresql://scott:tiger@localhost:5432/mydatabase
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/testdb"
    """ SQLALCHEMY_DATABASE_URI = "sqlite:///todolist_database.db" """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 300
    """
    SECRET_KEY = "horrible_secret_key"
    LOGIN_DISABLED = True
