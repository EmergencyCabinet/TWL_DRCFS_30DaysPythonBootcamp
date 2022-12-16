# Feel free to add as much lines as you want between ## START CODE HERE and ## END CODE HERE.
# Please donot write code outside this boundry or you may fail the test.

# start by importing the necessary documents

import random
import string 
READ_FILE = r"Week 2\Assignments\Users-Pwds.txt"
WRITE_FILE = r"Week 2\Assignments\Users-Pwds-Chked.txt"

def rank(pwd: str) -> str:
    '''
    Ranker function that ranks the password based on the assigned criteria

    Input: pwd -> character or string

    The following are the requirements for POOR / MODERATE / STRONG password.

    Passwords can contain (not required) any of the following requirements:  
    i. Lower case letters (a – z).       iii) Numbers ( 0 – 9 ).  
    ii. Upper case letters (A – Z).      iv) Symbols ( ! + - = ? # % * @ & ^ $ _ )

    1. A POOR Password is defined as: 
    a. Contains less than 3 from the above 4 items ( i – iv ).  
    b. Less than 8 characters in length.

    2. A MODERATE Password is defined as:  
    a. Contains 3 from the above 4 items ( i – iv )  
    b. Between 8 to 10 characters in length.

    3. A STRONG Password is defined as:  
    a. Meets all 4 of the above items ( i – iv )  
    b. Greater than 10 characters in length.

    Returns: rank -> rank of password; POOR / MODERATE / STRONG
    '''
    ## Start code here

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

   ## End code here
    
   

def option1():
    '''
    Helper function that will be executed when user selects option 1 in the initial case.
    '''
    # Steps to follow:
    # 1. Ask user to rank password from either Users-Pwds.txt or a custom file (second part for bonus only you can skip this)
    # 2. Open the file containing username and password in each line and a file to store the ranked password information(Users-Pwds-Chked.txt).
    # 2.1 ## !IMPORTANT ## Store the list of username,passwords in a variable called usrpwds. 
    # 3. Use the rank() function to rank the password
    # 4. Write to the Users-Pwds-Chked.txt file (username,password,rank) in each line as string. Omit the brackets and only fill up the actual values. 
    # 5. Close necessary files and print to terminal.
    
    ## START CODE HERE"
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


    ## END CODE HERE

    print('#'*80)
    # [INFO] Be sure to change userpwds with the name of variable that you give to the list of passwords
    print('[INFO] '+'Number of passwords checked:',str(len(check_password))) 
    print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
    print('#'*80)

def option2():
    '''
    Function to be executed when the user selects option 2 (generate password) in the main loop.
    
    Steps to follow:
        Prompt the user for a username (No more the 20 characters in length).
        Create a Function that will have no (zero) arguments. (generate)
        The Function will randomly generate a STRONG password (Meeting the STRONG Requirments).
        Ask the user if they would like this saved (Y or N).
        If Y: Open the Input file (Users-Pwds.txt) and append the username,password to the EOF.
        If N: Ask if they would like to generate a different password for this user (Y or N).
        Then the program loops back to the menu again offering displaying and offering to select 1, 2 or 3.
    '''

    def generate() -> str:
        '''
        Helper function to generate password.
        Returns: A string pwd with strong ranking in our ranking system.
        '''
        # Starter code, Ualphabets contains all upper case alphabets
        # Lalphabets condains all lowercase alphabets
        # chars contains all special characters and digits contains all numeric digits
        Ualphabets = string.ascii_uppercase
        Lalphabets = string.ascii_lowercase
        chars = string.punctuation
        digits = string.digits

        # Hint: user random.choice to select a random Upperalphabet(Ualphabet), Lalphabet, chars, and digits. Join then all together in pwd and check ranking
        # While the required ranking is not met continue joining new Ualphabet, Lalphabet, chars and digits.
        
        ## START CODE HERE

        random_ualpha =''.join(random.sample(Ualphabets, 5 ))
        random_lalpha = ''.join(random.sample(Lalphabets, 5))
        random_char =''.join(random.sample(chars, 5))
        random_digits = ''.join(random.sample(digits, 5))

        pwd = random_ualpha + random_lalpha + random_char + random_digits
        
        ## END CODE HERE
        
        return pwd
    
    # Ask for username and check 20 character limits

    ## START CODE HERE

    ## END CODE HERE

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
        
        # try converting the inp to integer form and then check condition if input was either option1, 2, 3 or something else. 
        # exit the loop by using the break command if the user selects 3 other wise use option1() and option 2() function 

        ## START CODE HERE
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
        ## END CODE HERE


#DONOT TOUCH THESE LINES

if __name__=='__main__':
   main()
   
