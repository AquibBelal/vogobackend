import configparser
import pymongo

config = configparser.ConfigParser()
config.read('configmsg.ini')
dsh = config['DASH']
MONGO_HOST = dsh['mongodb://localhost']
MONGO_PORT = int(dsh['27017'])
myclient = pymongo.MongoClient(MONGO_HOST,MONGO_PORT)
mydb = myclient[(dsh['vogohelmetsdata'])]

def db_details():
    return(mydb)