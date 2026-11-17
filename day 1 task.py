                         # -------1. lists-------

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


                         # ------2. TUPLES------


my_tuple = (10, 100, 8, 30, 4, 4, 60, 80)
print("Count of 4:", my_tuple.count(4))

tuple_to_list = list(my_tuple)
print("Tuple to List:", tuple_to_list)

list_to_tuple = tuple(tuple_to_list)
print("List to Tuple:", list_to_tuple)


                         # ------3. SETS-------

my_list = [1, 2, 2, 3, 3, 4]
print("Unique values:", set(my_list))

#------1.Union-----
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)

#----2.Intersection-----

print("Intersection:", a & b)

#------3.differene-----
print("differene a - b:" , a - b)
print("differene b - a:" , b - a)


                          # -----4.DICTIONARIES-----


# -------1.student record-----
student = {
    "name": "Palwasha",
    "age": 22,
    "class": "BSCS",
    "city": "Lahore"
}
print(student)
print("Name:", student["name"])
print("City:", student["city"])

# ------2.Naya data add karna------

student["marks"] = 85
print(student)

# ----3.calculate everage marks----
students = {
    "palwisha": 85,
    "Noor": 90,
    "Fatima": 78,
    "Ali": 92
}
total = 0
for marks in students.values():
    total = total + marks
average = total / len(students)
print("Average Marks:", average)

# --------4.Sab se zyada marks wala--------
topper = max(students, key=students.get)
print("Topper:", topper)

# -------5.frequency of words--------


sentence = "python is easy and python is fun"
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print(frequency)