import random

def gen_password(length=8):
    spec = ['!', '#', '$', '-', '+', '~', '*', '%', '@']
    
    lowercase = chr(random.randint(97, 122))
    uppercase = chr(random.randint(65, 90))
    digits = random.randint(100, 999)
    special = random.choice(spec)
    password = (uppercase + special + str(digits) + lowercase + uppercase +
                special +uppercase + lowercase + str(digits) + lowercase + special)
    l = random.sample(password, length)
    password = ('').join(l)
    return password

# Choose length of password
result = gen_password(15)
print(result)



# Code to give us a more random password
result1 = random.choice(result)
result2 = random.choice(result)
result3 = random.choice(result)
result4 = random.choice(result)
result5 = random.choice(result)
result6 = random.choice(result)
result7 = random.choice(result)
result8 = random.choice(result)

print('')
print(result1 + result2 + result3 + result4 + 
      result5 + result6 + result7 + result8)





