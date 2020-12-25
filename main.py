print("Function:")
print()
print("\t'a' for adding the text or continuing what you were writing\n\t'w' for overwriting everything (evrything will be deleted if you overwrite)\n\t'x' for creting a new file")

user_input = input("enter the fuction:  ")


if (user_input == 'x'):
    print("\tNote:\n\t\tPlease enter the file name with its extension")
    file_name = input("enter the file name: ")
    file = open(file_name,"x")
    print(file_name+ " is created\n")
    print("do you want to edit it now?")
    edit = input("enter y/n:       ")
    if(edit == "y"):
        print("\nFunction:")
        print("\t'a' for adding the text or continuing what you were writing\n\t'w' for overwriting everything (evrything will be deleted if you overwrite)")
        user_input = input("enter the fuction:  ")
        if user_input in ("a","w"):
            print("now you can type anything and when you're done press 'enter' on the keyboard to finish\n\n")
        
            user_data = input()
            
            if(user_input == 'a'):
                file = open(file_name,"a")
                file.write(user_data + ". ")
                print("your data is stored in the "+file_name+ " file\n")
        
            elif(user_input == "w"):
                file = open(file_name,"w")
                file.write(user_data+". ")
                print("overwrited your data")
        
        else:
            print("nothing is changed")
        

elif user_input in ("a","w"):
    print("now you can type anything and when you done press 'enter' on the keyboard\n\n")

    user_data = input()
    file_name = input("Enter the file name:  ")

    if(user_input == 'a'):
        file = open(file_name,"a")
        file.write(user_data + ". ")
        print("your data is stored in the 'file.txt' file\n")

    elif(user_input == "w"):
        file = open(file_name,"w")
        file.write(user_data+". ")
        print("overwrited your data")

else:
    print("nothing is changed")
