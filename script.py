"""Makeshift script file"""

from beavers import *
from server import *
from share_merge import *
from share import *
from share_sort import *

# If files have not been sorted, they will be
source_directory = os.getcwd()
if not os.path.exists(f"{source_directory}/female_1"):
    move_to_shares()
    sort_shares(f"{source_directory}/shares")


def count_students(gender_cat: str) -> int:
    server_func(f"{gender_cat}_1", "n1.txt")
    server_func(f"{gender_cat}_2", "n2.txt")

    num_students = share_merge("n1.txt", "n2.txt")

    return num_students


def average_across_gender(gender_cat: str, cat: str, names: list) -> float:
    filter_categories(gender_cat, cat, names)

    server_func("ashares", "n1.txt")
    server_func("bshares", "n2.txt")

    sum = share_merge("n1.txt", "n2.txt")

    num_students = count_students(gender_cat)

    avg: float = 0.0
    if num_students > 0:
        if cat == "gpa":
            avg = (sum / 100) / num_students
        else:
            avg = sum / num_students
        print(f"{gender_cat}+{cat}: {avg}")
    else:
        avg = 0
        print(f"no {gender_cat} in dataset.")

    delete_dir(f"{source_directory}/ashares")
    delete_dir(f"{source_directory}/bshares")
    return avg


def get_names(names_list: list) -> None:
    for filename in os.listdir(f"{source_directory}/comp_professors_1"):
        name = filename.partition("_")[0]
        if name not in names_list:
            names_list.append(name)

names = []
get_names(names)

gender_list = ["male", "female", "nonbinary", "comp_major"]
categories_list = ["comp_professors", "wellness", "comp_comfortability", "other_comfortability", "course_performance", "gpa"]

num_students: dict = {}
female_avgs: dict = {}
male_avgs: dict = {}
nonbinary_avgs: dict = {}

for gender in gender_list:
    num_students[gender] = count_students(gender)


for category in categories_list:
    female_avgs[category] = average_across_gender("female", category, names)
    male_avgs[category] = average_across_gender("male", category, names)
    nonbinary_avgs[category] = average_across_gender("nonbinary", category, names)
