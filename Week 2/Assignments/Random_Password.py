
import random
import string 
READ_FILE = r"Week 2\Assignments\Users-Pwds.txt"
WRITE_FILE = r"Week 2\Assignments\Users-Pwds-Chked.txt"

def rank(pwd: str) -> str:

    contains_lowercase = any([(char in string.ascii_lowercase) for char in pwd ])
    contains_uppercase = any([(char in string.ascii_uppercase) for char in pwd])
    contains_digits = any([char in string.digits for char in pwd])
    contains_specials = any([char in string.punctuation for char in pwd])
    
    requirements = [contains_lowercase, contains_uppercase, contains_digits, contains_specials] 
    req_count = 0 
    for count in requirements: 
        if count is True:
            req_count = req_count+1

    if req_count < 3:
        return "POOR"

    elif req_count < 4:
        return "MODERATE"

    else:
        return "STRONG"

    
def option1():
   
    with open(READ_FILE, 'r') as file1:
        lines = file1.readlines()
    check_password = []
    for line in lines:
        username,password = line.split(',')
        password = password.strip() # removes the spaces and new lines from string
        ranked_password = rank(password)
        check_password.append((username,password,ranked_password)) #made tuple 
    
    with open(WRITE_FILE, 'a') as file2:
        for check in check_password:
            written = ','.join(check) # tuple to string 

            file2.write(written)
            file2.write('\n')

    print('#'*80)
    # [INFO] Be sure to change userpwds with the name of variable that you give to the list of passwords
    print('[INFO] '+'Number of passwords checked:',str(len(check_password))) 
    print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
    print('#'*80)

def option2():
    
    def generate() -> str:
       
        Ualphabets = string.ascii_uppercase
        Lalphabets = string.ascii_lowercase
        chars = string.punctuation
        digits = string.digits

        random_ualpha =''.join(random.sample(Ualphabets, 5 ))
        random_lalpha = ''.join(random.sample(Lalphabets, 5))
        random_char =''.join(random.sample(chars, 5))
        random_digits = ''.join(random.sample(digits, 5))

        pwd = random_ualpha + random_lalpha + random_char + random_digits
    
        return pwd
    

    # Generate the password using generate() and follow the steps as guided in the function header. 

    ## START CODE HERE

    ## END CODE HERE

def main():

    print('Welcome to my password ranking program')
    while True:
        print('-'*40)
        print('Please select one of 3 options')
        print('option1. Rank password from an existing file \t option2. Generate a strong password \noption3. exit the program')
        inp = input("Enter your option here:")
        
        
        try: 
            integer = int(inp)
        except Exception:
            print('Conversion Error')
            continue # goes up to line 155 as error handling 

        if integer == 1: # check and write
            option1()
        elif integer == 2: #generate new pass
            option2()
        elif integer == 3:
            print('Exiting the program')
            break 
        else:
            print("invalid option")
       

if __name__=='__main__':
   main()
   
