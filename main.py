from pyscript import display, document

def create_account(e):
    document.getElementById('output').innerHTML = ' '
    
    username = document.getElementById('username').value
    password = document.getElementById('password').value


    if len(username) < 7:
        display('Username must be at least 7 characters', target='output')

    else:

        if len(password) < 10:
            display('Password must be at least 10 characters', target='output')

        else:

            has_letter = False
            for c in password:
                if c >= 'A' and c <= 'Z' or c >= 'a' and c <= 'z':
                    has_letter = True
                    break 

            
            has_number = False
            for c in password:
                if c >= '0' and c <= '9':
                    has_number = True
                    break  

            if has_letter == False:
                display('Password must contain at least 1 letter', target='output')

            elif has_number == False:
                display('Password must contain at least 1 number', target='output')

            else:
                display('Account Created Successfully!', target='output')