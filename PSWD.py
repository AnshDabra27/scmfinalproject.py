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
    # if you dont want to signup in i
# required length of password needed
def PSWD(MAX_LEN):
          

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']
 
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']
 
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    # the minimum length required to produce code is 4 
    if MAX_LEN >= 4:
    # combines all the character arrays above to form one array
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
 
    # randomly select at least one character from each character set above
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
 
    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
 
 
    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of the password length by selecting randomly from the combined
    # list of character above.
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
 
        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
 
    # traverse the temporary password array and append the chars
    # to form the password
        password = ""
        for x in temp_pass_list:
                password = password + x
         
    # print out password
        print(password)
    
    #if the length of code is less than 4
    else:
        print('''The Minimum lenght of password should be 4 
                Please try again      ''')

#when you had taken input

    while num == 1:
        password_input= input("Create a strong Password :(To randomly generate password please type '1')")
        # generated password to be inputed
        while password_input == '1':
            # the condition if the user wants the random passwor
            MAX_LEN = int(input("Please Enter the Required Length of Password: "))
            PSWD(MAX_LEN)

            # this loop will create random password 
            pswd_confirmation = int(input("Confirm this password type '1', New reccomendation type '2', manually enter type '3'"))
        if (pswd_check(password_input) == False):
            num = 1
    
        else
            num = 0
  
    print("Your account has been created succesfully")
    # if the sign up is succesful with the required password
    print("Now you can signin in your",PORTAL.upper(),"using this login credentials")

# the function is to check whether the password met all the conditions or not ?
# the verification is done by the already present function called (RE) Reading expressions
def pswd_check(pswd):
   specharlist = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
   # the list is for
   #the special characters
   alphalist = re.compile('[a-z]')
   #this list is for
   # the lowercase letter
   Alphalist = re.compile('[A-Z]')
   #this list is for
   # the uppercase letter
   numlist = re.compile('[0-9]')
   # this list is for 
   # the numbers  

   # the if conditions further check that the 
   #provided output either have the required input value or not
   if(alphalist.search(pswd) == None):
        print("The password need at least one lowercase alphabet to proceed")
        return 0# if it doesn"t have the value it returns false
   else:
       pass

   if(Alphalist.search(pswd) == None):
        print("The password needs at least one uppercase letter to proceed")
        return 0 
   else:
       pass # else it goes onto the next condition

   if(numlist.search(pswd) == None):
       print("The password needs atleast one number to proceed")
       return 0
   else:
       pass

   if(specharlist.search(pswd) == None):
       print("The password needs atleast one special character to proceed")
       return 0  
   else:
       pass

   return 1 # if all the conditions are meant it returns true


            if pswd_confirmation == 1:# if the random generated password is confirmed
               print("Your account has been created succesfully")
               # if the sign up is succesful with the required password 
               print("Now you can signin in your",PORTAL.upper(),"using this login credentials")
               exit()
            if pswd_confirmation == 2:#if user want a new random generatewd password
               continue
            if pswd_confirmation == 3:# if they want to manually type the pasword
               num = 1
               break
        
