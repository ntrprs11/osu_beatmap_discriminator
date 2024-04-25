from beatmapparser import BeatmapParser
import math
import numpy as np
import csv


def build_map(filepath: str):
    parser = BeatmapParser()
    parser.parseFile(filepath)
    beatmap = parser.build_beatmap()

    return beatmap


def get_objects(beatmap):
    """Initialize BeatmapParser including parsing the file completely

    # create new List featuring all Objects [time, x, y, new_combo: bool]
    # hitobjects time = time, x = x, y = y
    # slider time = start time, x = start x, y = start y
    # 'slider'2 time = end time, x = end x, y = end y
    # spinner time = start time, x = mid, y = mid
    # 'spinner'2 time = end time, x = mid, y = mid
    SLIDER AND SPINNER ARE '2' OBJECTS"""

    objects = []
    # Reading all elements
    for ho in beatmap["hitObjects"]:
        if ho["object_name"] == "circle":
            time = ho["startTime"]
            x = ho["position"][0]
            y = ho["position"][1]
            new_combo_int = ho["newCombo"]
            new_combo = False
            if new_combo_int == 4:
                new_combo = True
            if new_combo_int == 0:
                new_combo = False
            object = [time, x, y, new_combo]
            objects.append(object)
        if ho["object_name"] == "slider":
            time = ho["startTime"]
            x = ho["position"][0]
            y = ho["position"][1]
            time2 = ho["end_time"]
            x2 = ho["end_position"][0]
            y2 = ho["end_position"][1]
            new_combo_int = ho["newCombo"]
            new_combo = False
            if new_combo_int == 4:
                new_combo = True
            if new_combo_int == 0:
                new_combo = False
            object1 = [time, x, y, new_combo]
            object2 = [time2, x2, y2, new_combo]
            objects.append(object1)
            objects.append(object2)
        if ho["object_name"] == "spinner":
            time = ho["startTime"]
            x = ho["position"][0]
            y = ho["position"][1]
            time2 = ho["end_time"]
            x2 = ho["position"][0]
            y2 = ho["position"][1]
            new_combo_int = ho["newCombo"]
            new_combo = False
            if new_combo_int == 4:
                new_combo = True
            if new_combo_int == 0:
                new_combo = False
            object1 = [int(time), int(x), int(y), new_combo]
            object2 = [int(time2), int(x2), int(y2), new_combo]
            objects.append(object1)
            objects.append(object2)

    return objects


def return_information(beatmap):
    """Input: parsed Beatmap
    
    Output: BeatmapID, Audiofilename"""
    id = beatmap["BeatmapID"]
    audiofilename = beatmap["AudioFilename"]

    return id, audiofilename


def calculate_physics(objects: list):
    """Input: objects

    Output: max_distance_time, mean_distance_time, max_distance, min_time_window, mean_distance, max_acceleration, mean_acceleration"""

    # [time, x, y, new_combo: bool]
    max_distance_time = 0
    max_distance = 0
    min_time_window = float("+inf")
    distance_times = []
    all_distances = []
    all_time_windows = []
    for i in range(0, len(objects) - 1):
        x_len = abs(objects[i+1][1] - objects[i][1])
        y_len = abs(objects[i+1][2] - objects[i][2])
        distance = math.sqrt(x_len**2 + y_len**2)

        all_distances.append(distance)
        time_diff = objects[i+1][0] - objects[i][0]
        all_time_windows.append(time_diff)

        distance_time = (distance / time_diff)
        distance_times.append(distance_time)

        if time_diff <= min_time_window:
            min_time_window = time_diff
        if distance >= max_distance:
            max_distance = distance
        if distance_time >= max_distance_time:
            max_distance_time = distance_time

    accelerations = []
    max_acceleration = 0
    for i in range(0, len(distance_times) - 1):
        d_v = abs(distance_times[i+1] - distance_times[i])
        d_t = abs(all_time_windows[i+1] - all_time_windows[i])
        if d_v == 0 or d_t == 0:
            continue
        else:
            acceleration = d_v / d_t
            accelerations.append(acceleration)

            if acceleration >= max_acceleration:
                max_acceleration = acceleration

    mean_distance_time = np.mean(distance_times)
    mean_distance = np.mean(all_distances)
    mean_acceleration = np.mean(accelerations)

    return max_distance_time, mean_distance_time, max_distance, min_time_window, mean_distance, max_acceleration, mean_acceleration


