from random import *
import os
print(os.getcwd())

m_name = [x.strip() for x in open("m_name.txt",encoding = 'utf8')]
w_name = [x.strip() for x in open("w_name.txt",encoding = 'utf8')]
lastname = [x.strip() for x in open("lastname.txt",encoding = 'utf8')]


def person(gender = None):
    if gender == None:
        gender = choice(['m','w'])
    if gender not in ['m','w']:
        print('There are only two genders...')
        return None
    if gender == 'm':
        return choice(m_name),choice(lastname)
    else:
        last = choice(lastname)
        if last[-2:] in ['ый','ой']:
            last = last[:-2] + 'ая'
        elif last[-2:] == 'ий':
            last = last[:-2] + 'яя'
        else:
            last+='а'
        return choice(w_name),last

print(person())
print(person('m'))
print(person('w'))
print(person('abc'))




