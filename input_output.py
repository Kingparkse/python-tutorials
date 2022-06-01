name = input('name :')
message = 'hi, '+name+'...bye,'+name+'.'
print(message)


input_id = input('id:')
input_password = input('password:')
if input_id == 'egoing':
    if input_password == '0000':
        print('welcome')
# and로 if문 통합
if input_id == 'egoing' and input_password =='0000'
    print('welcome')

if input_id =='egoing':
    print('welcome')
if input_id == 'basta':
    print('welcome')
# or로 if 문 통합
if input_id =='egoing' or input_id == 'basta':
    print('welcome')