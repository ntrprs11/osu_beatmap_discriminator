import math
import csv
import numpy as np
import librosa
from scipy import signal
import matplotlib.pyplot as plt


def load_audio_file(filename: str):
    # load the audio file via librosa library
    audio, sample_rate = librosa.load(filename, sr=None)
    audio = np.asarray(audio)
    return audio, sample_rate


def mp3_transformation(audio, sample_rate):
    # calculates the FFT
    frequencies = np.fft.rfft(audio)
    frequency_amplitudes = np.abs(frequencies)
    time_interval = 1 / sample_rate
    frequency_axis = np.fft.rfftfreq(len(audio), time_interval)
    return frequency_axis, frequency_amplitudes

# getting all hz-intervals from 40z to 20000hz
def all_hz_intervals(amps):
    freqs = np.arange(len(amps))
    intervals = [(40, 80), (80, 250), (250, 600), (600, 4000),
                 (4000, 6000), (6000, 8000), (8000, 20000)]
    values = []

    for low, high in intervals:
        # calculates the difference between low & high frequency (intervals)
        diffs = np.abs(freqs - low) + np.abs(freqs - high)
        # finds the minimal index of diffs value
        index_min = np.argmin(diffs)
        # finds the max index of diffs value
        index_max = np.argmin(
            np.abs(freqs - freqs[index_min] - high)) + index_min
        # extract the amlitudes- and frequency between the intervals
        freqs_bands = np.abs(freqs[index_min:index_max+1])
        amp_bands = np.abs(amps[index_min:index_max+1])
        value = freqs_bands, amp_bands
        values.append(value)

    return values


def seperate_hz_intervals(audio, sample_rate):
    freqs, amps = mp3_transformation(audio, sample_rate)
    values = all_hz_intervals(amps)
    # seperating each interval from values list
    value1 = values[0]  # 40 - 80 Hz
    value2 = values[1]  # 80 - 250 Hz
    value3 = values[2]  # 250 - 600 Hz
    value4 = values[3]  # 600 - 4000 Hz
    value5 = values[4]  # 4000 - 6000 Hz
    value6 = values[5]  # 6000 - 8000 Hz
    value7 = values[6]  # 8000 - 20000 Hz

    return value1, value2, value3, value4, value5, value6, value7


# features
# calculates every amplitude per millisecond
def get_amplitude_per_millisecond(amps, sample_rate):
    # total duration of the audio signal
    total_duration = (2 * len(amps)) / sample_rate

    # total duration of the audio signal in miliseconds
    total_milliseconds = int(total_duration * 1000)

    # empty array for each miliseconds of amps
    amplitude_per_millisecond = np.zeros(total_milliseconds)

    for i in range(total_milliseconds):
        # amps for the exact milisecond
        amplitude_per_millisecond[i] = amps[i]

    return total_milliseconds, amplitude_per_millisecond


def time_intervals(amps, sample_rate):
    total_milliseconds, amplitude_per_millisecond = get_amplitude_per_millisecond(
        amps, sample_rate)
    time_intervals_dict = {}  # empty dict for the intervalls

    interval_count = 10

    # calculates every interval size
    interval_size = math.ceil(total_milliseconds / interval_count)

    for i in range(interval_count):
        # calculates the start- & endpoint of every interval
        start_ms = i * interval_size
        end_ms = min((i + 1) * interval_size, total_milliseconds)
        interval_key = f"interval_{i + 1}"

        # extract values for the current interval
        interval_values = amplitude_per_millisecond[start_ms:end_ms]
        time_intervals_dict[interval_key] = interval_values

    return time_intervals_dict


def calculate_average_of_amps_per_millisecond(amps, sample_rate):
    # gets the intervals from time_intervals function
    time_intervals_dict = time_intervals(amps, sample_rate)

    averages = []  # empty list for every average of the time_intervals_dict

    for interval_values in time_intervals_dict.values():
        # calculates the average of values in the time_intervals_dict
        average = np.average(interval_values)
        # appending every average to the averages list
        averages.append(average)

    return averages  # returns the list of averages


