import os


def list_all_folders_in_dir(folderpath: str):
    all_folders = []
    all_files = os.listdir(folderpath)

    for f in all_files:
        if os.path.isdir(folderpath + "/" + f):
            all_folders.append(folderpath + "/" + f)

    return all_folders


def get_id_through_folder_name(folderpath: str):
    """Input: folderpath

    using .split in foldername (usually foldernames look like this: 1011011 nekodex - new beginnings

    Output: returns set id of folderpath"""
    if os.path.isdir(folderpath):  # checks if path is folder
        parts = folderpath.split(sep=" ")
        first_half = parts[0]  # extract id as the first part of name
        new_parts = first_half.split(sep="/")
        set_id = new_parts[-1]
        return set_id  # THIS IS THE SET_ID!!!


def split_name_append_if_osu(folder: str, list: list, target_list: list, suffix: str):
    """Input: folder for correct path, list to loop through, 
    target_list to append on, suffix to filter

    Output: target_list append for files with suffix"""
    for f in range(len(list)):
        files_split = list[f].split(".")
        if files_split[-1] == suffix:
            target_list.append(folder + "/" + str(list[f]))


def return_filepaths_with_suffix(folder: str, suffix: str):
    """Input: folderpath, suffix

    Output: List of all filepaths in a folder (including folderpaths) with the suffix"""

    # Creates a list featuring every direction in a folder
    files = os.listdir(folder)
    list_of_files = []

    for f in files:
        folderpath = str(folder) + "/" + str(f)
        if os.path.isdir(folderpath) is True:  # checks if folder or not
            folder_files = os.listdir(folderpath)
            split_name_append_if_osu(
                folderpath, folder_files, list_of_files, suffix)
        else:  # adds .osu filepaths to list_of_files
            files_split = f.split(".")
            if files_split[-1] == suffix:
                list_of_files.append(folderpath)

    return list_of_files
