import pandas as pd
import read_data
import os


def merge_csvs(folder, csv_name, failed_maps):
    all_folders = read_data.list_all_folders_in_dir(folder)
    all_successful_folders = [folder for folder in all_folders if folder not in failed_maps]

    print(all_successful_folders)

    deletable_csvs = []
    print(f"\n\n\n\tStarted Merging Process 0/3 \n\n\n")

    for map in all_successful_folders:
        csvs = read_data.return_filepaths_with_suffix(map, "csv")
        data_frames = []
        for i in range(len(csvs)):
            name = str(csvs[i])
            nameparts = name.split(sep="_")
            if nameparts[-1] == "mapfeature.csv":
                df = pd.read_csv(csvs[i], sep=";")
                data_frames.append(df)
                deletable_csvs.append(csvs[i])
        print("[#]" + 40*"-" + "[#]")
        print(f"\tStarted creating merged Mapdata .csv for {map}")

        merged_df = pd.concat(data_frames, ignore_index=True)
        merged_df.to_csv(map + "/" + "combinedmapfeature.csv",
                         index=False, sep=";")

        print(f"\tFinished creating merged Mapdata .csv for {map}")

    print("[#]" + 40*"-" + "[#]")
    for csv in deletable_csvs:
        print(f"\tDeleting {csv}")
        os.remove(csv)
    print("[#]" + 40*"-" + "[#]")

    print(f"\n\n\n\tFinished Merging Process 1/3 \n\n\n")

    deletable_csvs_2 = []
    print(f"\tStarted Merging 3 .csvs into 1  in each folder")
    print("[#]" + 40*"-" + "[#]")

    for map in all_successful_folders:
        print(f"\tStarted Merging .csvs for {map}")
        websitefeature = pd.read_csv(map + "/websitefeature.csv", sep=";")
        audiofeature = pd.read_csv(map + "/audiofeature.csv", sep=";")
        combinedmapfeature = pd.read_csv(
            map + "/combinedmapfeature.csv", sep=";")

        merged_df = pd.merge(websitefeature, combinedmapfeature,
                             on="beatmapid", how="inner")

        final_df = pd.merge(merged_df, audiofeature, on="set_id", how="inner")

        final_df.to_csv(map + "/" + "merged.csv", index=False)
        print(f"\tFinished Merging .csvs for {map}")
        print("[#]" + 40*"-" + "[#]")

        deletable_csvs_2.append(map + "/websitefeature.csv")
        deletable_csvs_2.append(map + "/audiofeature.csv")
        deletable_csvs_2.append(map + "/combinedmapfeature.csv")

    ("[#]" + 40*"-" + "[#]")
    print(f"\tDeleting unneeded .csvs")
    ("[#]" + 40*"-" + "[#]")
    for file in deletable_csvs_2:
        os.remove(file)
        print(f"Removed {file}")
        print("[#]" + 40*"-" + "[#]")

    print(f"\tFinished Merging 3 .csvs into 1 in each folder 2/3\n\n\n")

    print(f"\tStarted Merging all .csvs into 1 in root")
    print("[#]" + 40*"-" + "[#]")
    final_df_as_output = pd.read_csv(all_successful_folders[0] + "/merged.csv", sep=";")
    for i in range(1, len(all_successful_folders)):
        current_folder = all_successful_folders[i]
        current_df = pd.read_csv(all_successful_folders[i] + "/merged.csv", sep=";")
        final_df_as_output = pd.concat([final_df_as_output, current_df])
        print(f"Appended {current_folder}")
        print("[#]" + 40*"-" + "[#]")

    final_df_as_output.to_csv(csv_name, sep=";", index=False)
    print(f"Created output.csv")
    print("[#]" + 40*"-" + "[#]")

    for map in all_successful_folders:
        try:
            os.remove(map + "/merged.csv")
            print(f"Removed merged.csv in {map}")
            print("[#]" + 40*"-" + "[#]")
        except Exception:
            print(f"No removable merged.csv found in {map}")
            print("[#]" + 40*"-" + "[#]")

    print(f"\tFinished Merging all .csvs into 1 in root 3/3")


if __name__ == "__main__":
    merge_csvs()
