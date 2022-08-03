
#โปรแกรม Log in ที่อ่านข้อมูลจาก *.ini มาเป็น dictionary

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Program Login")
root.resizable(0,0)
screen_height = root.winfo_screenwidth()
screen_width = root.winfo_screenheight()
root_height = 100
root_width = 300
root_x_cordinate = int((screen_height/2) - (root_width/2))
root_y_cordinate = int((screen_width/2) - (root_height/2))
root.geometry("{}x{}+{}+{}".format(root_width, root_height, root_x_cordinate, root_y_cordinate)) #Place the window on center of the screen 1#

#root.geometry("500x500") #have to use this, if use "center" below
#root.eval("tk::PlaceWindow . center") #Place the window on center of the screen 2#
#root.state("zoomed") #Initialize a window as maximized#

def root_close():
    if messagebox.askokcancel("Close", "Do you want to close program?"):
        root.destroy()

file_user_config = open("C:\\Users\\thana\\PycharmProjects\\JustPython\\user_config.ini", "r")
user_dict = {}
for line in file_user_config:
    key, value = line.strip().split(",")
    user_dict[key.strip()] = value.strip()
total_user = len(user_dict)
file_user_config.close()

def check_user():
    user_data = user_input.get()
    pass_data = pass_input.get()
    count_user = 0
    for user,password in user_dict.items():
        if user_data == user:
            if pass_data == password:
                alert_window("Alert!!","Logged!!",50,200)
                break
            else:
                alert_window("Alert!!","Invalid password!!",50,200)
                break
        count_user += 1
        if count_user == total_user:
            alert_window("Alert!!","Invalid user name!!",50,200)

def alert_window(title,message,height,width):
    alert = Tk()
    alert.title(title)
    alert.attributes("-topmost", True)
    alert.resizable(False,False)
    alert_x_cordinate = int((screen_height / 2) - (width / 2))
    alert_y_cordinate = int((screen_width / 2) - (height / 2))
    alert.geometry("{}x{}+{}+{}".format(width, height, alert_x_cordinate, alert_y_cordinate))
    alert_message = Label(alert,text=message,font=50).pack()

user_label = Label(root,text="User name : ",font=50).grid(row=0,column=0)
user_input = Entry(root)
user_input.grid(row=0,column=1)

pass_label = Label(root,text="Password : ",font=50).grid(row=1,column=0)
pass_input = Entry(root)
pass_input.grid(row=1,column=1)

ok_button = Button(root,text="Log in",font=500,command=check_user).grid(row=2,column=1)


root.protocol("WM_DELETE_WINDOW", root_close)
root.mainloop()
