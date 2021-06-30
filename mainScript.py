#IMPORTING NECESSARY LIBRARIES
import tkinter
import random
import string
import smtplib
from datetime import datetime

# SETTING UP BASIC WINDOW OF TKINTER
root = tkinter.Tk()
root.geometry('300x470')
root.resizable(0,0)
root.title('PwD Generator')
titl = tkinter.Label(text = 'Password Generator', font = ('Arial',25)).grid(row = 1, column =0)


# APPLYING IMAGE
canv = tkinter.Canvas(height = 100,width = 100)
logo = tkinter.PhotoImage(file = 'l.png')
canv.create_image(50,50,image=logo)
canv.grid(row=0,column=0)

# NECESSARY VARIABLES FOR PASSWORD GENERATION
constraints = {'upper':False, 'integer':False, 'special':False}
passw = None
pwd = tkinter.StringVar()
root2  = None


# THE THREE FUNCTIONS BELOW ARE USED TO CONFIGURE THE VARIABLE CONSTRAINTS TO ALTER THE PASSWORD GENERATION FORMAT
def uppertoggle():
    global constraints
    if constraints['upper']==False:
        constraints['upper']=True
    elif constraints['upper']==True:
        constraints['upper']=False

def inttoggle():
    global constraints
    if constraints['integer']==False:
        constraints['integer']=True
    elif constraints['integer']==True:
        constraints['integer']=False

def specialtoggle():
    global constraints
    if constraints['special']==False:
        constraints['special']=True
    elif constraints['special']==True:
        constraints['special']=False



# THE MAIN PASSWORD GENERATION FUNCTION
def passGen(length,c):
    global passw
    global pwd
    passw = ''
    for i in range(length):
        a = random.randint(0,3)
        if a==0 and c['upper']==True:
            passw+=random.choice(string.ascii_uppercase)
        elif a==1 and c['integer']==True:
            passw+=random.choice(string.digits)
        elif a==3 and c['special']==True:
            passw+=random.choice(string.punctuation)
        else:
            passw+=random.choice(string.ascii_lowercase)
    pwd.set('*'*len(passw))
    

# FUNCTION TO CHECK PASSWORD STRENGHT
def makstrlab(passwd):
    def password_check(passwd):
           
        l = len(passwd)
        st = 100

        if l < 8 : 
            return 'Password Strength : WEAK'

        elif l >= 8 and l <= 16:
            if not any(char.isdigit() for char in passwd): 
                st -= 25
            if not any(char.isupper() for char in passwd):
                st -= 25
            if not any(char in string.punctuation for char in passwd):
                st -= 25

    
            if st>0 and st<=25:
                return 'Password Strength : WEAK'
            elif st>25 and st<=50:
                return 'Password Strength : FAIR'
            elif st>50 and st<=75:
                return 'Password Strength : GOOD'
            elif st>75 and st<=100:
                return 'Password Strength : STRONG'
    pstr = password_check(passwd)
    
    global strlab
    global root
    strlab.destroy()
    strlab = tkinter.Label(root,)
    strlab.grid(row = 11)
    if 'WEAK' in pstr:
        strlab.destroy()
        strlab = tkinter.Label(root, text = pstr,fg = 'Red',bg = 'Black')
        strlab.grid(row=11)
    elif 'FAIR' in pstr:
        strlab.destroy()
        strlab = tkinter.Label(root, text = pstr,fg = 'Yellow3',bg = 'Black')
        strlab.grid(row=11)
    elif "GOOD" in pstr:
        strlab.destroy()
        strlab = tkinter.Label(root, text = pstr,fg = 'Lawn Green',bg = 'Black')
        strlab.grid(row=11)
    else:
        strlab.destroy()
        strlab = tkinter.Label(root, text = pstr,fg = 'Green2',bg = 'Black')
        strlab.grid(row=11)


    
    



