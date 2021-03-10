requested_name = [input('Name : ').title()]
req_password = [int(input('Password: '))]

dic = {'John': 123, 'Mike': 32}
auth = {'Admin': 142}


for req_name, req_pass in zip(requested_name, req_password):
    password = None
    if req_name in dic:
        print(f"Hello {req_name}")
        password = dic[req_name]
    elif req_name in auth:
        print("Hello Admin, It's All Yours!")
        password = auth[req_name]
    else:
        print("Wrong Username")
        break

    if req_pass == password:
        print("Access Granted.!")
    else:
        print("Access Denied.!")
