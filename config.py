class BaseConfig(object):
    # sqlite:////tmp/test.db
    # postgresql://scott:tiger@localhost:5432/mydatabase
    """SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/testdb" """
    """ SQLALCHEMY_DATABASE_URI = "sqlite:///todolist_database.db" """
    """ SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://root:root@localhost:5432/testdb" """
    SQLALCHEMY_DATABASE_URI = "postgres://wvlaqmvatbbwbu:be6fd7cc0d7f144c0e7bfbc2b9f8d36e2f8ba4dbd52091b685f4f5b0c1dada9f@ec2-3-217-251-77.compute-1.amazonaws.com:5432/d2vpptod6krkuv"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 300
    """
    SECRET_KEY = "horrible_secret_key"
    LOGIN_DISABLED = True
