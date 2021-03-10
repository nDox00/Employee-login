requested_name = [input('Name : ').title()]
usernames = ['John','Mike', 'Will', 'Jack']
auth = ['Admin']

for requested_name in requested_name:
    if requested_name in usernames:
        print (f'Hello {requested_name}')
    elif requested_name in auth:
        print('Hello Admin, Take Control')
    else:
        print(f'Wrong Username')
        
        ## I might not need the 'for' as normally only checking one login at a time
