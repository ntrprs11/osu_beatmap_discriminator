import read_data
import featureextraction
from ossapi import *
import os
from dotenv import load_dotenv
import time


async def clean_data(client: OssapiAsync, folder: str):
    all_maps = read_data.list_all_folders_in_dir(folder)

    deletable_filepaths = []

    max = len(all_maps)
    count = 0

    print(f"\n\n\n\tStart cleaning data in '{folder}' ")
    print("[#]" + 40*"-" + "[#]")

    for map in all_maps:
        deletable_filepaths = []
        set_id = read_data.get_id_through_folder_name(map)
        # try:
        count_deletable_files = 0
        start_time = time.time()

        jpgs = read_data.return_filepaths_with_suffix(map, "jpg")
        jpegs = read_data.return_filepaths_with_suffix(map, "jpeg")
        pngs = read_data.return_filepaths_with_suffix(map, "png")
        osbs = read_data.return_filepaths_with_suffix(map, "osb")
        for jpg in jpgs:
            deletable_filepaths.append(jpg)
            count_deletable_files += 1
        for jpeg in jpegs:
            deletable_filepaths.append(jpeg)
            count_deletable_files += 1
        for png in pngs:
            deletable_filepaths.append(png)
            count_deletable_files += 1
        for osb in osbs:
            deletable_filepaths.append(osb)
            count_deletable_files += 1

        osus = read_data.return_filepaths_with_suffix(map, "osu")
        audionames = []
        for osu in osus:
            current_map = featureextraction.build_map(osu)
            id, audioname = featureextraction.return_information(
                current_map)
            audionames.append(audioname)

            client = client

            try:
                mode = str((await client.beatmap(
                    beatmap_id=id)).mode)
            except:
                diffnames = []
                ids_from_api = []
                diffs = (await client.beatmapset(beatmapset_id=set_id)).beatmaps
                for d in diffs:
                    version = d.version
                    id_from_api = d.id
                    diffnames.append(version)
                    ids_from_api.append(id_from_api)
                current_diff = osu.split("[")[-1].split("]")[0]
                for diffname, id_from_api in zip(diffnames, ids_from_api):
                    if current_diff == diffname:
                        mode = str((await client.beatmap(
                            beatmap_id=id_from_api)).mode)
            if mode != "GameMode.OSU":
                deletable_filepaths.append(osu)
                count_deletable_files += 1
        mp3s = read_data.return_filepaths_with_suffix(map, "mp3")
        mp4s = read_data.return_filepaths_with_suffix(map, "mp4")
        wavs = read_data.return_filepaths_with_suffix(map, "wav")
        oggs = read_data.return_filepaths_with_suffix(map, "ogg")
        avis = read_data.return_filepaths_with_suffix(map, "avi")
        m4vs = read_data.return_filepaths_with_suffix(map, "m4v")
        for mp3 in mp3s:
            parts = mp3.split("/")
            part = parts[-1]
            if part not in audionames:
                deletable_filepaths.append(mp3)
                count_deletable_files += 1
        for m4v in m4vs:
            parts = m4v.split("/")
            part = parts[-1]
            if part not in audionames:
                deletable_filepaths.append(m4v)
                count_deletable_files += 1
        for avi in avis:
            parts = avi.split("/")
            part = parts[-1]
            if part not in audionames:
                deletable_filepaths.append(avi)
                count_deletable_files += 1
        for mp4 in mp4s:
            parts = mp4.split("/")
            part = parts[-1]
            if part not in audionames:
                deletable_filepaths.append(mp4)
                count_deletable_files += 1
        for wav in wavs:
            parts = wav.split("/")
            part = parts[-1]
            if part not in audionames:
                deletable_filepaths.append(wav)
                count_deletable_files += 1
        for ogg in oggs:
            parts = ogg.split("/")
            part = parts[-1]
            if part not in audionames:
                deletable_filepaths.append(ogg)
                count_deletable_files += 1
        count += 1
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(
            f"Finished Map: {map}\nElapsed Time: {elapsed_time:.2f} s\nDeleted files: {count_deletable_files}\nProgress: {count}/{max}")
        print("[#]" + 40*"-" + "[#]")
        time.sleep(1)

        for files in deletable_filepaths:
            os.remove(files)

    print(f"\tFinished cleaning data in '{folder}' \n\n\n")


if __name__ == "__main__":
    load_dotenv()

    apikey = str(os.getenv('api_key'))
    client_id = str(os.getenv('client_id'))
    client_secret = str(os.getenv('client_secret'))
    import asyncio

    asyncio.run(clean_data(client_id, client_secret))
