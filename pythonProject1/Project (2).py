
def main() : #runs the menu and splits the file
    file=open("info.txt", "r") #file with id, name and marks
    new_file=open("TotalMarks.txt","w") #file to write new data in
    file.readline()
    lists=[] #original list used for spliting file into parts
    ID=[]
    name=[]
    attendance=[]
    midterm_list=[]
    classwork_list=[]
    final_list=[]
    for line in file : #this loop assigns each list its proper inputs
        lists=line.split()
        ID.append(lists[0])
        name.append("%s %s" % (lists[1], lists[2]))
        attendance.append(lists[3])
        midterm_list.append(lists[4])
        classwork_list.append(lists[5])
        final_list.append(lists[6])
    menu()
    options=input("\nWhat would you like to do?\n>>> ")
    flag= False
    cond=""
    #The cond down below is for not restart the program if the program has terminated by wrong/invalid inputs
    while flag == False:
        if options=="1" :
            print("\noption has been called\n")
            cond=newfile(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
            flag=True
        elif options=="2" :
            print("\noption has been called\n")
            cond=specific(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
            flag = True
        elif options=="3" :
            print("\noption has been called\n")
            cond=adding(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
            flag = True
        elif options=="4" :
            print("\noption has been called\n")
            cond=removal(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
            flag = True
        elif options=="5" :
            print("\noption has been called\n")
            cond=modify(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
            flag = True
        elif options=="6" :
            print("\noption has been called\n")
            cond=data(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
            flag = True
        elif options=="7" :
            Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
            break
        else :
            print("\nERROR: WRONG INPUT, please enter a number between (1-6) or (7) to close the program.")
            options = input("What would you like to do?\n>>> ")

        if flag == True and cond!="Terminated":
            restart = input("\nDo you want to start the program again?\ny. Yes\nn. No\n>>> ").lower()
            if restart in ["y", "n"]:
                flag = False
            else:
                restart = menuCounter(restart)
                flag = False
            if restart == "y":
                menu()
                options = input("\nWhat would you like to do?\n>>> ")
            else:
                options = "7"


#step1
def newfile(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list) : #function to write a file with Name, ID, and the total mark
    if len(ID)>0:
        for i in range(len(ID)):
            total_marks = int(midterm_list[i]) + int(classwork_list[i]) + int(final_list[i])
            new_file.write("<%s> < %3s > < %2s >\n %s \n"
                           % (ID[i], name[i], str(total_marks), "-" * 30))
        print("New file generated")
    else:
        print("ERROR: THERE ARE NO STUDENTS IN THE CLASS")


#step 2
def specific(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list) : #function to show specific students data
    print("1. Attendances\n"
          "2. Midterms\n"
          "3. Classworks\n"
          "4. Finals")
    list_choice=input("Choose an option:\n>>> ")
    if list_choice=="1" :
        print("criteria:\n"
              " 1. <= \n"
              " 2. >=  ")
        criteria=input("Choose criteria:\n>>> ")
        while criteria!="1" and criteria!="2" :
            print("Wrong input")
            criteria=input("Choose criteria:\n>>> ")
        flag=True
        while flag==True :
            try :
                grade=int(input("Enter absences: \n>>> "))
                if criteria=="1" :
                    for i in range(0,len(ID)):
                        if int(attendance[i]) <= grade: #check the student who has the less than or equal abcenses
                            print("%s\n"
                                  "ID: %s\n"
                                  "Name: %s\n"
                                  "Absences: %s\n"
                                  "Midterm: %s\n"
                                  "Classwork: %s\n"
                                  "Final: %s\n"
                                  "%s"
                                  % ("-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i],
                                     final_list[i], "-" * 30))
                    flag=False
                else :
                    for i in range(0,len(ID)):
                        if int(attendance[i]) >= grade : #check the student who has the greater than or equal abcenses
                            print("%s\n"
                                  "ID: %s\n"
                                  "Name: %s\n"
                                  "Absences: %s\n"
                                  "Midterm: %s\n"
                                  "Classwork: %s\n"
                                  "Final: %s\n"
                                  "%s"
                                  % ("-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i],
                                     final_list[i], "-" * 30))
                    flag=False
            except :  #If the user enter invalid input
                print("int only")
    elif list_choice=="2" :
        print("criteria:\n"
              " 1. <= \n"
              " 2. >= ")
        criteria=input("Choose criteria: \n>>> ")
        while criteria!="1" and criteria!="2" :
            print("Wrong input")
            criteria=input("Choose criteria:\n>>> ")
        flag=True
        while flag==True :
            try :
                grade=int(input("Enter grade: \n>>> "))
                if criteria=="1" :
                    for i in range(0,len(ID)):
                        if int(midterm_list[i]) <= grade :  #check the student who has the less than or equal grade
                            print("%s\n"
                                  "ID: %s\n"
                                  "Name: %s\n"
                                  "Absences: %s\n"
                                  "Midterm: %s\n"
                                  "Classwork: %s\n"
                                  "Final: %s\n"
                                  "%s"
                                  % ("-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i],
                                     final_list[i], "-" * 30))

                    flag=False
                else :
                    for i in range(0,len(ID)):
                        if int(midterm_list[i]) >= grade :  #check the student who has the greater than or equal grade
                            print("%s\n"
                                  "ID: %s\n"
                                  "Name: %s\n"
                                  "Absences: %s\n"
                                  "Midterm: %s\n"
                                  "Classwork: %s\n"
                                  "Final: %s\n"
                                  "%s"
                                  % ("-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i],
                                     final_list[i], "-" * 30))
                    flag=False
            except : #If the user enter invalid input
                print("int only")
    elif list_choice=="3" :
        print("criteria:\n"
              " 1. <= \n"
              " 2. >=  ")
        criteria=input("Choose criteria: \n>>> ")
        while criteria!="1" and criteria!="2" :
            print("Wrong input")
            criteria=input("Choose criteria:\n>>> ")
        flag=True
        while flag==True :
            try :
                grade=int(input("Enter grade: \n>>> "))
                if criteria=="1" :
                    for i in range(0,len(ID)):
                        if int(classwork_list[i]) <= grade: #check the student who has the less than or equal grade
                            print("%s\n"
                                  "ID: %s\n"
                                  "Name: %s\n"
                                  "Absences: %s\n"
                                  "Midterm: %s\n"
                                  "Classwork: %s\n"
                                  "Final: %s\n"
                                  "%s"
                                  % ("-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i],
                                     final_list[i], "-" * 30))
                    flag=False
                else :
                    for i in range(0,len(ID)):
                        if int(classwork_list[i]) >= grade :  #check the student who has the greater than or equal grade
                            print("%s\n"
                                  "ID: %s\n"
                                  "Name: %s\n"
                                  "Absences: %s\n"
                                  "Midterm: %s\n"
                                  "Classwork: %s\n"
                                  "Final: %s\n"
                                  "%s"
                                  % ("-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i],
                                     final_list[i], "-" * 30))
                    flag=False
            except : #If the user enter invalid input
                print("int only")
    elif list_choice=="4" :
        print("criteria:\n 1. <= \n 2. >=  ")
        criteria=input("Choose criteria: \n>>> ")
        while criteria!="1" and criteria!="2" :
            print("Wrong input")
            criteria=input("Choose criteria:\n>>> ")
        flag=True
        while flag==True :
            try :
                grade=int(input("Enter grade: \n>>>"))
                if criteria=="1" :
                    for i in range(0,len(ID)):
                        if int(final_list[i]) <= grade: #check the student who has the less than or equal grade
                            print("%s\n"
                                  "ID: %s\n"
                                  "Name: %s\n"
                                  "Absences: %s\n"
                                  "Midterm: %s\n"
                                  "Classwork: %s\n"
                                  "Final: %s\n"
                                  "%s"
                                  % ("-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i],
                                     final_list[i], "-" * 30))

                    flag=False
                else :
                    for i in range(0,len(ID)):
                        if int(final_list[i]) >= grade :  #check the student who has the greater than or equal grade
                            print("%s\n"
                                  "ID: %s\n"
                                  "Name: %s\n"
                                  "Absences: %s\n"
                                  "Midterm: %s\n"
                                  "Classwork: %s\n"
                                  "Final: %s\n"
                                  "%s"
                                  % ("-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i],
                                     final_list[i], "-" * 30))

                    flag=False
            except :  #If the user enter invalid input
                print("int only")
    else :
        print("Exiting option")
        Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
        return "Terminated"


#step 3


def adding(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list) : #function to add a student to the record
    new_ID = input("Enter the student's ID number: ")
    flag = True
    while len(new_ID)!=9 or new_ID.isdigit()==False or new_ID in ID: #Check the validity and avaliblity
        new_ID= addIdCounter(new_ID)
        if new_ID=="End": #To end the program and terminated it if the user lost all his chances.
            flag = False
            Terminate(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
            return "Terminated"
        elif new_ID in ID: #Check if the ID is not already exists.
            new_ID= idValidity(new_ID, ID)
            if new_ID=="End":
                flag = False
                Terminate(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
                return "Terminated"
        else:
            flag=True

    if flag==True :
        new_name = (input("Enter the student's name: ").lower()).capitalize()  #Capitalize the first letter
        if new_name.isdigit()==True or new_name=="":
            new_name= addNameCounter(new_name)
            if new_name=="End":  #To end the program and terminated it if the user lost all his chances.
                flag = False
                Terminate(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
                return "Terminated"
            else:
                flag=True

    if flag == True:
        new_attendance = input("Enter the student's number of absences: ")
        if new_attendance.isdigit() == False:
            new_attendance = addAbsCounter(new_attendance)
            if new_attendance == "End": #To end the program and terminated it if the user lost all his chances.
                flag = False
                Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
                return "Terminated"
            else:
                flag = True

    if flag==True :
        new_midterm= input("Enter the student's midterm grade: ")
        if new_midterm>"35" or new_midterm.isdigit()==False:  #Check the validity
            new_midterm= addMidCounter(new_midterm)

            if new_midterm=="End": #To end the program and terminated it if the user lost all his chances.
                flag = False
                Terminate(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
                return "Terminated"
            else:
                flag= True

    if flag==True :
        new_classwork= input("Enter the student's classwork grade: ")
        if new_classwork.isdigit()==False or (new_classwork>"25"): #Check the validity
            new_midterm= addCWorkCounter(new_classwork)

            if new_classwork=="End":#To end the program and terminated it if the user lost all his chances.
                flag = False
                Terminate(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
                return "Terminated"
            else:
                flag= True

    if flag==True :
        new_final= input("Enter the student's final grade: ")
        if new_final.isdigit()==False or (new_final>"40"):  #Check the validity
            new_midterm= addFinalCounter(new_midterm)
            if new_final=="End":
                flag = False
                Terminate(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
                return "Terminated"
            else:
                flag= True

    if flag==True:  #Adding to the class (list).
        ID.append(new_ID)
        name.append(new_name)
        attendance.append(new_attendance)
        midterm_list.append(new_midterm)
        classwork_list.append(new_classwork)
        final_list.append(new_final)
        print("%s\n"
              "| Please run the program again and choose option 1 |"
              "\n%s"% ("-"*52, "-"*52))


#step 4
def removal(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list) : #function to remove a student's record
    flag=True
    print("Remove students based on his.....\n"
          "1. ID \n"
          "2. NAME")
    choice=input("Choose an option: \n>>> ")
    if choice not in ["1", "2"] :
        choice= removalCounter(choice) #Check the validity
        if choice=="End":  #To end the program and terminated it if the user lost all his chances.
            flag = False
            Terminate(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
            return "Terminated"
        else:
            flag=True
    if choice=="1" and flag==True:
        choice_ID=input("Enter the student's ID number: ")
        choice_ID = wrongData(choice_ID)  # checking the validity and the availability
        if choice_ID == "End":  #To end the program and terminated it if the user lost all his chances.
            Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
            return "Terminated"
        else:
            choice_ID = dataChecker(choice_ID, ID)
        i=0
        while i in range(len(ID)) and flag==True:
            if choice_ID==ID[i] :
                print("%s\n"
                      "ID: %s\n"
                      "Name: %s\n"
                      "Absences: %s\n"
                      "Midterm: %s\n"
                      "Classwork: %s\n"
                      "Final: %s\n"
                      "%s"
                      % ("-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i], final_list[i], "-" * 30))
                confirmation=input("Enter ( q ) if you want to remove the student\nor press any key to cancel."
                                   "\n>>>").lower()
                flag = False
                if confirmation=="q" :  #If user choose q
                    ID.pop(i)           #Remove the data from the list
                    name.pop(i)
                    attendance.pop(i)
                    midterm_list.pop(i)
                    classwork_list.pop(i)
                    final_list.pop(i)
                    print("Student data has been deleted")
                    print("%s\n"
                          "| Please run the program again and choose option 1 |"
                          "\n%s" % ("-" * 52, "-" * 52))

                else:   #Cancel
                    print("CANCELED!")
                    Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
                    return "Terminated"
            else :
                  flag=True
            i+=1
    elif choice=="2" :  #By name
        choice_name= (input("Enter the student's name: ").lower()).capitalize()  #Capitalize the first letter
        if choice_name.isdigit()==True or choice_name=="":
            choice_name= addNameCounter(choice_name)  #Check the validity
            if choice_name=="End":  #To end the program and terminated it if the user lost all his chances.
                flag = False
                Terminate(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
                return "Terminated"
            else:
                pass
        i=0
        for i in range(len(ID)):
            if choice_name==name[i] :
                print("%s\n"
                      "ID: %s\n"
                      "Name: %s\n"
                      "Absences: %s\n"
                      "Midterm: %s\n"
                      "Classwork: %s\n"
                      "Final: %s\n"
                      "%s"
                      % ("-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i], final_list[i], "-" * 30))

                confirmation=input("Enter ( q ) if you want to remove the student\n"
                                   "Enter ( s ) to search for another student with the same name\n"
                                   "or press any key to cancel and close the program"
                                   "\n>>> ").lower()
                if confirmation=="q" :
                    ID.pop(i)        #Remove the data
                    name.pop(i)
                    attendance.pop(i)
                    midterm_list.pop(i)
                    classwork_list.pop(i)
                    final_list.pop(i)
                    print("Student data has been deleted\n")
                    print("%s\n"
                          "| Please run the program again and choose option 1 |"
                          "\n%s" % ("-" * 52, "-" * 52))
                    break
                elif confirmation=="s" : #To search for another student
                    continue  #Will terminate the program if there is no more student with the same name
                else:
                    Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
                    return "Terminated"

            i+=1
        else:
            print("There is no / no more students with this name")
            Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
            return "Terminated"


# step 5
def modify(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list) : #function to edit and modify student data
    flag=True
    i=0
    choice_ID=input("Enter the student's ID number: ")
    choice_ID = wrongData(choice_ID)  # checking the validity and the availability

    if choice_ID == "End": #To end the program and terminated it if the user lost all his chances.
        Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
        return "Terminated"
    else:
        choice_ID = dataChecker(choice_ID, ID) #Check if the ID is already exist.

    while i in range(0, len(ID)) and flag == True: #To find the student
        if choice_ID==ID[i] :
            print("%s\n"
                  "ID: %s\n"
                  "Name: %s\n"
                  "Absences: %s\n"
                  "Midterm: %s\n"
                  "Classwork: %s\n"
                  "Final: %s\n"
                  "%s"
                  % (
                  "-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i], final_list[i], "-" * 30))

            print("A. ID\nB. Name\nC. Attendance\nd. Midterm\ne. Classwork\nf. Final")  #Choices
            Choice_list=input("Choose an option: \n>>> ").lower()


            if Choice_list not in ["a", "b", "c", "d", "e", "f"]: #Check if the user enter wrong choice.
                Choice_list= modifyCounter(Choice_list)
                if Choice_list=="End":
                    flag = False
                    Terminate(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)
                    return "Terminated"
                else:
                    flag=False


            if Choice_list=="a":
                choice_ID=input("Enter the student's ID number: ")

                #These lines below is to chack the validity and avaliblity
                while len(choice_ID) != 9 or choice_ID.isdigit() == False or choice_ID in ID:
                    choice_ID = addIdCounter(choice_ID)
                    if choice_ID == "End":
                        flag = False
                        Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
                        return "Terminated"

                    elif choice_ID in ID:
                        choice_ID = idValidity(choice_ID, ID)
                        if choice_ID == "End":
                            flag = False
                            Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
                            return "Terminated"

                ID[i]=choice_ID  #Change the ID
                print("Modified")
                print("%s\n"
                      "| Please run the program again and choose option 1 |"
                      "\n%s" % ("-" * 52, "-" * 52))
                flag=False

            elif Choice_list=="b" :
                flag=True
                choice_name = (input("Enter the student's name: ").lower()).capitalize() #To capitalize the first letter
                while flag==True:
                    choice_name = addNameCounter(choice_name) #check the validity
                    if choice_name == "End":  #To end the program and terminated it if the user lost all his chances.
                        flag = False
                        Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
                        return "Terminated"
                    else:
                        flag=False
                else:
                    name[i]=choice_name #Change the name
                    print("Modified")
                    print("%s\n"
                        "| Please run the program again and choose option 1 |"
                        "\n%s" % ("-" * 52, "-" * 52))
                flag=False

            elif Choice_list=="c" :
                flag=True
                choice_attendance = input("Enter the student's number of absences: ")
                while flag==True:
                    choice_attendance = addAbsCounter(choice_attendance)  #Check the validity
                    flag = False
                    if choice_attendance == "End":  #To end the program and terminated it if the user lost all his chances.
                        Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
                        return "Terminated"
                    else:
                        flag=False
                else:
                    attendance[i]=choice_attendance #change the abcenses
                    print("Modified")
                    print("%s\n"
                          "| Please run the program again and choose option 1 |"
                          "\n%s" % ("-" * 52, "-" * 52))
                flag=False

            elif Choice_list=="d" :
                flag = True
                choice_midterm = input("Enter the student's midterm grade: ")
                while flag==True:
                    choice_midterm = addMidCounter(choice_midterm)  #Check the validity
                    flag = False
                    if choice_midterm == "End": #To end the program and terminated it if the user lost all his chances.
                        Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
                        return "Terminated"
                    else:
                        flag=False
                else:
                    midterm_list[i] = choice_midterm  #Change the midterm grade
                    print("Modified")
                    print("%s\n"
                          "| Please run the program again and choose option 1 |"
                          "\n%s" % ("-" * 52, "-" * 52))
                flag = False

            elif Choice_list=="e" :
                flag = True
                choice_classwork = input("Enter the student's classwork grade: ")
                while flag==True:
                    choice_classwork = addCWorkCounter(choice_classwork) #Check the validity
                    flag = False
                    if choice_classwork == "End":  #To end the program and terminated it if the user lost all his chances.
                        Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
                        return "Terminated"
                    else:
                        flag=False
                else:
                    classwork_list[i] = choice_classwork  #change the classwork grade
                    print("Modified")
                    print("%s\n"
                          "| Please run the program again and choose option 1 |"
                          "\n%s" % ("-" * 52, "-" * 52))
                flag = False

            elif Choice_list=="f" :
                flag = True
                choice_final = input("Enter the student's final grade: ")
                while flag==True:
                    choice_final = addFinalCounter(choice_final) #Check the validity
                    if choice_final == "End":  #To end the program and terminated it if the user lost all his chances.
                        Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
                        return "Terminated"
                    else:
                        flag=False
                else:
                    final_list[i] = choice_final #Change the final grade
                    print("Modified")
                    print("%s\n"
                          "| Please run the program again and choose option 1 |"
                          "\n%s" % ("-" * 52, "-" * 52))
                flag = False
        else :
            i+=1


#step 6
def data(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list)  : #shows students record and info.
    show_data = input("Enter ID: ")
    show_data = wrongData(show_data) #checking the validity and the availability

    if show_data=="End":    #To end the program and terminated it if the user lost all his chances.
        Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
        return "Terminated"
    else:
        show_data = dataChecker(show_data, ID) #Check if the ID is not already exist
        if show_data=="End":  #To end the program and terminated it if the user lost all his chances.
            Terminate(new_file, file, ID, name, attendance, midterm_list, classwork_list, final_list)
            return "Terminated"
        else:
            for i in range(0, len(ID)):
                if show_data == ID[i]:
                    print("%s\n"
                          "ID: %s\n"
                          "Name: %s\n"
                          "Absences: %s\n"
                          "Midterm: %s\n"
                          "Classwork: %s\n"
                          "Final: %s\n"
                          "%s"
                          % (
                          "-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i], final_list[i], "-" * 30))


#step 7
def menu() :  #To display the menu of choices for user to choose.
    print("1.Generate a new file that has Name, ID, and the total mark "
          "\n2.Show students that meet a specific criteria "
          "\n3.Add a Student to the class "
          "\n4.Remove a student from the class "
          "\n5.Modify student's information "
          "\n6.Show the data of a student "
          "\n7.Terminate program"
          "\nChoose an option between 1-7")


def Terminate(new_file,file,ID,name,attendance,midterm_list,classwork_list,final_list) : #function to stop the program
    print("Program terminated")
    new_file.close()
    file.close()
    print("\nPrinting the list: \n")
    for i in range(0,len(ID)):  #Print the information of all the students in the class.
        print("%s\n"
                          "ID: %s\n"
                          "Name: %s\n"
                          "Absences: %s\n"
                          "Midterm: %s\n"
                          "Classwork: %s\n"
                          "Final: %s\n"
                          "%s"
                          % (
                          "-" * 30, ID[i], name[i], attendance[i], midterm_list[i], classwork_list[i], final_list[i], "-" * 30))



#Counters and Checkers
###### NOTE: Most of the counters and checkers are the same the difference is the ERROR message
############ which will raise or the condition.

#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Counter for restart the program. It will terminate the program if the user enter 10 invalid input.

def menuCounter(restart):
    count=10
    while restart not in ["y", "n"]:
        count-=1

        if count>1:
            print("\nERROR:WRONG INPUT, try again.")
            print("(%d chances left!)\n"% count)
        elif count==1:
            print("\nERROR:WRONG INPUT, try again.")
            print("(Last chance!)\n")
        else:
            print("\nYour chances has finished!")
            restart="n"
            break
        restart = input("\nDo you want to start the program again?\ny. Yes\nn. No\n>>> ").lower()

    return restart
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Function to check if the ID is in the class and give the user 3 chances only.

def dataChecker (data, ID):
    count=4

    while data not in ID: #Counter
        count -= 1
        print("\nERROR: ID NOT FOUND, try again.")
        if count > 1:
            print("(you have %d chances)" % count)
        elif count == 1:
            print("(Last chance!)")
        else:
            print("\nYour chances has finished!")
            data= "End"
            break
        data = input("\nEnter ID: ")
    return data
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Function to check if the ID is valid and give the user 10 chances.

def wrongData(data):
    count=10
    while len(data)!=9 or data.isdigit()==False:
        count-=1
        print("\nERROR: INVALID INPUT, ID should be 9 digits.")
        if count>1:
            print("(%d chances left!)\n"% count)
        elif count==1:
            print("(Last chance!)\n")
        else:
            print("\nYour chances has finished!")
            return "End"
        data = input("\nEnter the student's ID number: ")
    return data
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Function to check if the ID is valid but for adding (Step#3)

def addIdCounter(new_ID):
    count = 10
    while len(new_ID) != 9 or new_ID.isdigit()==False:
        count -= 1

        if count > 1:
            print("\nERROR: INVALID INPUT. ID number should be 9 numbers.")
            print("(%d chances left!)\n" % count)
        elif count == 1:
            print("\nERROR: INVALID INPUT. ID number should be 9 numbers.")
            print("(Last chance!)\n")
        else:
            print("\nYour chances has finished!")
            new_ID= "End"
            break
        new_ID = input("Enter the student's ID number: ")

    return new_ID
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Function to check if the name is valid and real, and give the user 10 chances.

def addNameCounter(new_name):
    count = 10
    while new_name=="" or new_name.isdigit()==True:
        count -= 1
        if count > 1:
            print("\nERROR: INVALID INPUT. Enter a valid name.")
            print("(%d chances left!)\n" % count)
        elif count == 1:
            print("\nERROR: INVALID INPUT. Enter a valid name.")
            print("(Last chance!)\n")
        else:
            print("\nYour chances has finished!")
            new_name= "End"
            break
        new_name = (input("Enter the student's name: ").lower()).capitalize()

    return new_name
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Function to check if the absences are numbers, and give the user 10 chances.

def addAbsCounter(new_attendance):
    count = 10
    while new_attendance.isdigit()==False:
        count -= 1
        if count > 1:
            print("\nERROR: INVALID INPUT. Enter an integer number.")
            print("(%d chances left!)\n" % count)
        elif count == 1:
            print("\nERROR: INVALID INPUT. Enter an integer number.")
            print("(Last chance!)\n")
        else:
            print("\nYour chances has finished!")
            new_attendance= "End"
            break
        new_attendance = input("Enter the student's number of absences: ")

    return new_attendance
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Function to check if the midterm grades are valid and in the range, and give the user 10 chances.

def addMidCounter(new_midterm):
    count = 10
    while new_midterm.isdigit()==False or (new_midterm>"35"):
        count -= 1
        if count > 1:
            print("\nERROR: INVALID INPUT. Maximum midterm grade is 35.")
            print("(%d chances left!)\n" % count)
        elif count == 1:
            print("\nERROR: INVALID INPUT. Maximum midterm grade is 35.")
            print("(Last chance!)\n")
        else:
            print("\nYour chances has finished!")
            new_midterm= "End"
            break
        new_midterm = input("Enter the student's midterm grade: ")

    return new_midterm
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Function to check if the classwork grades are valid and in the range, and give the user 10 chances.

def addCWorkCounter(new_classwork):
    count = 10
    while new_classwork.isdigit()==False or (new_classwork>"25"):
        count -= 1
        if count > 1:
            print("\nERROR: INVALID INPUT. Maximum midterm grade is 25.")
            print("(%d chances left!)\n" % count)
        elif count == 1:
            print("\nERROR: INVALID INPUT. Maximum midterm grade is 25.")
            print("(Last chance!)\n")
        else:
            print("\nYour chances has finished!")
            new_classwork= "End"
            break
        new_classwork = input("Enter the student's classwork grade: ")

    return new_classwork
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Function to check if the final grades are valid and in the range, and give the user 10 chances.

def addFinalCounter(new_final):
    count = 10
    while new_final.isdigit()==False or (new_final>"40"):
        count -= 1
        if count > 1:
            print("\nERROR: INVALID INPUT. Maximum midterm grade is 40.")
            print("(%d chances left!)\n" % count)
        elif count == 1:
            print("\nERROR: INVALID INPUT. Maximum midterm grade is 40.")
            print("(Last chance!)\n")
        else:
            print("\nYour chances has finished!")
            new_final= "End"
            break
        new_final = input("Enter the student's final grade: ")

    return new_final
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Function to check the options for remove option, and give the user 10 chances.

def removalCounter(choice):
    count = 10
    while choice not in ["1", "2"]:
        count -= 1
        if count > 1:
            print("\nERROR: WRONG INPUT. Only (1) and (2) are acceptable.")
            print("(%d chances left!)\n" % count)
        elif count == 1:
            print("\nERROR: WRONG INPUT. Only (1) and (2) are acceptable.")
            print("(Last chance!)\n")
        else:
            print("\nYour chances has finished!")
            choice= "End"
            break
        choice = input("Choose an option: \n>>> ")

    return choice
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Function to check the options for modify option, and give the user 10 chances.

def modifyCounter(choice_list):
    count = 10
    while choice_list not in ["a", "b", "c", "d", "e", "f"]:
        count -= 1
        if count > 1:
            print("\nERROR: WRONG INPUT. Enter a valid letter.")
            print("(%d chances left!)\n" % count)
        elif count == 1:
            print("\nWRONG INPUT. Enter a valid letter.")
            print("(Last chance!)\n")
        else:
            print("\nYour chances has finished!")
            choice_list= "End"
            break
        choice_list = input("Choose an option: \n>>> ")

    return choice_list
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#Function to check if the ID are already exist in the class, and give the user 10 chances.

def idValidity (new_ID, ID):
    count = 10
    while new_ID in ID:
        count -= 1
        if count > 1:
            print("\nERROR: INVALID INPUT. ID number is already exist (duplicated)")
            print("(%d chances left!)\n" % count)
        elif count == 1:
            print("\nERROR: INVALID INPUT. ID number is already exist (duplicated)")
            print("(Last chance!)\n")
        else:
            print("\nYour chances has finished!")
            new_ID = "End"
            break
        new_ID = input("Enter the student's ID number: ")

    return new_ID
#--------------------------------------------------------------#
#--------------------------------------------------------------#

main()

