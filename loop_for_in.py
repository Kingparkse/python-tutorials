persons = [
    ['egoing','seoul','Web'],
    ['basta','seoul','iot'],
    ['blackdew','tongyeong','ml'],
]

print(persons[2] [1])

for person in persons:
    print(person)
person = persons[0]
name = person[0]
address = person[1]
interest = person[2]
print(name,address,interest)

name,address,interest = ['egoing','seoul','web']
print(name,address,interest)

for name,address,interest in persons:
    print(name,address,interest)
