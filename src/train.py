from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.feature import VectorAssembler, MinMaxScaler
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import psutil
import os
import time
import configparser

import redis
import pandas as pd

import json

from websocket import create_connection 


def ws_vitrina(task, name, value=None):
        uri = "ws://{}:{}".format("py_vitrina", 8103) 
        ws = create_connection(uri)
        if task== "get":
            data = {'task': task, 'name': name}
        else:
            data = {'task': task, 'name': name, "value" : value}
        ws.send(json.dumps(data))
        responce = json.loads(ws.recv())
        ws.close()
        print(responce.keys())
        return responce
            

    

config = configparser.ConfigParser()
config.read("config.ini")

class model_KMean():
    def __init__(self, config):
        self.spark = SparkSession.builder.appName("test") \
        .config("spark.executor.instances", "2") \
        .config("spark.executor.memory", "2g") \
        .config("spark.executor.cores", "4") \
        .config("spark.driver.memory", "4g") \
        .config("spark.driver.cores", "4") \
        .getOrCreate()
        self.model = KMeans().setK(int(config["parameters"]["k_p"])).setSeed(int(config["parameters"]["seed"]))
        

    def train(self):
        file = ws_vitrina("get","Table_for_segmentation")["result"]
        pd.read_json(file).to_csv("data.csv", sep="\t", index= False)
        dat = self.spark.read.format("csv").option("header", True).option("sep", "\t").load("data.csv")
        dat = dat.select([col(i).cast("float") for i in dat.columns])
        dat = VectorAssembler(inputCols=dat.columns, outputCol="prefeatures").setHandleInvalid("error").transform(dat)
        sc = MinMaxScaler().setInputCol("prefeatures").setOutputCol("features")
        dat = sc.fit(dat).transform(dat)
        metric = ClusteringEvaluator()
        self.model = self.model.fit(dat)
        pred = self.model.transform(dat)
        
        return metric.evaluate(pred)
        

def main():
    global config
    time.sleep(240)
    files = os.listdir("/app/showcase/datacsv_6")
    model = model_KMean(config)
    print("_____")
    print("_____")
    rez = model.train()
    print("Result:", rez)
    print("This result sent on redis server: ", rez, ws_vitrina("send", "rez", rez))
    print("_____")

if __name__ == "__main__":
	main()
