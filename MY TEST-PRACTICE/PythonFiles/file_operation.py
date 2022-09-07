
file = open("C:\\Users\\HP\\Documents\\Victory Chapel.txt", 'r') ##To open the file

## 1. 
filecontent = file.read()  #To read the opened file
# print(filecontent)

##Readlines()
# print('.................')
# filecontent = file.readlines()
# print(filecontent)

##Readline()
# filecontent = file.readline()
# print(filecontent)
# filecontent = file.readline()
# print(filecontent)
# # filecontent = file.readline()
# # print(filecontent)


for x in filecontent:
    print(x, end='')


