import matplotlib.pyplot as plt
import pandas as pd

def trainingsdata_histogram():
    all_data = pd.read_csv("output.csv", sep=",")
    all_data = all_data.dropna()
    data = list(all_data["rating"])

    data_rounded = []
    for i in data:
        rounded_value = min(round(float(i), 1), 10)
        data_rounded.append(rounded_value)

    print(data_rounded)
    dictionary = {}

    for rating in data_rounded:
        if rating in dictionary:
            dictionary[rating] += 1
        else:
            dictionary[rating] = 1

    plt.bar(dictionary.keys(), dictionary.values())
    plt.title('histogram of trainingsdata ratings (rounded one decimal)')
    plt.xlabel('ratings')
    plt.ylabel('amount')

    plt.savefig('trainingsdata_ratings.png')

    plt.show()

def trainingsdata_histogram_gaus():
    all_data = pd.read_csv("output.csv", sep=",")
    all_data = all_data.dropna()
    data = list(all_data["rating"])

    data_rounded = []
    for i in data:
        rounded_value = min(round(float(i), 1), 10)
        data_rounded.append(rounded_value)

    print(data_rounded)
    dictionary = {}

    for rating in data_rounded:
        if rating in dictionary:
            dictionary[rating] += 1
        else:
            dictionary[rating] = 1

    import numpy as np

    x = np.array(list(dictionary.keys()))
    y = np.array(list(dictionary.values()))
    coefficients = np.polyfit(x, y, 5)

    x_curve = np.linspace(x.min(), x.max(), 100)
    y_curve = np.polyval(coefficients, x_curve)

    plt.plot(x_curve, y_curve)
    plt.title('histogram of trainingsdata ratings fitted polynomial')
    plt.ylim(bottom=0)
    plt.xlabel('x')
    plt.ylabel('y')

    plt.savefig('trainingsdata_ratings_gaus.png')

    plt.show()

def testdata_histogram():
    all_data = pd.read_csv("input.csv", sep=",")
    all_data = all_data.dropna()
    data = list(all_data["rating"])

    data_rounded = []
    for i in data:
        rounded_value = min(round(float(i), 1), 10)
        data_rounded.append(rounded_value)

    print(data_rounded)
    dictionary = {}

    for rating in data_rounded:
        if rating in dictionary:
            dictionary[rating] += 1
        else:
            dictionary[rating] = 1

    plt.bar(dictionary.keys(), dictionary.values())
    plt.title('histogram of testdata ratings (rounded one decimal)')
    plt.xlabel('ratings')
    plt.ylabel('amount')

    plt.savefig('testdata_ratings.png')

    plt.show()

def offset_histogram():
    from main import run_main
    offsets = run_main()
    dictionary = {}
    data_rounded = []

    for i in offsets:
        rounded_value = min(round(float(i), 1), 10)
        data_rounded.append(rounded_value)
    
    for rating in data_rounded:
        if rating in dictionary:
            dictionary[rating] += 1
        else:
            dictionary[rating] = 1

    plt.bar(dictionary.keys(), dictionary.values())
    plt.title('histogram of offset from truth (rounded one decimal)')
    plt.xlabel('offset')
    plt.ylabel('amount')

    plt.savefig('offset_histogram.png')

    plt.show()

def check_inputs():
    all_data = pd.read_csv("output.csv", sep=",")
    all_data = all_data.dropna()
    all_data2 = pd.read_csv("input.csv", sep=",")
    all_data2 = all_data2.dropna()

    set_ids = set(all_data["set_id"])
    set_ids2 = set(all_data2["set_id"])

    duplicates = []
    for s in set_ids2:
        if s in set_ids:
            duplicates.append(s)
        else:
            continue

    return duplicates

if __name__ == "__main__":
    #print(check_inputs())
    testdata_histogram()
    trainingsdata_histogram()
    trainingsdata_histogram_gaus()
    offset_histogram()