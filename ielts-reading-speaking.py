
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

loginForm = Tk()
loginForm.title('IELTS Band Score')
loginForm.geometry('400x300')
right = int(loginForm.winfo_screenwidth() / 2 - 400 / 2)
down = int(loginForm.winfo_screenheight() / 2 - 200 / 2)
loginForm.geometry('+{}+{}'.format(right, down))
loginForm.resizable(0,0)

def validate_input(new_value):
    if new_value.isdigit() or new_value == "":
        return True
    else:
        loginForm.bell()
        msg.showinfo(':)', "Please enter a valid integer.")
        return False



def ielts_calculator():
    s = txtNumber1.get()

    if s<4:
        msg.showinfo(':)', "number of Listening must be between 4 and 40.")
        return
    elif s>=4 and s<=5:
        sp=2.5
    elif s>=6 and s<=7:
        sp=3
    elif s>=8 and s<=10:
        sp = 3.5
    elif s>=10 and s<=12:
        sp = 4
    elif s>=13 and s<=15:
        sp = 4.5
    elif s>=16 and s<=17:
        sp=5
    elif s>=18 and s<=22:
        sp=5.5
    elif s>=23 and s<=25:
        sp=6
    elif s>=26 and s<=29:
        sp=6.5
    elif s>=30 and s<=31:
        sp=7
    elif s>=32 and s<=34:
        sp=7.5
    elif s>=35 and s<=36:
        sp=8
    elif s>=37 and s<=38:
        sp=8.5
    elif s>=39 and s<=40:
        sp=9
    elif s>40:
        msg.showinfo(':)', "number of Listening must be between 4 and 40.")
        return

    selected_value = radio_var.get()

    l = txtNumber2.get()
    if selected_value == 1:
        if l < 6:
            msg.showinfo(':)', "number of Reading must be between 6 and 40.")
            return
        elif l >= 6 and l <= 8:
            lp=2.5
        elif l >= 9 and l <= 11:
            lp=3
        elif l >= 12 and l <= 14:
            lp=3.5
        elif l==15:
            lp=4
        elif l >= 16 and l <= 22:
            lp=4.5
        elif l==23:
            lp=5
        elif l >= 22 and l <= 29:
            lp=5.5
        elif l==30:
            lp=6
        elif l >= 31 and l <= 33:
            lp=6.5
        elif l==34:
            lp=7
        elif l >= 35 and l <= 37:
            lp=7.5
        elif l==38:
            lp=8
        elif l==39:
            lp=8.5
        elif l==40:
            lp=9
        elif l > 40:
            msg.showinfo(':)', "number of Reading must be between 4 and 40.")
            return


    elif selected_value == 2:
        if l < 4:
            msg.showinfo(':)', "number of Reading must be between 6 and 40.")
            return
        elif l >= 4 and l <= 5:
            lp = 2.5
        elif l >= 6 and l <= 7:
            lp = 3
        elif l >= 8 and l <= 9:
            lp = 3.5
        elif l >= 10 and l <= 12:
            lp = 4
        elif l >= 13 and l <= 14:
            lp = 4.5
        elif l == 15:
            lp = 5
        elif l >= 16 and l <= 22:
            lp = 5.5
        elif l == 23:
            lp = 6
        elif l >= 24 and l <= 29:
            lp = 6.5
        elif l == 30:
            lp = 7
        elif l >= 31 and l <= 34:
            lp = 7.5
        elif l == 35:
            lp = 8
        elif l >= 36 and l <= 38:
            lp = 8.5
        elif l >= 39 and l <= 40:
            lp = 9
        elif l > 40:
            msg.showinfo(':)', "number of Reading must be between 4 and 40.")
            return

    msg.showinfo(':)', f"Your listening score is {sp} and Reading score is {lp}")



lblNumber1=Label(loginForm,text='Num listening:')
lblNumber1.grid(row=0,column=0,padx=10,pady=10)

txtNumber1=IntVar(value="")
validate_cmd = loginForm.register(validate_input)
entNumber1 = Entry(loginForm, width=20, textvariable=txtNumber1, validate="key", validatecommand=(validate_cmd, '%P'))
entNumber1.grid(row=0,column=1,padx=10,pady=10)

lblNumber2=Label(loginForm,text='Num Reading:')
lblNumber2.grid(row=1,column=0,padx=10,pady=10)

txtNumber2=IntVar(value="")
entNumber2=Entry(loginForm,width=20,textvariable=txtNumber2)
entNumber2.grid(row=1,column=1,padx=10,pady=10)

radio_var = IntVar()

check_button = ttk.Radiobutton(loginForm, text="General",variable=radio_var, value=1, command=ielts_calculator)
check_button.grid(row=2,column=0,padx=10,pady=10)

check_button = ttk.Radiobutton(loginForm, text="Academic",variable=radio_var, value=2, command=ielts_calculator)
check_button.grid(row=2,column=1,padx=10,pady=10)

btnlogin=ttk.Button(loginForm,text='+',width=10,command=ielts_calculator)
btnlogin.grid(row=3,column=1,padx=10,pady=10)



loginForm.mainloop()





