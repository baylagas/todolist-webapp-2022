class BaseConfig(object):
    # sqlite:////tmp/test.db
    # postgresql://scott:tiger@localhost:5432/mydatabase
    """SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/testdb" """
    SQLALCHEMY_DATABASE_URI = "mysql://b96354f915678f:6ebe6dfb@us-cdbr-east-05.cleardb.net:3306/heroku_e3185dc57eef12c"
    """ SQLALCHEMY_DATABASE_URI = "sqlite:///todolist_database.db" """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """ SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 300 """
    SQLALCHEMY_POOL_RECYCLE = 35  # value less than backend’s timeout
    SQLALCHEMY_POOL_TIMEOUT = 7  # value less than backend’s timeout
    SQLALCHEMY_PRE_PING = True
    SECRET_KEY = "horrible_secret_key"
    LOGIN_DISABLED = True


class ProductionConfig(object):
    # sqlite:////tmp/test.db
    # postgresql://scott:tiger@localhost:5432/mydatabase
    """SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/testdb" """
    SQLALCHEMY_DATABASE_URI = "mysql://b96354f915678f:6ebe6dfb@us-cdbr-east-05.cleardb.net:3306/heroku_e3185dc57eef12c"
    """ SQLALCHEMY_DATABASE_URI = "sqlite:///todolist_database.db" """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 300
    SECRET_KEY = "horrible_secret_key"
    LOGIN_DISABLED = True
