from tkinter import *
from tkinter import messagebox
from datetime import date
import customtkinter as ctk

rich=ctk.CTk()
rich.title('RICH IN FRUITIES')
rich.geometry("1500x860")
rich.geometry("+20+0")
rich.config(bg="pink")
rich.resizable(False,False)

font1=('Bodoni MT Black', 30, 'bold')
font2=('Comic Sans MS', 30, 'bold')
font3=('Eras Bold ITC', 30, 'bold')
font4=('Cooper Black',35, 'bold')
font5=(('Eras Bold ITC', "1"))

price_list=[20, 25]
change=0

bill_frame=ctk.CTkFrame(rich,width=350,height=400, fg_color="#D5D8DC")
bill_frame.place(relx=0.48,y=0.05)
 
menu_label=ctk.CTkLabel(rich,text=" ٩(◕‿◕)۶ RICH IN FRUITIES (っ˘ڡ˘ς)", font=font4,text_color="black", bg_color="#D7BDE2")
menu_label.place(relx=0,rely=0)


orange=PhotoImage(file=r"images/orange cute.png")
apple=PhotoImage(file=r"images/cutie apple.png")
logo=PhotoImage(file=r"images/logo shop.png")
moneyy=PhotoImage(file=r"images/money.png")
girl_cooker=PhotoImage(file=r"images/girl cooker.png")
emoticon=PhotoImage(file=r"images/cute emoticon.png")
emoticon2=PhotoImage(file=r"images/cute emoticon2.png")
emoticon3=PhotoImage(file=r"images/cute angel emoticon.png")

def pay():
    global change
    if(customer_entry.get()==''):
        messagebox.showwarning(title="ERROR SPOTTED!!",message="HI, MISS/SIR I THINK YOU FORGOT TO ENTER YOUR NICKNAME. KINDLY PUT IT FIRST BEFORE PROCEEDING. THANK YOU<3- HANGE")
    else:
      total_fruits= int(apple_quantity.get()) *price_list[0] + int(orange_quantity.get()) *price_list[1]
      money= int(money_choices.get())
      change= money - total_fruits

      if total_fruits > money:
        customer_entry.delete(0, END)
        apple_quantity.set(0)
        orange_quantity.set(0)
        money_choices.set(0)

        for label in bill_frame.winfo_children():
            label.destroy()

    # Clear the list after removing labels
        bill_frame.pack_forget()
        return messagebox.showerror(title="INVALID INPUT", message="YOUR MONEY IS NOT ENOUGH")
        
      if total_fruits==0:
       messagebox.showwarning(title="Error", message= "PLEASE SELECT THE QUANTITY OF THE FRUITS YOU WANT, THANK YOU<3- TAKINA")
      else:
         bill_label=ctk.CTkLabel(bill_frame, text='Bill Receipt', font=font3, bg_color="#D5D8DC", text_color="black")
         bill_label.place(relx=0.20,rely=0.03)
         insta_label=ctk.CTkLabel(bill_frame, text='@_RICH_IN_FRUITIES', font=font3, bg_color="#D5D8DC", text_color="black")
         insta_label.place(relx=0.0,rely=0.90)
         name_label=ctk.CTkLabel(bill_frame,text=f'Customer: {customer_entry.get()}', font=font2, bg_color="#D5D8DC", text_color="black")
         name_label.place(relx=0.09,rely=0.20)
         price_label=ctk.CTkLabel(bill_frame,text=f'Total Change: {change}₱',font=font2, bg_color="#D5D8DC", text_color="black" )
         price_label.place(relx=0.09,rely=0.35)
         today_label=ctk.CTkLabel(bill_frame,text=f'Date : {date.today()}', font=font2, bg_color="#D5D8DC", text_color="black")
         today_label.place(relx=0.09,rely=0.50)
         
def new():
   if(change==0):
       messagebox.askyesnocancel(title="NOTE SPOTTED!!", message= "ARE YOU SURE YOU WANT TO CREATE NEW? - CHISATO<3")
   customer_entry.delete(0, END)
   apple_quantity.set(0)
   orange_quantity.set(0)
   money_choices.set(0)
   
   for label in bill_frame.winfo_children():
        label.destroy()

    # Clear the list after removing labels
   bill_frame.pack_forget()

