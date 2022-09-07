
def validate(username, password):
    if username == 'uche' and password == '1234':
        return ('Valid Login')
    else:
        return ('Invalid Login')
    
def get_details(**kwargs):
    print(kwargs)    
    

login = validate('uche', '1234')
print(login)
print(login, login, sep=', ', end='.')
print(' ')

get_details(names='Emenogu Uchenna', age='28', email='uche@aol.com', phone='0708879444' )


