requested_name = [input('Name : ').title()]
req_password = [int(input('Password: '))]

dic = {'John':123,'Mike':32}
auth = {'Admin': 142}

for requested_name in requested_name:
    if requested_name in dic.keys():
        print (f'Hello {requested_name}')
    
    elif requested_name in auth.keys():
        print('Hello Admin, Take Control')
    else:
        print ('Wrong Username')
        break
       
        if req_password in dic.values():
            print('Access Granted')
        else:
            print('Access Denied')
    
       
#Its not printing back after password
