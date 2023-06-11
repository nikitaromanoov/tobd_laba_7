import json
import asyncio
import websockets
import json
import argparse
from os import path
import os

import redis

import pandas as pd

parser = argparse.ArgumentParser(description='')
parser.add_argument("--address", type=str, default="0.0.0.0",  help= "ws server address" )
parser.add_argument("--port", type=int, default=8103,  help= "ws server port" )


def redis_f(name, value, p_get=True, p_set=True):
        r = redis.Redis(host="redis",
                        port=6379,
                        decode_responses=True)
        if p_set:
            r.set(name, value)
        if p_get:
            return r.get(name)
            
            
r = redis.Redis(host="redis",
                port=6379,
                decode_responses=True)
file = redis_f("Table_for_segmentation", None, p_set=False)                
pd.read_json(file).to_csv("/app/showcase/data.csv", sep="\t", index= False)

def main():
    args = parser.parse_args()
    async def ws(websocket, path):
        async for data in websocket:

            data = json.loads(data)
            try:
                task = data['task']
                name = data["name"]
                r = redis.Redis(host="redis",
                            port=6379,
                            decode_responses=True)
                if task == "send":
                    r.set(name, data["value"])
                    result = "Data has sended"
                elif task == "get":
                    for i in os.listdir("/app/showcase/data_preprocessed.csv"):
                        if i[-4:] == ".csv":
                            best = "/app/showcase/data_preprocessed.csv/" + i
                    df = pd.read_csv(best, sep="\t")
                    df.to_json("./data/data.json")
                    with open("./data/data.json") as f:
                        result = json.dumps(json.load(f))


                service_output = {'result': result, 'event': 'success'}
                await websocket.send(json.dumps(service_output))

            except Exception as e:
                print("Error: {}".format(e))
                service_error = {'event': 'error', 'msg': "Error! {}".format(e)}
                await websocket.send(json.dumps(service_error))

    print('WS Server started.\n')

    print(f"WS server started at uri={args.address}:{args.port}")
    asyncio.get_event_loop().run_until_complete(websockets.serve(ws, args.address, args.port, max_size=1024*1024*10))

    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    import sys
    sys.path.append(path.join(path.dirname(__file__), '../..'))
    main()