# seperating the averages into values
def seperate_average_of_amps_per_ms(amps, sample_rate):
    averages = calculate_average_of_amps_per_millisecond(amps, sample_rate)
    average1_of_ms = averages[0]
    average2_of_ms = averages[1]
    average3_of_ms = averages[2]
    average4_of_ms = averages[3]
    average5_of_ms = averages[4]
    average6_of_ms = averages[5]
    average7_of_ms = averages[6]
    average8_of_ms = averages[7]
    average9_of_ms = averages[8]
    average10_of_ms = averages[9]

    return average1_of_ms, average2_of_ms, average3_of_ms, average4_of_ms, average5_of_ms, average6_of_ms, average7_of_ms, average8_of_ms, average9_of_ms, average10_of_ms

# calculates the 3 and 97 percent of each amp per millisecond of each intervall


def calculate_3_and_97_percent_amps_per_millisecond(amps, sample_rate):
    average1_of_ms, average2_of_ms, average3_of_ms, average4_of_ms, average5_of_ms, average6_of_ms, average7_of_ms, average8_of_ms, average9_of_ms, average10_of_ms = seperate_average_of_amps_per_ms(
        amps, sample_rate)

    average_values = [average1_of_ms, average2_of_ms, average3_of_ms, average4_of_ms, average5_of_ms,
                      average6_of_ms, average7_of_ms, average8_of_ms, average9_of_ms, average10_of_ms]

    # calculating 3%
    percent_3_values = [value * 0.03 for value in average_values]

    # calculating 97%
    percent_97_values = [value * 0.97 for value in average_values]

    return percent_3_values, percent_97_values


# seperating the 3% values from the list
def seperate_percent_3_values(amps, sample_rate):
    percent_3_values, _ = calculate_3_and_97_percent_amps_per_millisecond(
        amps, sample_rate)

    value1 = percent_3_values[0]
    value2 = percent_3_values[1]
    value3 = percent_3_values[2]
    value4 = percent_3_values[3]
    value5 = percent_3_values[4]
    value6 = percent_3_values[5]
    value7 = percent_3_values[6]
    value8 = percent_3_values[7]
    value9 = percent_3_values[8]
    value10 = percent_3_values[9]

    return value1, value2, value3, value4, value5, value6, value7, value8, value9, value10


# seperating the 97% values from the list
def seperate_percent_97_values(amps, sample_rate):
    _, percent_97_values = calculate_3_and_97_percent_amps_per_millisecond(
        amps, sample_rate)

    value1 = percent_97_values[0]
    value2 = percent_97_values[1]
    value3 = percent_97_values[2]
    value4 = percent_97_values[3]
    value5 = percent_97_values[4]
    value6 = percent_97_values[5]
    value7 = percent_97_values[6]
    value8 = percent_97_values[7]
    value9 = percent_97_values[8]
    value10 = percent_97_values[9]

    return value1, value2, value3, value4, value5, value6, value7, value8, value9, value10


# calculating 1/10 second of the frequencies (hz)
def calculate_freq_bands(freqs_intervals, amps, sample_rate):
    # empty list for frequency bands
    freq_bands = []
    for i in range(len(freqs_intervals)):
        # calculating the millisecond for the current index
        milliseconds = i / sample_rate * 10
        amp_interval = np.abs(amps[int(milliseconds)])

        # adding the amplitude interval value to the freq_bands list
        freq_bands.append(amp_interval)
    return freq_bands


