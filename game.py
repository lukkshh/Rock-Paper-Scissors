from tkinter import PhotoImage
import customtkinter , random
items = ['rock','paper','scissors']
def rock():
    b = random.choice(items)
    if b == 'rock':
        btext.configure(text='A Draw' , fg='#43ff14')
        bphoto.configure(image=rock_img)
    elif b == 'paper':
        btext.configure(text='You Lose !', fg='#f00')
        bphoto.configure(image=paper_img)
    elif b == 'scissors':
        btext.configure(text='You Win !', fg='#f7ff14')
        bphoto.configure(image=scissors_img)
def paper():
    b = random.choice(items)
    if b == 'rock':
        btext.configure(text='You Win !', fg='#f7ff14')
        bphoto.configure(image=rock_img)
    elif b == 'paper':
        btext.configure(text='A Draw',fg='#43ff14')
        bphoto.configure(image=paper_img)
    elif b == 'scissors':
        btext.configure(text='You Lose !', fg='#f00')
        bphoto.configure(image=scissors_img)
def scissors():
    b = random.choice(items)
    if b == 'rock':
        btext.configure(text='You Lose !',fg='#f00')
        bphoto.configure(image=rock_img)
    elif b == 'paper':
        btext.configure(text='You Win !', fg='#f7ff14')
        bphoto.configure(image=paper_img)
    elif b == 'scissors':
        btext.configure(text='A Draw',fg='#43ff14')
        bphoto.configure(image=scissors_img)
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')
root = customtkinter.CTk()
root.title('RPS GAME')
root.geometry('500x550')
root.resizable(False,False)
rock_img = PhotoImage(file="./assets/rock.png")
paper_img = PhotoImage(file="./assets/paper.png")
scissors_img = PhotoImage(file="./assets/scissors.png")
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20 , padx=20 , fill='both', expand=True)
bot_f = customtkinter.CTkFrame(master=frame)
bot_f.pack_propagate(0)
bot_f.pack(pady=20 , padx=20 , fill='x')
btext = customtkinter.CTkLabel(master=bot_f,text='')
btext.configure(font=('Arial',25))
btext.pack(pady=1,padx=1)
bphoto = customtkinter.CTkLabel(master=bot_f, image=None , text='')
bphoto.pack(padx=1,pady=2)
buttons = customtkinter.CTkFrame(master=frame, height=200)
buttons.pack_propagate(0)
buttons.pack(pady=20 , padx=20 , fill='x')
lukkshh = customtkinter.CTkLabel(master=frame, text='LUKKSHH')
lukkshh.configure(font=('Arial',15))
lukkshh.pack()
rock = customtkinter.CTkButton(master=buttons , image=rock_img , width=100 , height=120 , text='' , command=rock)
paper = customtkinter.CTkButton(master=buttons , image=paper_img , width=100 , height=120 , text='' , command=paper)
scissors = customtkinter.CTkButton(master=buttons, image=scissors_img , width=100 , height=120 , text='', command=scissors)
rock.pack(side=customtkinter.LEFT , expand=2)
paper.pack(side=customtkinter.LEFT , expand=2)
scissors.pack(side=customtkinter.LEFT , expand=2)
root.mainloop()