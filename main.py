import pandas as pd
from training import train_RFR, apply_RFR
import numpy as np
import returnlists as rl
from sklearn.metrics import mean_squared_error

def run_main():

    input_data_raw = pd.read_csv("input.csv", sep=",")
    #print(input_data_raw.columns)
    len_input_data_raw = len(input_data_raw)
    input_data = input_data_raw.dropna()
    len_input_data = len(input_data)
    diff_input = len_input_data_raw - len_input_data
    print(f"Dropped out {diff_input} samples because of missing data")

    data_raw = pd.read_csv("output.csv", sep=",")

    len_data_raw = len(data_raw)
    data = data_raw.dropna()
    len_data = len(data)
    diff = len_data_raw - len_data
    print(f"Dropped out {diff} samples because of missing data")


    # OPTIONAL FEATURE CHOICE!
    
    features = rl.return_all_features()
    #features = rl.return_rl()
    #features = rl.return_rl2()
    #features = rl.return_audio_features()
    #features = rl.return_map_features()
    #features = rl.return_website_features()

    x = data[features]
    y = data["rating"]
    x_input = input_data[features]

    RFR, RFR_score = train_RFR(x, y, 10, n_estimators=100, random_state=42, max_features="sqrt")

    x_input_id = input_data["beatmapid"]
    y_input = input_data["rating"] # truth of y

    y_predicted = apply_RFR(RFR, x_input) 

    mse = mean_squared_error(y_input, y_predicted)
    offsets = []

    print(f"\nPredicted\tTruth\t\tOffset\t\tBeatmapID")
    for id, truth, y_pred in zip(x_input_id, y_input, y_predicted):
        offset = float(abs(float(truth) - float(y_pred)))
        offsets.append(offset)
        print("{}\t\t{}\t\t{}\t\t{}".format(y_pred, truth, offset, id))
    fit_time = np.mean(RFR_score["fit_time"])
    score_time = np.mean(RFR_score["score_time"])
    test_score = np.mean(RFR_score["test_score"])
    train_score = np.mean(RFR_score["train_score"])
    

    print(f"\n\n\nRFR fit_time: {fit_time:.2f}\nRFR score_time: {score_time:.2f}\nRFR test_score: {test_score:.2f}\nRFR train_score: {train_score:.2f}\nRFR mse: {mse:.2f}")
 
    fi = RFR.feature_importances_
    print(f"\n\n\nFeature Importances:")
    for feature_name, importance in zip(x.columns, fi):
        print(f"{feature_name}: {importance*100:.2f}%")

    return offsets


if __name__ == "__main__":
    run_main()