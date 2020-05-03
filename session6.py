#sorting lists alphabetically 

studentsInClass = ["Katy", "Bob", "Alice", "Jake", "Zack", "Fatemeh"]
studentsInClass.sort()

print("students in clasS: ", studentsInClass)

studentsInClass.sort(reverse=True)
print("reverse order: ", studentsInClass)

def sorting_list(students):
	return sorted(students)

new_students = ["Janice", "Damien", "Cady"]
print("Mean girls gang: ", new_students)
print("Alphabetical: ", sorting_list(new_students))	

# The idea is that when you use "sort()", you're essentially changing the 
# order of the list, but if you use "sorted()" then it's temporary

studentsInClass.reverse()
print("if you wanna reverse the sort: ", studentsInClass)

#find length of a list
num_of_students = len(studentsInClass)
print("I have ", num_of_students, " in my class")