print( "There are currently x number of participants")
print("There are currently y number of mentos.")

#IMPORT THE MODULE DIRECTLY WAY
import Constantt
# yo tala ko last lenthy xa 
# print( "There are currently" + str(Constantt.CURRENT_STUDENT_COUNT) + "number of participants" )
# print("There are currently" + str(Constantt.CURRENT_MENTOR_COUNT) + "number of mentos.")

#IMPORT VARIABLE FROM CONSTANTS...MULTIPLE LAI COMMA
from Constantt import CURRENT_MENOTOR_COUNT , CURRENT_MENTOR_COUNT
#FROM PAXI KO NAME BHAYO ANI IMPORT PAXI KO NAME OF THE CONSTANT 

# Printing using module 
print( "There are currently",str(Constantt.CURRENT_STUDENT_COUNT) , "number of participants" )


# Printing by directing import variable from module
print( "There are currently" + str(Constantt.CURRENT_STUDENT_COUNT) + "number of participants" )
print("There are currently" + str(Constantt.CURRENT_MENTOR_COUNT) + "number of mentos.")
