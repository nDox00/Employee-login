req_name = input('Name : ').title()
req_password = int(input('Password: '))

dic = {'John':123,'Mike':32}
auth = {'Admin': 142}

if req_name in dic.keys():
    if req_password == dic.get(req_name):
        print(f'Hello {req_name}')
        print('Access Granted')
    else:
        print(f'Sorry {req_name}, Access Denied')
        
elif req_name in auth.keys():
    if req_password == auth.get(req_name):
        print(f'Hello {req_name} take control')
        print('Access Granted')
    else:
        print(f'Sorry {req_name}, Access Denied')
else:
    print('Wrong Username')