def save():
   if(change==0):
       messagebox.askokcancel(title="WARNING SPOTTED!!", message= "BEFORE PRESSING OK, PLEASE ENTER YOUR NICKNAME AND TOTAL OF FRUITS YOU WANT- MISAKI<3")
   f= open(f'{customer_entry.get()} Bill', "w")
   f.write(f'Customer Nickname: {customer_entry.get()}\n')
   f.write(f'Total Price: {change}₱ \n')
   f.write(f'Bill Date Purchase: {date.today()}')
   messagebox.showinfo(title="SAVED", message= 'BILL HAS BEEN SAVED')

     

apple_label=ctk.CTkLabel(rich,image=apple, text="APPLES\n Price: ₱ 20", font=font2, text_color="black", fg_color="#DE3163", width=50, height=200, corner_radius=20, compound=TOP, anchor=N)
apple_label.place(relx=0.03,rely=0.17)

orange_label=ctk.CTkLabel(rich,image=orange, text="ORANGES\n Price: ₱ 25", font=font2, text_color="black", fg_color="#DE3163", width=130, height=200, corner_radius=20, compound=TOP, anchor=N)
orange_label.place(relx=0.23,rely=0.17)

logoo=ctk.CTkLabel(rich,image=logo,text="", font=font2,fg_color="pink", width=130, height=50, compound=TOP, anchor=N)
logoo.place(relx=0.74,rely=0.0)

moneyyy=ctk.CTkLabel(rich,image=moneyy, text="MONEY", font=font2, text_color="black", fg_color="#DE3163", width=130, height=200, corner_radius=20, compound=TOP, anchor=N)
moneyyy.place(relx=0.06,rely=0.63)

girl_cooking=ctk.CTkLabel(rich, image=girl_cooker, text="", font=font2, text_color="black", fg_color="pink", width=130, height=200,  compound=TOP, anchor=N)
girl_cooking.place(relx=0.83,rely=0.44)

emoticon_=ctk.CTkLabel(rich, image=emoticon, text="", font=font2,fg_color="pink", width=130, height=25, compound=TOP, anchor=N )
emoticon_.place(relx=0.45, rely=0.78)

emoticon_2=ctk.CTkLabel(rich, image=emoticon2, text="", font=font2,fg_color="pink", width=130, height=50, compound=TOP, anchor=N )
emoticon_2.place(relx=0.63, rely=0.76)

emoticon_3=ctk.CTkLabel(rich, image=emoticon3, text="", font=font2,fg_color="pink", width=130, height=50, compound=TOP, anchor=N )
emoticon_3.place(relx=0.82, rely=0.76)


apple_quantity=ctk.CTkComboBox(rich,font=font3,text_color="white",fg_color="gray", values=('1','2','3','4', '5'), state="readonly")
apple_quantity.place(relx=0.07,rely=0.57)
apple_quantity.set(0)

orange_quantity=ctk.CTkComboBox(rich,font=font3,text_color="white",fg_color="gray", values=('1','2','3','4', '5'), state="readonly")
orange_quantity.place(relx=0.28,rely=0.57)
orange_quantity.set(0)

money_choices=ctk.CTkComboBox(rich,font=font3,text_color="white",fg_color="gray", values=('10','50','100','200', '250'), state="readonly")
money_choices.place(relx=0.27,rely=0.81)
money_choices.set(0)

customer_label=ctk.CTkLabel(rich,text= "Customer Nickname:", font=font2,text_color="black", fg_color="#AF7AC5")
customer_label.place(relx=0.45, rely=0.58)

customer_entry=ctk.CTkEntry(rich, font=font2, fg_color="white", text_color="black", border_color="white", width=200)
customer_entry.place(relx=0.67,rely=0.58)

pay_button=ctk.CTkButton(rich,command=pay, text="TOTAL CHANGE:", font=font2, text_color="yellow", border_color="violet", fg_color="#2E86C1", corner_radius=20, cursor="hand2")
pay_button.place(relx=0.4,rely=0.70)

save_button=ctk.CTkButton(rich,command=save, text="SAVE RECEIPT:", font=font2, text_color="yellow", border_color="violet",fg_color="#2E86C1", corner_radius=20, cursor="hand2")
save_button.place(relx=0.6, rely=0.70)

new_button=ctk.CTkButton(rich,command=new, text="CREATE NEW:",font=font2, text_color="yellow", border_color="violet", fg_color="#2E86C1",corner_radius=20, cursor="hand2")
new_button.place(relx=0.79,rely=0.70)

rich.mainloop()
