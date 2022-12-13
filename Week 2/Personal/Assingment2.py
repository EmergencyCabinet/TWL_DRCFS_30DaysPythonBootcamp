
text = open(r"C:\Users\acer\OneDrive\Desktop\Python\TWL_DRCFS_30DaysPythonBootcamp-1\Week 2\Personal\First.txt", "r")
con  = (text.readlines())
print(con)
text.close()


with open(r"C:\Users\acer\OneDrive\Desktop\Python\TWL_DRCFS_30DaysPythonBootcamp-1\Week 2\Personal\First.txt", "r") as file:
    cont = file.readlines()
    print(cont)
    

assign = open(r'C:\Users\acer\OneDrive\Desktop\Python\TWL_DRCFS_30DaysPythonBootcamp-1\Week 2\Personal\First.txt','r')
print(assign)
my_file = assign.read()
print(my_file)

assign.close()

