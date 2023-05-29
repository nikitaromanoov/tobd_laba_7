from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.feature import VectorAssembler, MinMaxScaler
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import psutil




import configparser

config = configparser.ConfigParser()
config.read("config.ini")




class model_KMean():
    def __init__(self, config):
        self.spark = SparkSession.builder.appName("test").getOrCreate()
        self.model = KMeans().setK(int(config["parameters"]["k_p"])).setSeed(int(config["parameters"]["seed"]))
    def preprocess(self, path):
        data = self.spark.read.format("csv").option("header", True).option("sep", "\t").load(path)
        persent_of_data = psutil.virtual_memory().total / (1024.0 **3) * 300000 / data.count()
        data = data.sample(persent_of_data,1)
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
        
    def save(self, path):
        self.model.save(path)

	

def main():
    global config
    model = model_KMean(config)
    print("_____")
    print("Size of dataset after preprocessing based on capacity of your device", model.preprocess("./data/en.openfoodfacts.org.products.csv"))
    print("_____")
    print("Result:", model.train())
    print("_____")
    model.save("model.pth")

if __name__ == "__main__":
	main()
