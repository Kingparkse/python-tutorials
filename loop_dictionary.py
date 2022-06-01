person = {'name':'egoing','address' : 'seoul','interest' : 'Web'}
print(person['interest'])
print('----------------')
for key in person:
    print(key,':',person[key])
print('------------------------')
persons = [
    {'name':'egoing','address' : 'seoul','interest' : 'Web'},
    {'name':'park','address' : 'pohang','interest' : 'python'},
    {'name':'lee','address' : 'jeonju','interest' : 'hack'}
]

for person in persons:
    for key in person:
        print(key,':',person[key])
    print('--------------------------')