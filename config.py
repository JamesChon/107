import pymongo
import certifi

con_str = "mongodb+srv://Chon:zaq1xsw2CDE#@sdgku.at4mlkc.mongodb.net/?retryWrites=true&w=majority&appName=SDGKU"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("107test")