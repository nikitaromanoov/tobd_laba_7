import csv
import redis
import json
import pandas as pd

r = redis.StrictRedis(host="redis", port = 6379)

df = pd.read_csv("./data/en.openfoodfacts.org.products.csv", sep="\t")
df.to_json("./data/data.json")
with open("./data/data.json") as f:
    r.set("Table_for_segmentation", json.dumps(json.load(f)))

