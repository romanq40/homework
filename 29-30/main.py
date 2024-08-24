import calc
print(calc.calcs(2,3))
import lists
text = ['jon','case','Andrey']
print(lists.list(text))
import hello
hello.hell('роман','силаев')

import requests
getdata = requests.get('https://jsonplaceholder.typicode.com/users')
print(getdata.content)
