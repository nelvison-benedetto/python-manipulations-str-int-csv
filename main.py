# numbers = [1,2,3]
# name = "Angela"
# names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
# new_numbers = [ n + 1 for n in numbers]
# new_name = [letter for letter in name]
# print(new_numbers)
# print(new_name)
#
# range_list = [ num*2  for num in range(1,5) ]
# print(range_list)
# short_names = [name.upper() for name in names if len(name)>5]
# print(short_names)


# #GET LIST OF SQUARED NUMS WITHOUT LOOPS
# numbers = [1,1,2,3,5,8,13,21,34,55]
# squared_nums = [n*n for n in numbers]  #NON HO USATO UN LOOP!HO OTTENUTO SAME RESULT!!
# #print(squared_nums)
#
# #INSERT NUMS IN LIST & CONVERT IN INT
# #print("insert the numbers: ")
# list_of_str = input().split(',')
# list_of_ints = [int(n) for n in list_of_str]
# pair_nums = [n for n in list_of_ints if n%2==0]
# #print(pair_nums)

# #LIST FILE1 + FILE2 COMMON NUMS
# with open("file1.txt", mode="r") as file1_data:
#     file1_content = file1_data.readlines()
#     file1_content_stripped = [n.replace("\n","").strip() for n in file1_content]
# with open("file2.txt", mode="r") as file2_data:
#     file2_content = file2_data.readlines()
#     file2_content_stripped = [n.replace("\n","").strip() for n in file2_content]
# common_nums = [int(n) for n in file1_content_stripped if n in file2_content_stripped]
# print(common_nums)

#LIST FILE1 + FILE2 UNIQUE NUMS
# file1plusfile2 = file1_content_stripped + file2_content_stripped
# fileuniquenums = []
# for n in file1plusfile2:
#     if (n not in fileuniquenums):
#         fileuniquenums.append(n)
# print(fileuniquenums)

#!!DICTIONARIES
# import random
# names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
# students_score = {student:random.randint(1,100) for student in names}  #USE {} NOT []
# passed_students = {student:score for (student,score) in students_score.items() if score >59}
#   #{chiave: valore for elemento in iterabile if condizione}
#   #passa attraverso tutti gli items in coppia chiamata (student,score)
# print(students_score)
# print(passed_students)


# #CALCULATE NUMS LETTERS OF EACH WORD IN INPUT
# print("Insert your sentence:")
# list_str = input().split(' ')
# list_countstr = {n : len(n) for n in list_str}
# print(list_countstr)

#CALCULATE CELSIUS-FARENHEIT
# def Conversion(x):
#         return (x*9/5)+ 32
# dict_temp_c = {}
# n_index = 0
# isPlaying = True
# while(isPlaying):
#     print("Add a temperature:")
#     temp_c = float(input())
#     n_index+=1
#     dict_temp_c.update({n_index:temp_c})
#     print("Do you want add more temperatures?(y/n)")
#     choiche_continue = input().strip()
#     if (choiche_continue != "y"):
#         break
# print(dict_temp_c)
# print("Conversion in Fahrenheit...")
# dict_temp_f = ({index:Conversion(value) for index,value in dict_temp_c.items()})
#   #!!FOR INDEX,VALUE NEEDS TO ITERATE THE DICT CELSIUS ON BOTH, SO USE .ITEMS()!!
# print(dict_temp_f)
# # for index,value in dict_temp_f.items():
# #     print(f"the index is {index} the value is {value}")

students_dict = {
    "student" : ["Angela","Zhu","Xi"],
    "score" : [56,89,34]
}
# for (key,value) in students_dict.items():
#     print(value)
import pandas
# student_DF = pandas.DataFrame(students_dict)
# #print(student_DF)
#
# #loop throught a data frame
# for (key,value) in student_DF.items():
#     print(value)
#
# #loop throught a data frame
# for (index,row) in student_DF.iterrows():
#     print(row.student)  #print only names student

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index,row) in alphabet_data.iterrows()}
print(alphabet_dict)
theword = input("Insert the word: ").upper()
#letters = [letter for letter in theword]
#letters_dict = {index: value for index,value in enumerate(theword)}

result_list = [alphabet_dict[letter] for letter in theword]
    #itera su ogni lettera di theworld e ottiene il corrispondente valore del dizionario alphabet_dict[letter]
print(result_list)