# using the frequencies to calculate the amps per frequencies
def hz_per_seconds(audio, sample_rate):
    freqs, amps = mp3_transformation(audio, sample_rate)
    value1, value2, value3, value4, value5, value6, value7 = seperate_hz_intervals(
        audio, sample_rate)

    freqs_interval_1 = list(value1)
    freqs_interval_2 = list(value2)
    freqs_interval_3 = list(value3)
    freqs_interval_4 = list(value4)
    freqs_interval_5 = list(value5)
    freqs_interval_6 = list(value6)
    freqs_interval_7 = list(value7)

    # calculating frequency bands for each interval
    freq_bands1 = calculate_freq_bands(freqs_interval_1, amps, sample_rate)
    freq_bands2 = calculate_freq_bands(freqs_interval_2, amps, sample_rate)
    freq_bands3 = calculate_freq_bands(freqs_interval_3, amps, sample_rate)
    freq_bands4 = calculate_freq_bands(freqs_interval_4, amps, sample_rate)
    freq_bands5 = calculate_freq_bands(freqs_interval_5, amps, sample_rate)
    freq_bands6 = calculate_freq_bands(freqs_interval_6, amps, sample_rate)
    freq_bands7 = calculate_freq_bands(freqs_interval_7, amps, sample_rate)

    # making each amp per frequencie unique and sort them
    redundant_freq_bands1 = set(freq_bands1)
    sorted_freq_bands1 = sorted(redundant_freq_bands1)
    redundant_freq_bands2 = set(freq_bands2)
    sorted_freq_bands2 = sorted(redundant_freq_bands2)
    redundant_freq_bands3 = set(freq_bands3)
    sorted_freq_bands3 = sorted(redundant_freq_bands3)
    redundant_freq_bands4 = set(freq_bands4)
    sorted_freq_bands4 = sorted(redundant_freq_bands4)
    redundant_freq_bands5 = set(freq_bands5)
    sorted_freq_bands5 = sorted(redundant_freq_bands5)
    redundant_freq_bands6 = set(freq_bands6)
    sorted_freq_bands6 = sorted(redundant_freq_bands6)
    redundant_freq_bands7 = set(freq_bands7)
    sorted_freq_bands7 = sorted(redundant_freq_bands7)

    return sorted_freq_bands1, sorted_freq_bands2, sorted_freq_bands3, sorted_freq_bands4, sorted_freq_bands5, sorted_freq_bands6, sorted_freq_bands7


def calculate_list(list):
    avg = np.average(list)
    return avg


# calculates the 3% and 97% of amp per frequency of each hz intervall
def calculate_3_percent_and_97_percent(audio, sample_rate):
    sorted_freq_bands1, sorted_freq_bands2, sorted_freq_bands3, sorted_freq_bands4, sorted_freq_bands5, sorted_freq_bands6, sorted_freq_bands7 = hz_per_seconds(
        audio, sample_rate)

    # getting the length of each sorted frequency bands list
    list_lengths = [
        len(sorted_freq_bands1),
        len(sorted_freq_bands2),
        len(sorted_freq_bands3),
        len(sorted_freq_bands4),
        len(sorted_freq_bands5),
        len(sorted_freq_bands6),
        len(sorted_freq_bands7)
    ]

    # calculates the 3% value for each frequency band
    percent_values_3_percent = [sorted_band[int(0.03 * length)] for sorted_band, length in zip(
        [sorted_freq_bands1, sorted_freq_bands2, sorted_freq_bands3, sorted_freq_bands4,
            sorted_freq_bands5, sorted_freq_bands6, sorted_freq_bands7],
        list_lengths
    )]

    # calculates the 97% value for each frequency band
    percent_values_97_percent = [sorted_band[int(0.97 * length)] for sorted_band, length in zip(
        [sorted_freq_bands1, sorted_freq_bands2, sorted_freq_bands3, sorted_freq_bands4,
            sorted_freq_bands5, sorted_freq_bands6, sorted_freq_bands7],
        list_lengths
    )]

    return list_lengths, percent_values_3_percent, percent_values_97_percent


