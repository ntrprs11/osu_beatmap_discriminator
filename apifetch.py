import os
from dotenv import load_dotenv
from ossapi import *
import csv
import time
from datetime import datetime


async def get_data(client: OssapiAsync, folder_set_id):
    """Uses Folder Set ID to get all Websitedata"""
    
    set_id = folder_set_id
    client = client

    map = (await client.beatmapset(
        beatmapset_id=set_id))

    rating = map.ratings

    favourite_count_raw = map.favourite_count  # gets total fc

    all_diffs = map.beatmaps

    diffs = []
    for d in all_diffs:
        mode = str(d.mode)
        if mode == "GameMode.OSU":
            diffs.append(d)

    diffcount = len(diffs)

    genre_dic = map.genre

    language_dic = map.language

    genre = genre_dic["id"]
    language = language_dic["id"]
    bpm = map.bpm

    try:
        creator_name = map.creator

        creator = (await client.user(str(creator_name))).id

    except:
        creator = 0

    artist_full_name = map.artist
    artist_parts = artist_full_name.split(",")
    artist = ""
    for part in artist_parts:
        artist += str(part)

    ranked_date = str(map.ranked_date)
    ranked_datetime_obj = datetime.fromisoformat(ranked_date)
    seconds_since_epoch_since_ranked = int(ranked_datetime_obj.timestamp())
    seconds_since_epoch_exact = time.time()
    seconds_since_ranked = int(
        seconds_since_epoch_exact - seconds_since_epoch_since_ranked)

    beatmapids = []
    favourite_p = []
    difficultyratings = []
    playcount = []
    passcount = []
    successrate = []
    total_length = []
    ar_in_order = []
    cs_in_order = []
    hp_in_order = []  # referenced as drain
    od_in_order = []  # referenced as accuracy
    for d in diffs:  # gets all diff information
        mode = str(d.mode)
        if mode == "GameMode.OSU":  # makes sure only osu maps are being processed
            difficultyratings.append(d.difficulty_rating)
            beatmapids.append(d.id)
            playc = d.playcount
            passc = d.passcount
            favourite_rate = (favourite_count_raw / playc)
            favourite_p.append(favourite_rate)
            playcount.append(playc)
            passcount.append(passc)
            successrate.append(round(((passc / playc) * 100), 2))
            total_length.append(d.total_length)
            ar_in_order.append(d.ar)
            cs_in_order.append(d.cs)
            hp_in_order.append(d.drain)  # hp
            od_in_order.append(d.accuracy)  # od
    top_each_diff = []  # list in list
    pp_value_each_diff = []  # list in list
    for bid in beatmapids:
        map = (await client.beatmap(beatmap_id=bid))
        mode = str(map.mode)
        if mode == "GameMode.OSU":
            bm_scores = (await client.beatmap_scores(beatmap_id=bid)).scores
            top_3_map_player = []
            pp_values = []
            for s in bm_scores:
                top_3_map_player.append(s.user_id)
                pp_values.append(s.pp)
            top_value = 0
            top_player = 0
            for i, j in zip(top_3_map_player, pp_values):
                if j > top_value:
                    top_value = j
                    top_player = i

            top_each_diff.append(top_player)
            pp_value_each_diff.append(top_value)

    # fetch all difficulty attributes from API
    aim_difficulty = []
    approach_rate_diff = []
    overall_difficulty = []
    slider_factor = []
    speed_difficulty = []
    speed_note_count = []
    for bid in beatmapids:
        map_in_bid = (await client.beatmap_attributes(beatmap_id=bid)).attributes
        aim_difficulty.append(map_in_bid.aim_difficulty)
        approach_rate_diff.append(map_in_bid.approach_rate)
        overall_difficulty.append(map_in_bid.overall_difficulty)
        slider_factor.append(map_in_bid.slider_factor)
        speed_difficulty.append(map_in_bid.speed_difficulty)
        speed_note_count.append(map_in_bid.speed_note_count)

    # calculates the avg rating as float
    weighted_sum = sum((i) * x for i, x in enumerate(rating))
    total_weight = sum(rating)
    rating_float = weighted_sum / total_weight

    # data dictionary featuring all data
    data = {
        "rating": str(rating_float),
        "diffcount": str(diffcount),
        "set_id": str(set_id),
        "beatmapid": beatmapids,
        "bpm": str(bpm),
        "ranked_date": seconds_since_ranked,
        "difficultyrating": difficultyratings,
        "favourite_p": favourite_p,
        "favourite_count": str(favourite_count_raw),
        "language": str(language),
        "genre": str(genre),
        "creator": str(creator),
        "artist": str(artist),
        "playcount": playcount,
        "passcount": passcount,
        "successrate": successrate,
        "total_lengths": total_length,
        "ar_in_order": ar_in_order,
        "cs_in_order": cs_in_order,
        "hp_in_order": hp_in_order,
        "od_in_order": od_in_order,
        "aim_difficulty": aim_difficulty,
        "approach_rate_diff": approach_rate_diff,
        "overall_difficulty": overall_difficulty,
        "slider_factor": slider_factor,
        "speed_difficulty": speed_difficulty,
        "speed_note_count": speed_note_count,
        "top_map_player": top_each_diff,
        "pp_value": pp_value_each_diff
    }

    return data, diffcount



def write_csv(data, diffcount, path):
    with open(path + "/" + "websitefeature.csv", mode="w", newline="") as file:

        writer = csv.writer(file, delimiter=";")

        # write keys as first row
        writer.writerow(data.keys())

        # write rows
        # NEEDS FIX
        for i in range(diffcount):
            row_data = []
            for value in data.values():
                if isinstance(value, list):
                    if isinstance(value[i], list):  # top 3 map players, pp values
                        row_data.append(str(value[i]))
                    else:
                        row_data.append(value[i])
                else:
                    row_data.append(value)
            del row_data[-1:-6]
            writer.writerow(row_data)


if __name__ == "__main__":
    load_dotenv()

    apikey = str(os.getenv('api_key'))
    client_id = str(os.getenv('client_id'))
    client_secret = str(os.getenv('client_secret'))

    data, diffcount = get_data(client_id, client_secret, 1210496)
    print(data, diffcount)
    write_csv(data, diffcount, "./data")
