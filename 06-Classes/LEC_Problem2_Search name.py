#Data:
#Rina Excell Sherlyn Farraz William Renato Ryan Fio Yoksan Nicholas
#Find Renato

data = ['Rina', 'Excel', 'Sherlyn', 'Farras', 'William', 'Renato', 'Ryan', 'Fio', 'Yoksan', 'Nicholas',]


def search(name):
    for i in data:
        if i == name:
            print('Eureka')
        else:
            continue

search('Renato')
