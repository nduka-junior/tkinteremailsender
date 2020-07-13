import tkinter as tk
from tkinter import messagebox,filedialog
import smtplib
from smtplib import SMTPAuthenticationError,socket
from email.message import EmailMessage
import imghdr
root=tk.Tk()
root.iconbitmap('icon.ico')
root.geometry('800x650')
root.title('Email sender')
root.rowconfigure(0,weight=0,minsize=100)
root.columnconfigure(0,weight=2,minsize=400)

imgpath=[]

def openimage():
    global filename
    global imgpath
    filename=filedialog.askopenfilename(initialdir='/Pictures',title='Email Sender',)
    imgpath.append(filename)
    print(imgpath)
    
def emailsender(senderemail=None,password=None,subject=None,from_=None,to=None,content=None):
    senderemail=senderEmail.get()
    password=password.get()
    subject=subject.get()
    from_=from_.get()
    to=to.get()
    content=content.get('1.0',tk.END)
    if senderemail == '':
        messagebox.showerror('Error',"Sender's Email Cannot be Empty!!")
    elif password=='':
        messagebox.showerror('Error',"password Email Cannot be Empty!!")

    elif subject=='':
        messagebox.showerror('Error',"Subject Cannot be Empty!!")
    elif from_=='':
        messagebox.showerror('Error',"From_ Cannot be Empty!!")
    elif to=='':
        messagebox.showerror('Error',"To Cannot be Empty!!")
    elif content=='\n':
        messagebox.showerror('Error',"Content Cannot be Empty!!")

    else:
        try:
            msg=EmailMessage()
            msg['subject']=subject
            msg['From']=from_
            msg['To']=to
            msg.add_alternative(f'''\
            <!DOCTYPE html>
            <html lang="en">

            <body>
                
                <p>{content}</p>
                
            </body>
            </html>

            ''',subtype='html')
            if imgpath=='':
                print()
            else:
                for i in imgpath:
                    with open(i,'rb') as f:
                        file_data=f.read()
                        file_type=imghdr.what(f.name)
                        file_name=f.name
                    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(senderemail,password)

                smtp.send_message(msg)
        
        except SMTPAuthenticationError as e:
                messagebox.showerror('Authentication','User is not Authenticated')
        except socket.error as e:
                messagebox.showerror('Authentication','Could not Connect to Server')
        imgpath.clear()
        print(imgpath)


header=tk.Label(root,text='Send Your Message below',font=('Roboto','19','bold')).grid(row=0,column=0)

detailsFrame=tk.Frame(root,)
detailsFrame.grid(row=1,column=0,)

#  sender's Email
senderEmailLabel=tk.Label(master=detailsFrame,text="Sender's Email",font=('Roboto','14'),borderwidth=0)
senderEmailLabel.grid(row=0,column=0,sticky='w')

senderEmail=tk.Entry(master=detailsFrame,font=('Helvitica','13'),width=70)
senderEmail.grid(row=1,column=0,sticky='nesw',pady=6)

# sender's Password
senderpasswordLabel=tk.Label(master=detailsFrame,text="Password",font=('Roboto','14'),borderwidth=0)
senderpasswordLabel.grid(row=2,column=0,sticky='w')

senderpassword=tk.Entry(master=detailsFrame,font=('Helvitica','13'),width=70)
senderpassword.grid(row=3,column=0,pady=6)


# subject of the Email
sendersubjectLabel=tk.Label(master=detailsFrame,text="Subject",font=('Roboto','14'),borderwidth=0)
sendersubjectLabel.grid(row=4,column=0,sticky='w')

sendersubject=tk.Entry(master=detailsFrame,font=('Helvitica','13'),width=70)
sendersubject.grid(row=5,column=0,sticky='nesw',pady=6)


# Email from
senderfromLabel=tk.Label(master=detailsFrame,text="From",font=('Roboto','14'),borderwidth=0)
senderfromLabel.grid(row=6,column=0,sticky='w',)

senderfrom=tk.Entry(master=detailsFrame,font=('Helvitica','13'),width=70)
senderfrom.grid(row=7,column=0,pady=6)


#  Email To
sendertoLabel=tk.Label(master=detailsFrame,text="To",font=('Roboto','14'),borderwidth=0)
sendertoLabel.grid(row=8,column=0,sticky='w')

senderto=tk.Entry(master=detailsFrame,font=('Helvitica','13'),width=70)
senderto.grid(row=9,column=0,pady=6)


# Email Content
sendercontentLabel=tk.Label(master=detailsFrame,text="Content",font=('Roboto','14'),borderwidth=0)
sendercontentLabel.grid(row=10,column=0,sticky='w')

sendercontent=tk.Text(master=detailsFrame,font=('Helvitica','13'),height=5,width=70)
sendercontent.grid(row=11,column=0,pady=8)

# images
openimage=tk.Button(master=detailsFrame,text='Open Image',command=openimage)
openimage.grid(row=12,column=0,sticky='ne',pady=4)

send=tk.Button(master=detailsFrame,font=('Helvitica','13'),text='Send',width=70,command=lambda :emailsender(senderemail=senderEmail,password=senderpassword,subject=sendersubject,from_=senderfrom,to=senderto,content=sendercontent))
send.grid(row=13,column=0,pady=6)


root.mainloop()