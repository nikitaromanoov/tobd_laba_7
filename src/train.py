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

def redis_f(name, value, p_get=True, p_set=True):
        r = redis.Redis(host="redis",
                        port=6379,
                        decode_responses=True)
        if p_set:
            r.set(name, value)
        if p_get:
            return r.get(name)


    

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
    def preprocess(self):
        file = redis_f("Table_for_segmentation", None, p_set=False)
        #pd.read_json(file.decode("utf-8")).to_csv("data.csv", sep="\t", index= False)
        pd.read_json(file).to_csv("data.csv", sep="\t", index= False)
        data = self.spark.read.format("csv").option("header", True).option("sep", "\t").load("data.csv")
        persent_of_data = (psutil.virtual_memory().total / (1024.0 **3) - 6)* 300000 / data.count()
        print(persent_of_data)
        data = data.select([col(x).cast("float") for x in [ i for i in data.columns if "100g" in i]])
        data = data.na.fill(0.0).na.fill("unk")
        data = VectorAssembler(inputCols=data.columns, outputCol="prefeatures").setHandleInvalid("error").transform(data)
        sc = MinMaxScaler().setInputCol("prefeatures").setOutputCol("features")
        self.data = sc.fit(data).transform(data)
        
        return persent_of_data

    def train(self):
        metric = ClusteringEvaluator()
        self.model = self.model.fit(self.data)
        pred = self.model.transform(self.data)
        
        return metric.evaluate(pred)
        

def main():
    global config
    model = model_KMean(config)
    print("_____")
    print("Size of dataset after preprocessing based on capacity of your device", model.preprocess())
    print("_____")
    rez = model.train()
    print("Result:", rez)
    print("This result sent on redis server: ", redis_f("rez", rez))
    print("_____")

if __name__ == "__main__":
	main()
