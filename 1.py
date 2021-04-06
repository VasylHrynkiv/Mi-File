class Entry:
    def login(self):
        form = input("Введіть пароль: ")
        if form == 'Aquatika': print("Привіт :D")
        elif form == 'підказка': print("Прив")
        else: 
            print("Пароль невірний")  
            Entry.login(self)
U = Entry()
U.login()

class Work:
    def create(self):
        f = open('text.txt', 'w')
        f.close()
    def wrt(self):
        with open('text.txt', 'w') as f:
            f.write(input("Запишіть в файл щось: "))
    def rd(self):
        with open('text.txt', 'r') as f:
            text = f.read()
        print(len(text))
        print(text)
W = Work()
W.create()
W.wrt()
W.rd()

#Василь Васильович Гриньків, група КІПЗс-2017
