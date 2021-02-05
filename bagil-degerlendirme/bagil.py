# AUTHOR: BATIKAN BORA ORMANCI

import os
import statistics 
import math


MIN_GRADE = 20
MAX_GRADE = 100
TOLERANCE = [0, 0.1, 0.2]
FILE_NAME = "inf701-2021.txt"
PRINT_AA_WINNERS = False

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


grade_dict = {}

with open(os.path.join(__location__, FILE_NAME), "r") as f:
    #print(f.read())
    names_included = len(f.readline().split()) == 2 # read header line, find if length = 2
    #print(names_included)
    stud = -1
    for line in f.readlines():
        if (names_included):
            stud, grade = line.split()
        else:
            stud += 1
        grade = float(grade.replace(',','.'))
        if grade < MIN_GRADE:
            continue
        grade = min(grade, MAX_GRADE)

        grade_dict[stud] = grade

ct = len(grade_dict.values())
avg = statistics.mean(grade_dict.values())
std = statistics.stdev(grade_dict.values())
print("count of grades to partake in bagil degerlendirme: ", ct)
print("average ' ' ' ': ", avg)
print("standard deviation ' ' ' '", std)
print("----------")
if (std < 8 or ct < 20):
    print('MUTLAK DEGERLENDIRME YAPILACAK')
    exit(-1)

for t in TOLERANCE:
    aa=avg+std*(-2+(5.7-t)*(1/math.exp(avg/100)))
    ab=avg+std*(-2.3+(5.7-t)*(1/math.exp(avg/100)))
    ba=avg+std*(-2.7+(5.7-t)*(1/math.exp(avg/100)))
    bb=avg+std*(-3+(5.7-t)*(1/math.exp(avg/100)))
    bc=avg+std*(-3.3+(5.7-t)*(1/math.exp(avg/100)))
    cb=avg+std*(-3.7+(5.7-t)*(1/math.exp(avg/100)))
    cc=avg+std*(-4+(5.7-t)*(1/math.exp(avg/100)))
    dc=avg+std*(-4.3+(5.7-t)*(1/math.exp(avg/100)))
    dd=avg+std*(-4.7+(5.7-t)*(1/math.exp(avg/100)))
    df=avg+std*(-5+(5.7-t)*(1/math.exp(avg/100)))
    fd=avg+std*(-5.1+(5.7-t)*(1/math.exp(avg/100)))
    ff=0
    print("For tolerance value: ", t, " the grades will be distributed as follows:")
    print("aa", aa)
    print("ab", ab)
    print("ba", ba)
    print("bb", bb)
    print("bc", bc)
    print("cb", cb)
    print("cc", cc)
    print("dc", dc)
    print("dd", dd)
    print("df", df)
    print("fd", fd)
    print("ff", ff)

    if (PRINT_AA_WINNERS):
            
        print("students to take AA:")
        for k, v in grade_dict.items():
            if v >= aa:
                print(k)    


    print("------------------")
