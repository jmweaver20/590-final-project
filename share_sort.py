"""File to sort all of the shares in a folder."""
import os
import shutil

sub_strings = ["_female_1.txt", "_female_2.txt", "_male_1.txt", "_male_2.txt", "_nonbinary_1.txt", "_nonbinary_2.txt", "_comp_professors_1.txt", "_comp_professors_2.txt"]

def sort_shares(folderpath: str):
    """Sorts shares in a folder into subfolders."""
    for filename in os.listdir(folderpath):
        # compare each file in the folder to each of the substrings to see whether they match
        for substring in sub_strings:
            if substring in filename:
                # move file into substring's folder if substring matches the end of the file
                sub_foldername = substring.replace(".txt", "")
                sub_foldername = sub_foldername.replace(sub_foldername[0], "", 1)
                src_path = f"{folderpath}/{filename}"
                dest_path = f"{os.getcwd()}/{sub_foldername}"
                # make the folder/directory for the shares to be stored in if it doesn't already exist
                if not os.path.exists(dest_path):
                    os.mkdir(dest_path)
                shutil.move(src_path, dest_path)

source_directory = os.getcwd()
sort_shares(f"{source_directory}/shares")