def calculate_angles(objects: list):
    """Input: objects
    
    Output: max angle, mean angle, min angle"""
    angles = []
    for i in range(1, len(objects) - 1):
        len_a_x = abs(objects[i-1][1] - objects[i][1])
        len_a_y = abs(objects[i-1][2] - objects[i][2])
        len_a = math.sqrt(len_a_x**2 + len_a_y**2)
        len_b_x = abs(objects[i][1] - objects[i+1][1])
        len_b_y = abs(objects[i][2] - objects[i+1][2])
        len_b = math.sqrt(len_b_x**2 + len_b_y**2)
        lengths = [len_a, len_b]
        lengths.sort(reverse=True)
        if lengths[1] == 0:
            angle = 0
            angles.append(angle)
        else:
            angle = np.degrees(np.arccos((lengths[1] / lengths[0])))
            angles.append(angle)

    max_angle = max(angles)
    min_angle = min(angles)
    mean_angle = np.mean(angles)

    return max_angle, min_angle, mean_angle


def calculate_max_rhythm_complexity(objects: list):
    """Input: objects

    Creates patterns featuring a list of all patterns and calculates max rhythm
    complexety of each pattern

    Formula: (patternlength / time_window)

    Output: float value rhythm complexity"""

    patterns = []
    pattern = []

    pattern.append([objects[0][0], objects[0][1],
                   objects[0][2], objects[0][3]])
    for i in range(1, len(objects)):
        nc_bool = objects[i][3]
        if nc_bool is True:
            patterns.append(pattern)
            pattern = []
            pattern.append([objects[i][0], objects[i][1],
                           objects[i][2], objects[i][3]])
        if nc_bool is False:
            pattern.append([objects[i][0], objects[i][1],
                           objects[i][2], objects[i][3]])

    # EXAMPLE PATTERNS LIST:[
    # [[3664, 255, 184, True]],
    # [[20279, 95, 66, True], [22125, 415, 66, False], [23048, 399, 194, False], [23971, 415, 322, False], [25818, 95, 322, False]], [[27202, 255, 34, True], [27664, 255, 34, False], [29510, 255, 322, False], [30433, 367, 258, False], [31356, 479, 194, False], [33202, 257, 62, False], [34125, 145, 126, False], [35048, 34, 191, False]],
    # [[57202, 333, 159, True]],
    # [[59049, 175, 158, True], [60894, 175, 159, False], [61818, 170, 324, False], [62741, 338, 324, False], [64588, 334, 159, False]],
    # [[75664, 256, 192, True]],
    # [[79356, 256, 192, True]],
    # [[101510, 467, 109, True]],
    # [[103357, 156, 51, True], [104279, 36, 191, False], [104741, 63, 279, False], [105202, 94, 365, False], [106126, 243, 317, False], [107048, 136, 166, False], [107972, 168, 13, False], [108433, 260, 24, False]],
    # [[108894, 351, 36, True]],
    # [[110741, 394, 369, True], [111664, 211, 337, False], [112587, 28, 306, False], [114434, 10, 139, False], [115356, 211, 337, False], [115818, 294, 353, False]],
    # [[116279, 384, 337, True]],
    # [[118126, 273, 40, True], [119048, 456, 15, False], [119972, 476, 197, False], [121819, 159, 194, False], [122741, 40, 336, False]],
    # [[123664, 221, 370, True]],
    # [[125511, 32, 138, True]],
    # [[126433, 256, 192, True]]
    # ]

    max_rhythm_complexity = 0
    for pattern in patterns:
        if len(pattern) == 1:
            continue

        patternlength = len(pattern)
        time_window = pattern[-1][0] - pattern[0][0]

        rhythm_complexity = (patternlength / time_window) * 100

        if rhythm_complexity >= max_rhythm_complexity:
            max_rhythm_complexity = rhythm_complexity

    return max_rhythm_complexity


def return_dict(path: str):
    map = build_map(path)
    id, _ = return_information(map)
    objects = get_objects(map)
    max_distance_time, mean_distance_time, max_distance, min_time_window, mean_distance, max_acceleration, mean_acceleration = calculate_physics(
        objects)
    max_rhythm_complexity = calculate_max_rhythm_complexity(objects)
    max_angle, min_angle, mean_angle = calculate_angles(objects)

    data = {
        "beatmapid": id,
        "max_v": max_distance_time,
        "mean_v": mean_distance_time,
        "max_x": max_distance,
        "min_t": min_time_window,
        "mean_x": mean_distance,
        "max_a": max_acceleration,
        "mean_a": mean_acceleration,
        "max_rhythm_complexity": max_rhythm_complexity,
        "max_angle": max_angle,
        "min_angle": min_angle,
        "mean_angle": mean_angle
    }

    return data, map


def write_csv(data, path, beatmap):
    with open(path + "/" + str(beatmap["BeatmapID"]) + "_mapfeature.csv", mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(data.keys())
        writer.writerow(data.values())


if __name__ == "__main__":
    testpath = './data/1561504 Eisyo-kobu - Oriental Blossom -Eika Shuuei-\Eisyo-kobu - Oriental Blossom -Eika Shuuei- (- Rem -) [Petals].osu'
    # write_csv(return_dict(testpath))
    map = build_map(testpath)
    print(map)
    id, audiofilename = return_information(map)
    print(id + "/" + audiofilename)