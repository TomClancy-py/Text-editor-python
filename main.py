print("Function:")
print()
print("\t'a' for adding the text or continuing what you were writing\n\t'w' for overwriting everything (evrything will be deleted if you overwrite)\n\t'x' for creting a new file")

user_input = input("enter the fuction:  ")


if (user_input == 'x'):
    print("\tNote:\n\t\tPlease enter the file name with its extension")
    file_name = input("enter the file name: ")
    file = open(file_name,"x")
    print(file_name+ " is created\n")
    print("do you wnat to edit it now?")
    edit = input("enter y/n:       ")
    if(edit == "y"):
        print("\nFunction:")
        print("\t'a' for adding the text or continuing what you were writing\n\t'w' for overwriting everything (evrything will be deleted if you overwrite)")
        user_input = input("enter the fuction:  ")
        if user_input in ("a","w"):
            print("now you can type anything and when you done press 'enter' on the keyboard\n\n")
        
            user_data = input()
            
            if(user_input == 'a'):
                file = open(file_name,"a")
                file.write(user_data + ". ")
                print("your data is stored in the 'file.txt' file\n")
        
            elif(user_input == "w"):
                file = open(file_name,"w")
                file.write(user_data+". ")
                print("overwited your data")
        
        else:
            print("nothing is changed")
        

elif user_input in ("a","w"):
    print("now you can type anything and when you done press 'enter' on the keyboard\n\n")

    user_data = input()
    
    if(user_input == 'a'):
        file = open("file.txt","a")
        file.write(user_data + ". ")
        print("your data is stored in the 'file.txt' file\n")

    elif(user_input == "w"):
        file = open("file.txt","w")
        file.write(user_data+". ")
        print("overwited your data")

else:
    print("nothing is changed")
