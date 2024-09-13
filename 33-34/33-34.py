import json
a = {}
for i in range(3):
    name = input('Введите имя')
    age = int(input('Введите возраст'))
    a[name] = age
new_a = json.dumps(a, indent=2)
print(new_a)

with open('text3.json','w') as file:
    json.dump(a,file,indent=2)

with open('text3.json','r') as file:
    c = json.load(file)
f = 0
for value in c.values():
    if value > f:
        f=value
print(f)

