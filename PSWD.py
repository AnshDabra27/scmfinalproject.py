import random
import array
import re
import string

# required length of password needed

    
# the display of the portals to sign-up
def portal_list():
     
     print("Site Examples :-")
     port_list1=["Google","Facebook","Ubisoft"] 
     # the examples of the sites we can create
     
     port_list2=["Github","Rockstar","Microsoft"]
     # our username and password
     
     port_list3=["Amazon","LinkedIn","Twitter"]
     # we can any another site we prefer or like
     
     for x in port_list1:
          print(x,end="    ")
     print() # thr for loop is used to print the examples in different lines
     
     for x in port_list2:
          print(x,end="    ")
     print()
     
     for x in port_list3:
          print(x,end="    ")
     print()

# the function is to check whether the password met all the conditions or not ?
# the verification is done by the already present function called (RE) Reading expressions


# Code starts here
print("                              Welcome to the Sign-up Portal")

# to start the code take  input of s 
Start_Input= input(' Press "S" to start ')

num = 1 

#when you had taken input
if Start_Input == "S" or Start_Input == "s":
    portal_list() # the list of sites that can be opened will be displayed by this function 
    #the input of the site name
    PORTAL= str(input("Please enter the site name :"))
    # PORTAL.capitalize()
    print("                         WELCOME TO ",PORTAL.upper())

    name_input= input("Please enter the name :") 
    # the users name will be input
    print("Hi,",name_input.capitalize()) 
    # the greetings will be provided to the users
    username_input= input("Create your username :")
    # desired username to be input
    print("Password must contain UPPERCASE,lowercase letter, special symbol and numeric value")
    # instuction for the required password

else:
    print("Thankyou for visiting ")
    # if you dont want to signup in it
