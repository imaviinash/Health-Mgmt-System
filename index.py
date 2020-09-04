'''client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
log_list = {1: "Exercise", 2: "Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Selaect Client Nmae")
    for key, value in client_list:
        print("Press", key, "for", value, "\n", end="")
        client_name = int(input())
        print("Selected Client:", client_list[client_name], "\n", end="")

        print("Press 1 for log")
        print("Press 2 for retrive")
        op = int(input())
        if op is 1:
            for key, value in log_list.items():
                print("Press", key, "to log", value, "\n", end="")
                log_name = int(input())
                print("Selected Job:", log_list[log_name], "\n", end="")

f = open(client_list[client_name]+""+ log_list[log_name]+ ".txt", "a")
k = "y"
while k is not "n":
    print("Enter", log_list[log_name], "\n", end="")
    mytext = input()
    f.write("["+str(getdate())+"]:", mytext)
    k = input("Add more y/n?")
    continue
    f.close()

if op is 2:
    for key, value in log_list.items():
        print("Press", key, "to retrive", value, "\n", end="")
        log_name = int(input())
        print(client_list[client_name], *_* log_list[log_name], "Report: \n", end="")

f = open(client_list[client_name]+""+ log_list[log_name]+ ".txt", "rt")
contents = f.readlines()
for f in contents:
    print(line, end="")
    f.close()
else:
    print("Inavlid Input")

except Exception as e:
print("Wrong Input")'''

'''def getdate():
    import datetime
    return datetime.datetime.now()


n = {1: "Harry", 2: "Rohan", 3: "Hammad"}
x = int(input("1 for Harry, 2 for Rohan, 3 for Hammad"))
y = input("Retrive or Read:")
z = input("Exercise or Food:")

def abc():
    if z=="Exercise":
        return "__e.txt"
    elif z=="Read":
        return "__r.txt"
    else:
        return "Inavalid Input"

    d=abc()
    with open("str(n[x]+d)", "r+") as f:
        if y=="Retrive":
            print(f.read())
            f.write("\n"+input("Put your new task:")+"Time:" + str(getdate()))
        else:
            print(f.read())'''

from datetime import datetime

print("1 for harry , 2 for rohan , 3 for nikhil")

person_select = int(input("choose person:"))

# Harry code
if (person_select == 1):
    add_see = int(input("1 for see the harry log and 2 for add log"))
    if (add_see == 1):
        option = int(input("1 for exercise and 2 for diet"))
        if (option == 1):
            try:
                _file = open("harryexercise.txt", "r")
                for line in _file.readlines():
                    print(line)
                _file.close()
            except:
                create_file = open("harryexercise.txt", "a+")
                print(create_file.readlines())
                create_file.close()

        if (option == 2):
            try:
                _file2 = open("harrydiet.txt", "r")
                for line in _file2.readlines():
                    print(line)
                _file2.close()
            except:
                create_file2 = open("harrydiet.txt", "a+")
                print(create_file2.readline())
                create_file2.close()

    if (add_see == 2):
        option2 = int(input("1 for exercise and 2 for diet"))

        if (option2 == 1):
            fileforwrite1 = open("harryexercise.txt", "a")
            content = input("Write the log:")
            contentinfile = "\n" + str(datetime.now()) + " " + content
            fileforwrite1.write(contentinfile)
            fileforwrite1.close()

        if (option2 == 2):
            fileforwrite1 = open("harrydiet.txt", "a")
            content = input("Write the log:")
            contentinfile = "\n" + str(datetime.now()) + " " + content
            fileforwrite1.write(contentinfile)
            fileforwrite1.close()

# Rohan code
if (person_select == 2):
    add_see = int(input("1 for see the rohan log and 2 for add log"))
    if (add_see == 1):
        option = int(input("1 for exercise and 2 for diet"))
        if (option == 1):
            try:
                _file = open("rohanexercise.txt", "r")
                for line in _file.readlines():
                    print(line)
                _file.close()
            except:
                create_file = open("rohanexercise.txt", "a+")
                print(create_file.readlines())
                create_file.close()

        if (option == 2):
            try:
                _file2 = open("rohandiet.txt", "r")
                for line in _file2.readlines():
                    print(line)
                _file2.close()
            except:
                create_file2 = open("rohandiet.txt", "a+")
                print(create_file2.readline())
                create_file2.close()

    if (add_see == 2):
        option2 = int(input("1 for exercise and 2 for diet"))

        if (option2 == 1):
            fileforwrite1 = open("rohanexercise.txt", "a")
            content = input("Write the log:")
            contentinfile = "\n" + str(datetime.now()) + " " + content
            fileforwrite1.write(contentinfile)
            fileforwrite1.close()

        if (option2 == 2):
            fileforwrite1 = open("rohandiet.txt", "a")
            content = input("Write the log:")
            contentinfile = "\n" + str(datetime.now()) + " " + content
            fileforwrite1.write(contentinfile)
            fileforwrite1.close()

# Nikhil code
if (person_select == 3):
    add_see = int(input("1 for see the Nikhil log and 2 for add log"))
    if (add_see == 1):
        option = int(input("1 for exercise and 2 for diet"))
        if (option == 1):
            try:
                _file = open("nikhilexercise.txt", "r")
                for line in _file.readlines():
                    print(line)
                _file.close()
            except:
                create_file = open("nikhilexercise.txt", "a+")
                print(create_file.readlines())
                create_file.close()

        if (option == 2):
            try:
                _file2 = open("nikhildiet.txt", "r")
                for line in _file2.readlines():
                    print(line)
                _file2.close()
            except:
                create_file2 = open("nikhildiet.txt", "a+")
                print(create_file2.readline())
                create_file2.close()

    if (add_see == 2):
        option2 = int(input("1 for exercise and 2 for diet"))

        if (option2 == 1):
            fileforwrite1 = open("nikhilexercise.txt", "a")
            content = input("Write the log:")
            contentinfile = "\n" + str(datetime.now()) + " " + content
            fileforwrite1.write(contentinfile)
            fileforwrite1.close()

        if (option2 == 2):
            fileforwrite1 = open("nikhildiet.txt", "a")
            content = input("Write the log:")
            contentinfile = "\n" + str(datetime.now()) + " " + content
            fileforwrite1.write(contentinfile)
            fileforwrite1.close()
