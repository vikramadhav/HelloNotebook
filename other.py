# ot=[i for i in range(2,6)]


# print(ot)


import os
import random

# print(os.getcwd())
# print(os.listdir())
# os.makedirs('myfolder')
# os.chdir(os.getcwd()+'/myfolder')
# print(os.getcwd())

os.chdir(os.getcwd()+'/myfolder')
if 'myfolder' not in os.listdir():
    os.mkdir('myfolder')
else :
    os.mkdir('myfolder'+str(random.randint(1,20)))

print(os.listdir())
