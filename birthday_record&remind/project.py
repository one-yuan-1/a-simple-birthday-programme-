# Import the time module to get the time (month and day), the json module handles the json file
import time
import datetime
import json
print("Today is:")
print(time.strftime("%m,%d", time.localtime()) )
month=time.strftime("%m", time.localtime())
day=time.strftime("%d", time.localtime())



#Open file (for storing birthdays)
file=open("birthday.json","a")
with open("birthday.json","r",encoding="UTF-8") as file_r:
    tem_datas=file_r.read()
dict_datas=json.loads(tem_datas)




# Define a function to add birthdays, read the original file content as a dictionary, add new elements to the dictionary, and finally overwrite the original file with the new dictionary. Finish adding birthdays
def add_bir():
    with open("birthday.json", "r",encoding="utf-8") as f:
        json_data = f.read()
    data = json.loads(json_data)

    tem_input1 = input("Whose birthday do you want to add?:")
    tem_input2=input("His or her birthday is:(month.day)(eg:6.01)")
    data[tem_input1]=float(tem_input2)

    with open('birthday.json', 'w',encoding="utf-8") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)



#Add a function to view birthdays
def check_birthday():

#open() function is used to open a json file, the read() method reads the file as a string, and the json.loads() function parses the string into a dictionary  
    with open("birthday.json", "r",encoding="utf-8") as f:
        json_data = f.read()
    data = json.loads(json_data)
#dictionary.keys() is used to get all key values
    keys = data.keys()
    #print(keys)

    for i in keys:
        name = i
        bir = data[i]
        print(f"name: {name}\nbirthday: {bir}")

#define a function to delete birthdays,which is similar to add birthdays
def delete():
    with open("birthday.json", "r",encoding="utf-8") as f:
        json_data = f.read()
    data = json.loads(json_data)
    input_del_who=input("whose birthday you'd like to delete?")
    data.pop(input_del_who)

    with open("birthday.json", "w",encoding="utf-8") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)

   

#Use for and if to check if the birthday is approaching and make a reminder
for i in dict_datas:
    value=dict_datas[i]
    month_plus_1=int(month)+1
    num=100
    if int(month) < float(value) < (float(month) + float(day) / num):
        print("This month you have a friend or relative's birthday that has passed")
    if (float(month) + float(day) / num) < float(value) <= int(month_plus_1):
        print("You have a friend or family's birthday coming up this month.")
    else:
        print("There are no birthdays of your friends and relatives this month")



#Main program
a=1
while a==1:
    print("Welcome to Birthday Recorder\n1.add birthday\n2.view birthday\n3.birthday remind(automatic)\n4.exit\n5.delete birthday")
    input_0=input()
    if input_0=="1":
        add_bir()
    elif input_0=="2":
        check_birthday()
    elif input_0=="3":
        print("The automatic birthday reminder has been turned on.")
    elif input_0=="4":
        break
    elif input_0=="5":
        delete()
    else:
        print("Please enter correctly.")









file.close()
