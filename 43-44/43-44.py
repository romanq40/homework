class Programmer:
    def __init__(self,name,rang='junior',time=0):
        self.name = name
        self.rang = rang
        self.junior = 10
        self.middle = 15
        self.senior = 20
        self.salary = 0
        self.time = 0


    def work(self,time):
        if self.rang == 'junior':
            self.salary += time * self.junior
            self.time += time
            return self.salary,self.time
        elif self.rang == 'middle':
            self.salary += time * self.middle
            self.time += time
            return self.salary,self.time
        else:
            self.salary += self.senior * time
            self.time += time
            return self.salary,self.time

    def rise(self):
        if self.rang == 'junior':
            self.rang = 'middle'
            return self.rang
        elif self.rang == 'middle':
            self.rang = 'senior'
            return self.rang
        else:
            self.senior += 1
            return self.rang

    def info(self):
        print(f'Ваше имя {self.name} вы отработали {self.time} ваша зп составляет {self.salary}')

one = Programmer(name='Иван')
one.work(750)
one.info()
one.rise()
one.work(500)
one.info()
one.rise()
one.work(250)
one.info()
one.rise()
one.work(250)
one.info()
