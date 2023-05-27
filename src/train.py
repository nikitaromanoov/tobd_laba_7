from preprocessing import Preprocess
from pyspark.ml.clustering import KMeans

import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def get_params():
	with open()


def train():
	trainer = KMeans().setK(config["parameters"]["k"]).setSeed(config["parameters"]["seed"])

def main():
	

if __name__ == "__main__":
	main()
