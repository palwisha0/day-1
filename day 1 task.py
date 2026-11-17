# -------lists-------
numbers = [10,100,8,30,4,4,60,80]
#  1. largest numbers 
print ("largest:" , max(numbers))
#  2. second largest number 
unique_sorted = sorted(set(numbers))
print ("second largest:", (unique_sorted[-2]))
#  3. remove dublicate numbers
print ("without duplicate:", list(set(numbers)))
#  4. reversed without reversed() 
reversed_list =numbers [::-1]
print("reversed:", reversed_list)
list1 = [3, 4, 5, 6]
list2 = [5, 6, 7, 8]
# 5. common numbers between two lists
common = list(set(list1) & set(list2)) 
print("common:" , common)
 # ------TUPLES------
my_tuple = (10, 100, 8, 30, 4, 4, 60, 80)
print("Count of 4:", my_tuple.count(4))
tuple_to_list = list(my_tuple)
print("Tuple to List:", tuple_to_list)
list_to_tuple = tuple(tuple_to_list)
print("List to Tuple:", list_to_tuple)
my_list = [1, 2, 2, 3, 3, 4]
# ------SETS-------
print("Unique values:", set(my_list))
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("differene a - b:" , a - b)
print("differene b - a:" , b - a)
# -----DICTIONARIES-----
student = {"name": "Palwasha", "age": 22, "marks": 80}
print("Student:", student)
students_marks = {"Ali": 80, "Malaika": 90, "Usaid": 70}
average = sum(students_marks.values()) / len(students_marks)
print("Average Marks:", average)
sentence = "hello world hello python"
words = sentence.split()
