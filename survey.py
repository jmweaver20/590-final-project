"""Doctsring"""

"""Hello"""

# import os
# import math
from share import make_shares

#biggest prime that fits in 31 bits
#useful resource: https://t5k.org/lists/2small/

P = 2**31-1 # do we need to change this

# def make_shares(input: int, s1FileName: str, s2FileName: str) -> None:
#     """Input a number as input to the computation and two output share file names,
#     output two files with shares of the number."""

#     randBytes = os.urandom(math.ceil(math.log2(P)))

#     #produce shares s1 and s2, you need to convert randBytes to an integer mod P
#     s1 = int.from_bytes(randBytes, "big") % P
#     s2 = (input - s1) % P


#     s1Bytes = s1.to_bytes(length=4, byteorder='big')
#     s2Bytes = s2.to_bytes(length=4, byteorder='big')

#     #write the shares to the given files
#     s1File = open(s1FileName, "w")
#     s2File = open(s2FileName, "w")
#     s1File.write(s1Bytes.hex())
#     s2File.write(s2Bytes.hex())
#     s1File.close()
#     s2File.close()

#     return

print("Welcome to the CS + Gender Survey!")

name: str = input("What is your first name: ")
name: str = name.lower()

gender: str = str(input("What gender do you identify with (female, male, nonbinary): "))

while gender != "female" and gender != "male" and gender != "nonbinary":
    gender = input("What gender do you identify with (female, male, nonbinary): ")

if gender == "female":  
    make_shares(1, f"{name}_female_1.txt", f"{name}_female_2.txt")
    make_shares(0, f"{name}_male_1.txt", f"{name}_male_2.txt")
    make_shares(0, f"{name}_nonbinary_1.txt", f"{name}_nonbinary_2.txt")
elif gender == "male":
    make_shares(0, f"{name}_female_1.txt", f"{name}_female_2.txt")
    make_shares(1, f"{name}_male_1.txt", f"{name}_male_2.txt")
    make_shares(0, f"{name}_nonbinary_1.txt", f"{name}_nonbinary_2.txt")
elif gender == "nonbinary":
    make_shares(0, f"{name}_female_1.txt", f"{name}_female_2.txt")
    make_shares(0, f"{name}_male_1.txt", f"{name}_male_2.txt")
    make_shares(1, f"{name}_nonbinary_1.txt", f"{name}_nonbinary_2.txt")


# comp_major: str = str(input("Are you a comp sci major? (Y/N) "))

# if comp_major == "Y":
#     make_shares(1, f"{name}_comp_major_1.txt", f"{name}_comp_major_2.txt")
# elif comp_major == "N":
#     make_shares(0, f"{name}_comp_major_1.txt", f"{name}_comp_major_2.txt")


# wellness: int = int(input("On a scale of 1-5 (1 = terrible, 5 = better than ever), how would you rate your wellness in general? "))

# while wellness < 1 or wellness > 5:
#     wellness: int = int(input("On a scale of 1-5 (1 = terrible, 5 = better than ever), how would you rate your wellness in general? "))

# make_shares(wellness, f"{name}_wellness_1.txt", f"{name}_wellness_2.txt")


# comp_comfortability: int = int(input("On a scale of 1-5 (1 = terrible, 5 = better than ever), how comfortable do you feel in your comp sci classes? "))
# while comp_comfortability < 1 or comp_comfortability > 5:
#     comp_comfortability: int = int(input("On a scale of 1-5 (1 = terrible, 5 = better than ever), how comfortable do you feel in your comp sci classes? "))

# make_shares(comp_comfortability, f"{name}_comp_comfortability_1.txt", f"{name}_comp_comfortability_2.txt")


# other_comfortability: int = int(input("On a scale of 1-5 (1 = terrible, 5 = better than ever), how comfortable do you feel in your other classes? "))
# while other_comfortability < 1 or other_comfortability > 5:
#     other_comfortability: int = int(input("On a scale of 1-5 (1 = terrible, 5 = better than ever), how comfortable do you feel in your other classes? "))

# make_shares(other_comfortability, f"{name}_other_comfortability_1.txt", f"{name}_other_comfortability_2.txt")


# course_performance: int = int(input("On a scale of 1-5 (1 = terrible, 5 = better than ever), how do you feel about your course performance? "))
# while course_performance < 1 or course_performance > 5:
#     course_performance: int = int(input("On a scale of 1-5 (1 = terrible, 5 = better than ever), how do you feel about your course performance? "))

# make_shares(course_performance, f"{name}_course_performance_1.txt", f"{name}_course_performance_2.txt")


comp_professors: int = int(input("On a scale of 1-5 (1 = terrible, 5 = better than ever), how supported do you feel by your comp sci professors? "))
while comp_professors < 1 or comp_professors > 5:
    comp_professors: int = int(input("On a scale of 1-5 (1 = terrible, 5 = better than ever), how supported do you feel by your comp sci professors? "))

make_shares(comp_professors, f"{name}_comp_professors_1.txt", f"{name}_comp_professors_2.txt")


# gpa: int = int(float(input("What is your GPA (Round to 2 decimals if necessary)? ")) * 100)
# while gpa < 0 or gpa > 400:
#     gpa: int = int(float(input("What is your GPA (Round to 2 decimals if necessary)? ")) * 100)

# make_shares(gpa, f"{name}_gpa_1.txt", f"{name}_gpa_2.txt")