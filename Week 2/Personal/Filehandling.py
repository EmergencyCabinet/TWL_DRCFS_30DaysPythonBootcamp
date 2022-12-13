file = open("my_file.txt", 'w')

file.write('hello world'\n)
file.write('ke xa kta kt ho')

file.close()
 #w = write mode
 # a = append mode appends data aagdi print gareko ne rakhxa 
 # naya data matra thapnu xa bhane append 
 # write mode le agadi ko udaidinxa

username_pwd = open('passworrds.txt', 'r').read()
username_pwd =  username_pwd.split('\n')

for uname_pwd in username_pwd:
    username, passworrds = uname_pwd.split(',')

    print(f'The password of {username} is {password}')
 