######################################################################################################################################################################
######################################################################################################################################################################
######################################################################################################################################################################
def mailgui(p):
    pword = p
       
    # CREATING NECESSARY VARIABLES
    global root2
    
    
    #DEFINING NECESSARY FUNCTIONS

    def send_email(user, pwd, recipient, subject, body):
                
        FROM = user
        TO = recipient if isinstance(recipient, list) else [recipient]
        SUBJECT = subject
        TEXT = body

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user, pwd)
            server.sendmail(FROM, TO, message)
            server.close()


            root3 = tkinter.Tk()
            root3.geometry('300x50')
            root3.resizable(0,0)
            root3.title('Confirmation')
            tkinter.Label(root3,text = 'Mail Sent Successfully').pack()
            con = tkinter.Button(root3,text = 'OK',bg = 'Light Blue', command = lambda: [root3.destroy(),root2.destroy()],font=('unispace',8,'bold')).pack()
            root3.mainloop()
        except:
            root4 = tkinter.Tk()
            root4.geometry('300x50')
            root4.resizable(0,0)
            root4.title('Confirmation')
            tkinter.Label(root4,text = 'Failed To Send Mail').pack()
            con = tkinter.Button(root4,text = 'OK',bg = 'Light Blue', command = root4.destroy,font=('unispace',8,'bold')).pack()
            root4.mainloop()


    def submit(pw,mail1,mail2,username,description):
        #from datetime import datetime
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        sub = 'Password Generation'

        body = f'''USERNAME - {username}
PASSWORD - {pw}
DESCRIPTION - 
{description}


Mail generated at {now}'''
        



        if mail1==mail2:
            send_email('csprojteam3@gmail.com','yylezzgg',mail1,sub,body)
        else:
            root5 = tkinter.Tk()
            root5.geometry('300x50')
            root5.resizable(0,0)
            root5.title('Confirmation')
            tkinter.Label(root5,text = 'E-Mail ID does not match').pack()
            con = tkinter.Button(root5,text = 'OK',bg = 'Light Blue', command = root5.destroy,font=('unispace',8,'bold')).pack()
            root5.mainloop()




    #CREATING AND SETTING UP A SECONDARY GUI INTERFACE
    root2 = tkinter.Tk()
    root2.geometry('340x400')
    root2.title("Mail Form")
    root2.resizable(0,0)
    ti = tkinter.Label(root2,text = "Mail Entry Form", font = ('Arial',25)).grid(row=0,column=0,columnspan=2)
    
    
       
    #CREATING WIDGETS FOR ENTRY FORM
    #username entry
    tkinter.Label(root2,text = "Username").grid(row = 1,column =0)  
    entry1 = tkinter.Entry(root2,width = 40)
    entry1.grid(row = 1,column =1)

    #description entry
    tkinter.Label(root2,text = "Description").grid(row=3,column=0)
    entry2 = tkinter.Text(root2,height = 10,width = 30)
    entry2.grid(row=3,column=1,)

    

    tkinter.Label(root2,).grid(row = 4,column=0,columnspan=2)

    #email entry
    tkinter.Label(root2, text = 'E-Mail').grid(row=5,column=0)
    entry3 = tkinter.Entry(root2,width=40)
    entry3.grid(row=5,column=1)
    
    #retype email entry
    tkinter.Label(root2,text = 'Retype E-Mail').grid(row=6,column=0)
    entry4 = tkinter.Entry(root2,width=40)
    entry4.grid(row=6,column=1)

    tkinter.Label(root2,).grid(row=7,column=0,columnspan=2)
    sub = tkinter.Button(root2,text = 'Submit',bg = 'Light Blue', font=('unispace',8,'bold'),command = lambda: submit(pword,entry3.get(),entry4.get(),entry1.get(),entry2.get(1.0,'end'))).grid(row=8,column=0,columnspan=2)

    

    
    
    root2.mainloop()
######################################################################################################################################################################
######################################################################################################################################################################
######################################################################################################################################################################


def dest():
    try:
        root2.destroy()
    except:
        pass



######################################################################################################################################################################

# SETUP FOR OBTAINING PASSWORD LENGTH
lentext = tkinter.Label(text = 'Password Length').grid()
pass_len = tkinter.IntVar()
pass_len.set('6')
lent = tkinter.Spinbox(root, from_=4, to_=16, textvariable = pass_len, width = 4,state = 'readonly').grid()

# SETUP FOR PASSWORD FORMAT
uppers =  tkinter.Checkbutton(root, text = 'Include Uppercase', command = uppertoggle).grid()
integers = tkinter.Checkbutton(root, text = 'Include Integers', command = inttoggle).grid()
special = tkinter.Checkbutton(root, text = "Include Special Characters", command = specialtoggle).grid()



# PASSWORD GENERATION GUI BUILD
tkinter.Label(root,).grid() 
genbut = tkinter.Button(root, text = 'Generate New Password', command = lambda:[passGen(pass_len.get(),constraints),dest(),makstrlab(passw)],bg='light green',fg='black',font=('unispace',8,'bold')).grid()
tkinter.Label(root,).grid()
tkinter.Entry(root,textvariable = pwd).grid()
tkinter.Label(root,).grid(row = 12)


mailpwd = tkinter.Button(root, text = 'Mail Password', command = lambda: mailgui(passw), bg = 'Light Blue',fg = 'Black', font=('unispace',8,'bold')).grid()
tkinter.Label(root,).grid()

ext = tkinter.Button(root, text = 'Exit', command = root.destroy, bg = 'tomato',fg = 'Black',font=('unispace',8,'bold')).grid()
strlab = tkinter.Label(root,)
strlab.grid()
root.mainloop()

######################################################################################################################################################################



