# AUTHOR: BATIKAN BORA ORMANCI

import os
import statistics 
import math


MIN_GRADE = 20
MAX_GRADE = 100
TOLERANCE = [0, 0.1, 0.2]
FILE_NAME = "ete2021.txt" # replace with your own file name
FILE_PATH = "grades/" + FILE_NAME
PRINT_AA_WINNERS = True

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


grade_dict = {}
grade = str()
with open(os.path.join(__location__, FILE_PATH), "r") as f:
    #print(f.read())
    names_included = len(f.readline().split()) == 2 # read header line, find if length = 2
    
    #print(names_included)
    stud = -1


    for line in f.readlines():
        if (names_included):
            stud, grade = line.split()
        else:
            stud += 1
            grade = line
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

letter_grades = {}
for t in TOLERANCE:
    # grade_letters = ["aa", "ab", "ba", "bb", "bc", "cb", "cc", "dc", "dd", "df", "fd", "ff"]

    letter_grades["aa"]=avg+std*(-2+(5.7-t)*(1/math.exp(avg/100)))
    letter_grades["ab"]=avg+std*(-2.3+(5.7-t)*(1/math.exp(avg/100)))
    letter_grades["ba"]=avg+std*(-2.7+(5.7-t)*(1/math.exp(avg/100)))
    letter_grades["bb"]=avg+std*(-3+(5.7-t)*(1/math.exp(avg/100)))
    letter_grades["bc"]=avg+std*(-3.3+(5.7-t)*(1/math.exp(avg/100)))
    letter_grades["cb"]=avg+std*(-3.7+(5.7-t)*(1/math.exp(avg/100)))
    letter_grades["cc"]=avg+std*(-4+(5.7-t)*(1/math.exp(avg/100)))
    letter_grades["dc"]=avg+std*(-4.3+(5.7-t)*(1/math.exp(avg/100)))
    letter_grades["dd"]=avg+std*(-4.7+(5.7-t)*(1/math.exp(avg/100)))
    letter_grades["df"]=avg+std*(-5+(5.7-t)*(1/math.exp(avg/100)))
    letter_grades["fd"]=avg+std*(-5.1+(5.7-t)*(1/math.exp(avg/100)))
    letter_grades["ff"]=0
    print("For tolerance value: ", t, " the grades will be distributed as follows:")
    for k, v in letter_grades.items():
        print(k, v)


    if (PRINT_AA_WINNERS):
            
        print("students to take AA:")
        for k, v in grade_dict.items():
            if v >= letter_grades['aa']:
                print(k, end=', ')    


    print("\n------------------")

# l is the list of grades
def print_grade_density(l):
    print_list = {}
    for g in l:
        if (print_list.keys().__contains__(g)):
            print_list[g] += "."
        else:
            print_list[g] = "."
        
    for k, v in print_list.items():
        print(k, v)
print_grade_density(grade_dict.values()) 


