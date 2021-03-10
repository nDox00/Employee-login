requested_name = [input('Name : ').title()]
req_password = input('Password: ')

usernames = ['John','Mike', 'Will', 'Jack']
password = ['123', '1243']

for requested_name in requested_name:
    if requested_name in usernames:
        print (f'Hello {requested_name}')
    elif requested_name in auth:
        print('Hello Admin, Take Control')
    else:
        print ('Wrong Username')
        break
    
        if req_password in password:
            print('Access Granted')
        else:
            print('Access Denied')
       
## I need to research on how to use tuples..

