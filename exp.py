#Q.1- Write a python code to find a valid email address from a text.

import re
a=str(input("enter email"))
matcher=re.finditer('\w[_a-zA-Z0-9.]*[@](gmail.com|twitter.com)',a)
for m in matcher:
    print("Match is at :{},end :{},Pattern found :{}".format(m.start(),m.end(),m.group()))

#Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )

import re
p=input("enter phn no.")
m=re.finditer('(\+91-)[6789]{1}[0-9]{9}',p)
for i in m:
    print("Match is at :{},end :{},Pattern found :{}".format(i.start(),i.end(),i.group()))





