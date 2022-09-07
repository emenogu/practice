import re

#Password is ABCdef123
s1 = 'emenogu'
# s = input('Enter Password: ')
s = 'ASDfgh123'
r = re.compile('[A-Z]{3}[a-z]{3}[0-9]{3}')
r1 = re.compile('[A-Za-z0-9]{5,99}')
l = re.findall(r, s)
l1 = re.findall(r1, s1)
print('Password entered is: ', l)
print('username entered is: ', l1)

m = re.search(r,s) #The re.search() func is used to check and tell you if the value s matches with the condition r.
# print(m)
if m:
    print(m.group())
else:
    print('Pattern does not match')
print()


# #DATE dd-mm-yyyy
# date = '02-09-2022'
# r_date = re.compile('^([0-9]{1,2})-([0-9]{1,2})-([0-9]{4})$') #Grouped using round brackets () around []{}
# s_date = re.findall(r_date, date)
# print(s_date)

# m_date = re.search(r_date,date)
# if m_date:
#     print(m_date.group(), 'matches with the pattern')
# else:
#     print('Pattern does not match')
    
 
# #DATE dd-mm-yyyy
# NAME GROUPING   
#Group, note that uppercase P used not lowercase p
date = '02-Sept-2022'
r_date = re.compile('^(?P<day>[0-9]{1,2})-(?P<month>[A-Za-z0=9]{1,9})-(?P<year>[0-9]{4})$')
s_date = re.findall(r_date, date)
print(s_date)

m_date = re.search(r_date,date)
if m_date:
    print('Day is:',(m_date.group(('day'))))
    print('Month is:',(m_date.group(('month'))))
    print('Year is:',(m_date.group(('year'))))
else:
    print('Pattern does not match')
print()    
    
## PHONE NO.
phone = '+234-7060481958'
r_phone = re.compile('(\+234\s?)?-?([0-9]{6,11})')
m_date = re.search(r_phone, phone)
print(m_date.group())




# month = ['Jan.', 'Feb.', 'Mar.', 'April', 'May', 'Jun.', 'Jul.', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']