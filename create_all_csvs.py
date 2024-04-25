import read_data
import os
from dotenv import load_dotenv
import featureextraction
import time
import apifetch
from ossapi import *
import mp3transformation


async def create_csvs(client: OssapiAsync, folder: str):
    all_maps = read_data.list_all_folders_in_dir(folder)
    list_of_failed_maps = []

    print("\tStarted creating all .csv files")
    print("[#]" + 40*"-" + "[#]")

    len_maps = len(all_maps)
    total_time_start = time.time()

    for map in all_maps:
        print(f"\t{map}")
        print("[#]" + 40*"-" + "[#]")
        osus = read_data.return_filepaths_with_suffix(map, "osu")
        for osu in osus:
            try:
                start_time = time.time()
                mapdata_dict, current_beatmap = featureextraction.return_dict(
                    osu)
                featureextraction.write_csv(mapdata_dict, map, current_beatmap)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print("Created Mapdata .csv for " +
                      str(current_beatmap["Version"]))
                print(f"Elapsed Time: {elapsed_time:.2f}")
                print("[#]" + 40*"-" + "[#]")

            except Exception as e:
                print(f"Error during creating Mapdata .csv for {osu}")
                print("[#]" + 40*"-" + "[#]")
                print(f"{e}")
                list_of_failed_maps.append(map)

        mp3s = read_data.return_filepaths_with_suffix(map, "mp3")
        oggs = read_data.return_filepaths_with_suffix(map, "ogg")
        MP3s = read_data.return_filepaths_with_suffix(map, "MP3")
        audios = []
        for mp3 in mp3s:
            audios.append(mp3)
        for ogg in oggs:
            audios.append(ogg)
        for MP3 in MP3s:
            audios.append(MP3)

        for audio in audios:
            try:
                start_time = time.time()
                mp3transformation.calc_data_and_create_csv(audio, map)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Created Audiodata .csv for {audio} in {map}")
                print(f"Elapsed Time: {elapsed_time:.2f}")
                print("[#]" + 40*"-" + "[#]")

            except Exception as e:
                print(
                    f"Error during creating Audiodata .csv for {mp3} in {map}")
                print("[#]" + 40*"-" + "[#]")
                print(f"{e}")
                list_of_failed_maps.append(map)

        try:
            start_time = time.time()
            set_id = int(read_data.get_id_through_folder_name(map))
            data, diffcount = await apifetch.get_data(client, set_id)
            apifetch.write_csv(data, diffcount, map)
            end_time = time.time()
            elapsed_time = end_time - start_time

            print(f"Created Websitedata .csv for {set_id} from {map}")
            print(f"Elapsed Time: {elapsed_time:.2f}")
            print("[#]" + 40*"-" + "[#]")
        except:
            print(f"Error during creating Websitedata .csv for {map}")
            print("[#]" + 40*"-" + "[#]")
            print(f"{e}")
            print("Sleeping 60 Seconds and skipping folder")
            time.sleep(60)
            list_of_failed_maps.append(map)

    total_time_end = time.time()
    total_time_elapsed = total_time_end - total_time_start

    print(f"\tFinished creating all .csv files")
    print(f"\t{total_time_elapsed:.2f} s for {len_maps} Maps")

    return set(list_of_failed_maps)

if __name__ == "__main__":
    load_dotenv()

    apikey = str(os.getenv('api_key'))
    client_id = str(os.getenv('client_id'))
    client_secret = str(os.getenv('client_secret'))

    create_csvs(client_id, client_secret)
