# Create a list of students' names
students = ["Hermoine", "Harry", "Ron", "Draco"]

# Create a list of corresponding houses
houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]

# Create a dictionary where student names are keys and their houses are values
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# Print the house of "Hermoine"
print(students["Hermoine"])

# Print the house of "Harry"
print(students["Harry"])

# Print the house of "Ron"
print(students["Ron"])

# Print the house of "Draco"
print(students["Draco"])

# Loop through the dictionary and print student names
for student in students:
    print(student)

# Loop through the dictionary and print student names and their houses
for student in students:
    print(student, students[student])

# Loop through the dictionary and print student names, houses, and separator
for student in students:
    print(student, students[student], sep=", ")

# Create a list of dictionaries containing student information
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

# Loop through the list of dictionaries and print student information
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
