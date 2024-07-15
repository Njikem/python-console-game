import dbhelpers

def signup():

    print('Sign In or Create an account')

    username = input('Write your username')
    password = input('Write your password')
    print(username)
    print(password)

    result = dbhelpers.run_statement('call get_client(?, ?)', [username, password])
    print(result)
    if result:
        print('Signup is successful')
        return username

    else:
        print('Login failed, Please try again.')   

signup()


