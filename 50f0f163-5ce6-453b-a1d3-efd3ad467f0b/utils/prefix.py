from pymongo import MongoClient
import os
import motor.motor_asyncio

cluster_url = os.environ.get("mongocluster")
cluster = MongoClient(cluster_url)
db = cluster['discord']
prefix_col = db['prefix']

def sdprefix(client,message):
  all_prefix =  prefix_col.find({"server":str(message.guild.id)})
  for i in all_prefix:
    return i["prefix"]

