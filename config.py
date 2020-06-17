import os
 
app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_USER= 'hello@postgreserver-nd'
    POSTGRES_PW = os.getenv('POSTGRE_SERVER_PW') 
    POSTGRES_DB= 'techconfdb'
    POSTGRES_SERVER= 'postgreserver-nd.postgres.database.azure.com'
    DB_URL = 'postgresql://{user}:{pw}@{host}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,host=POSTGRES_SERVER,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm' 
    #SERVICE_BUS_CONNECTION_STRING = os.getenv('SERVICE_BUS_STRING') 
    #SERVICE_BUS_QUEUE_NAME ='myndqueue'
    #ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    #SENDGRID_API_KEY = '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"'

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False