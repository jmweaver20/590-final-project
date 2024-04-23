"""Makeshift script file"""

from beavers import *
from server import *
from share_merge import *
from share import *
from share_sort import *

# starting with assuming shares have been moved to a shares folder
source_directory = os.getcwd()
move_to_shares()
sort_shares(f"{source_directory}/shares")

def average_across_gender(gender_cat: str, cat: str, names: list) -> int:
    filter_categories(gender_cat, cat, names)

    server_func("ashares", "n1.txt")
    server_func("bshares", "n2.txt")

    sum = share_merge("n1.txt", "n2.txt")

    server_func(f"{gender_cat}_1", "n1.txt")
    server_func(f"{gender_cat}_2", "n2.txt")

    num_students = share_merge("n1.txt", "n2.txt")

    if num_students > 0:
        if cat == "gpa":
            avg = {(sum / 100) / num_students}
        else:
            avg = {sum / num_students}
        print(f"{gender_cat}+{cat}: {avg}")
    else:
        avg = 0
        print(f"no {gender_cat} in dataset.")

    delete_dir(f"{source_directory}/ashares")
    delete_dir(f"{source_directory}/bshares")
    return avg

names_list = []
for filename in os.listdir(f"{source_directory}/comp_professors_1"):
    name = filename.partition("_")[0]
    if name not in names_list:
        names_list.append(name)

categories_list = ["comp_professors", "wellness", "comp_comfortability", "other_comfortability", "course_performance", "gpa"]

female_avgs: dict[str, float] = {}
male_avgs: dict[str, float] = {}
nonbinary_avgs: dict[str, float] = {}

for category in categories_list:
    female_avgs[category] = average_across_gender("female", category, names_list)
    male_avgs[category] = average_across_gender("male", category, names_list)
    nonbinary_avgs[category] = average_across_gender("nonbinary", category, names_list)

print(female_avgs)
print(male_avgs)
print(nonbinary_avgs)