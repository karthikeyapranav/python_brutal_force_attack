import getpass
from random import*
user_pass = getpass.getpass('enter password = ')
password = [1,2,3,4,5,6,7,8,9,0]
passw = ""
while(passw!= user_pass):
 passw = ""
 for letter in range(len(user_pass)):
     passw_num=password[randint(0,9)]
     passw = str(passw_num)+str(passw)
     print(passw)
print('your password is',passw)