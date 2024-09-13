def transfer(rubles,course):
    return rubles * course

def adult():
    age = int(input('Сколько вам лет'))
    if age >= 18:
        return True
    else:
        return False
    
print(adult())