# this function appends all useful calculated data into the dictionary of the function create_table()
def append_hz_1_to_7_into_dict(audio, sample_rate, amps, audiofilepath):
    # creating an empty dictionary
    table_dict = {}

    import read_data
    folder_path = '/'.join(audiofilepath.split('/')[:-1])
    set_id = read_data.get_id_through_folder_name(folder_path)
    table_dict["set_id"] = set_id

    # filling the dictionary table_dict with "features" and "values"

    average1_of_ms, average2_of_ms, average3_of_ms, average4_of_ms, average5_of_ms, average6_of_ms, average7_of_ms, average8_of_ms, average9_of_ms, average10_of_ms = seperate_average_of_amps_per_ms(
        amps, sample_rate)

    _, power_density = mp3_transformation(audio, sample_rate)

    avg40_80 = calculate_list(power_density[40:80])
    avg80_250 = calculate_list(power_density[80:250])
    avg250_600 = calculate_list(power_density[250:600])
    avg600_4000 = calculate_list(power_density[600:4000])
    avg4000_6000 = calculate_list(power_density[4000:6000])
    avg6000_8000 = calculate_list(power_density[6000:8000])
    avg8000_20000 = calculate_list(power_density[8000:20000])

    table_dict["set_id"] = set_id
    table_dict["40-80 Hz"] = avg40_80
    table_dict["80-250 Hz"] = avg80_250
    table_dict["250-600 Hz"] = avg250_600
    table_dict["600-4000 Hz"] = avg600_4000
    table_dict["4000-6000 Hz"] = avg4000_6000
    table_dict["6000-8000 Hz"] = avg6000_8000
    table_dict["8000-20000 Hz"] = avg8000_20000
    
    # adding the average of amps per time

    table_dict["Avg of IV 1"] = average1_of_ms
    table_dict["Avg of IV 2"] = average2_of_ms
    table_dict["Avg of IV 3"] = average3_of_ms
    table_dict["Avg of IV 4"] = average4_of_ms
    table_dict["Avg of IV 5"] = average5_of_ms
    table_dict["Avg of IV 6"] = average6_of_ms
    table_dict["Avg of IV 7"] = average7_of_ms
    table_dict["Avg of IV 8"] = average8_of_ms
    table_dict["Avg of IV 9"] = average9_of_ms
    table_dict["Avg of IV 10"] = average10_of_ms

    value1, value2, value3, value4, value5, value6, value7, value8, value9, value10 = seperate_percent_3_values(
        amps, sample_rate)

    # adding the 3% of amps per time
    table_dict["3 Percent of IV 1"] = value1
    table_dict["3 Percent of IV 2"] = value2
    table_dict["3 Percent of IV 3"] = value3
    table_dict["3 Percent of IV 4"] = value4
    table_dict["3 Percent of IV 5"] = value5
    table_dict["3 Percent of IV 6"] = value6
    table_dict["3 Percent of IV 7"] = value7
    table_dict["3 Percent of IV 8"] = value8
    table_dict["3 Percent of IV 9"] = value9
    table_dict["3 Percent of IV 10"] = value10

    value1, value2, value3, value4, value5, value6, value7, value8, value9, value10 = seperate_percent_97_values(
        amps, sample_rate)

    # adding the 97% of amps per time
    table_dict["97 Percent of IV 1"] = value1
    table_dict["97 Percent of IV 2"] = value2
    table_dict["97 Percent of IV 3"] = value3
    table_dict["97 Percent of IV 4"] = value4
    table_dict["97 Percent of IV 5"] = value5
    table_dict["97 Percent of IV 6"] = value6
    table_dict["97 Percent of IV 7"] = value7
    table_dict["97 Percent of IV 8"] = value8
    table_dict["97 Percent of IV 9"] = value9
    table_dict["97 Percent of IV 10"] = value10

    return table_dict


# writes all features as a table in a csv data
def output_csv(table_dict, path):
    with open(path + "/" + "audiofeature.csv", mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(table_dict.keys())
        writer.writerow(table_dict.values())


def calc_data_and_create_csv(audiofilepath: str, outpath: str):
    # loading audio file
    audio, sample_rate = load_audio_file(audiofilepath)

    # calculate the FFT
    _, amps = mp3_transformation(audio, sample_rate)
        # creating the intervals from 40Hz to 20000Hz

    table_dict = append_hz_1_to_7_into_dict(
        audio, sample_rate, amps, audiofilepath)

    # writing the dictionary into a .csv file
    output_csv(table_dict, outpath)


if __name__ == "__main__":
    audiofilepath = './data/wings.mp3'
    outpath = './data/'
    calc_data_and_create_csv(audiofilepath, outpath)
