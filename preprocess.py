from dotenv import load_dotenv
from cleanup import clean_data
from create_all_csvs import create_csvs
import os
import time
from merge_csvs import merge_csvs
import asyncio
from ossapi import *

load_dotenv()

apikey = str(os.getenv('api_key'))
client_id = str(os.getenv('client_id'))
client_secret = str(os.getenv('client_secret'))

def preprocess(folder: str, csv_name):
    prep_start_time = time.time()

    client = OssapiAsync(client_id=client_id, client_secret=client_secret)

    print(f"\n\n\n\tStarted preprocessing!\n\t- Clearing unneeded Files\n\t- Creating .csvs\n\t# Made by Robin Korn and David Deml")
    asyncio.run(clean_data(client, folder))
    failed_maps = asyncio.run(create_csvs(client, folder))
    merge_csvs(folder, csv_name, failed_maps)

    prep_end_time = time.time()
    prep_elapsed_time = prep_end_time - prep_start_time

    print(
        f"\n\n\n\tFinished preprocessing!\n\tElapsed Time Preprocessing: {prep_elapsed_time:.2f} s\n\n\n")
    
    return failed_maps

if __name__ == "__main__":
    # OPTIONAL REMOVE EITHER INPUT OR DATA!
    failed_maps1 = preprocess("./data", "output.csv")
    failed_maps2 = preprocess("./input", "input.csv")

    for map in failed_maps1:
        print(f"Failed to preprocess {map}")

    for map in failed_maps2:
        print(f"Failed to preprocess {map}")