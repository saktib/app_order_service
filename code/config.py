import os

class Config:
    dbuser = os.environ.get('MYSQL_USER')
    dbpassword = os.environ.get('MYSQL_PASSWORD')
    dbname = os.environ.get('MYSQL_DATABASE')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{dbuser}:{dbpassword}@database:3306/{dbname}?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

