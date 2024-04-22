"""Makeshift script file"""

from beavers import *
from server import *
from share_merge import *
from share import *
from share_sort import *

# starting with assuming shares have been moved to a shares folder
source_directory = os.getcwd()
sort_shares(f"{source_directory}/shares")

#TODO: add code to move shares into shares folder

names_list = []
for filename in os.listdir(f"{source_directory}/comp_professors_1"):
    name = filename.partition("_")[0]
    if name not in names_list:
        names_list.append(name)

print(names_list)

filter_categories("female", "comp_professors", names_list)

server_func("ashares", "n1.txt")
server_func("bshares", "n2.txt")

sum = share_merge("n1.txt", "n2.txt")

server_func("female_1", "n1.txt")
server_func("female_2", "n2.txt")

num_females = share_merge("n1.txt", "n2.txt")

print(sum / num_females)

