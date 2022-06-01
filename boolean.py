input_id = input('id:' )
input_password = input('password:' )
id = 'park'
password = '0000'
if input_id == id:
    if input_password == password:
        print('wellcome'+id)
    else:
        print('wrong password')
else:
    print('wrong id')
