# LIST: ORDERED                           []
# list.append

# TUPLE: ORDERED, IMMUTABLE               ()

# SET: UNORDERED, only 1 value once       {}
# set()

# DICTIONARY                          {key: value}


set1 = {1,2,3}
set2 = set()
set1.add(4)
print(set1)

set3=set()
set3.add('john')
set3.add(9)
set3.add('miamia')

print(set3)

students = [
    {
        "name": "Jane Doe",
        "Math": 2,
        "English": 3
    }, 
    {
            "name": "Sarah Smith",
            "Math": 5,
            "English": 1
    }, 
     {
                "name": "Sam Doe",
                "Math": 4,
                "English": 5
    }, 
]

print(students[0])
print(students[0]['name'])
for student in students:
    print(student["name"])
    print(student["Math"])
    print(student["English"])