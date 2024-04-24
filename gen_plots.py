from script import female_avgs, male_avgs, nonbinary_avgs, num_students

import matplotlib.pyplot as plt

PINK = "#fb56e2"
BLUE = "#0fb2f5"
GREEN = "#73e27b"

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i] + 0.03, y[i], ha = 'center')

def generate_plot(cat: str) -> None:
    x = ["male", "female", "nonbinary"]
    y = []

    y.append(male_avgs[cat])
    y.append(female_avgs[cat])
    y.append(nonbinary_avgs[cat])

    plt.xlabel("Gender Categories")
    if cat == "gpa":
        plt.ylabel("Average GPA")
        plt.title(f"Reported {cat} Across Gender")
    else:
        plt.ylabel("Average Rating")
        plt.title(f"Rating of {cat} Across Gender")

    bars = plt.bar(x,y)
    bars[0].set_color(BLUE)
    bars[1].set_color(PINK)
    bars[2].set_color(GREEN)
    addlabels(x, y)
    plt.show()

def generate_gender_counts() -> None:
    x = ["male", "female", "nonbinary"]
    y = []

    y.append(num_students["male"])
    y.append(num_students["female"])
    y.append(num_students["nonbinary"])

    plt.xlabel("Gender Categories")
    plt.ylabel("Number of Students")
    plt.title(f"Number of Students Across Gender")

    bars = plt.bar(x,y)
    bars[0].set_color(BLUE)
    bars[1].set_color(PINK)
    bars[2].set_color(GREEN)
    plt.show()

def generate_majors() -> None:
    x = ["comp_majors", "non_comp_majors"]
    y = []

    y.append(num_students["comp_major"])
    non_comp_majors = (num_students["nonbinary"] + num_students["female"] + num_students["male"]) - num_students["comp_major"]
    y.append(non_comp_majors)

    plt.xlabel("Major Categories")
    plt.ylabel("Number of Students")
    plt.title(f"Number of Students Across Majors")

    bars = plt.bar(x,y)
    bars[0].set_color(BLUE)
    bars[1].set_color(GREEN)
    plt.show()




