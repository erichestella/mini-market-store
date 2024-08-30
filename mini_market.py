

from tkinter.constants import *
from tkinter import *
from tkinter import messagebox
from datetime import date
import customtkinter as ctk



tsu=ctk.CTk()
tsu.title('RICH IN FRUITIES')
tsu.geometry("1500x860")
tsu.geometry('+20+0')
tsu.config(bg="#D7682B")
tsu.resizable(False,False)

font1=('Georgia', 30, 'bold')
font2=('Eras Bold ITC', 30, 'bold')
font3=('Forte', 30, 'bold')
font4=('Cooper Black', 35, 'bold')
font5=('Imprint MT Shadow', 20, 'bold')

price_list=[20, 25]
total_price=0

bill_frame=ctk.CTkFrame(tsu, width=390,height=400, fg_color="#EB984E")
bill_frame.place(relx=0.51,rely=0.0)
 


wow_label=ctk.CTkLabel(tsu,text="(๑´• .̫ •ू`๑) RICH IN FRUITIES (˵¯͒〰¯͒˵)", font=font4,text_color="black", bg_color="#C39BD3")
wow_label.place(relx=0.02,rely=0.03)

orange_pic=PhotoImage(file=r"images/orange.png")
apple_pic=PhotoImage(file=r"images/apple.png")
logo_shop=PhotoImage(file=r"images/logo shop.png")
girll_ventor=PhotoImage(file=r"images/girl ventor.png")
cute_cat=PhotoImage(file=r"images/cat.png")
cute_dog=PhotoImage(file=r"images/cute dog.png")
cute_duck=PhotoImage(file=r"images/cute duck.png")
girll_baker=PhotoImage(file=r"images/girl baker.png")


def total():
    global total_price
    if(customer_entry.get()==''):
        messagebox.showwarning(title="Error",message="HEY! YOU FORGOT TO TYPE YOUR NAME :( - SHADEY")
    else:
      total_price=int(quntity1_combobox.get())*price_list[0]+int(quntity2_combobox.get())*price_list[1]
      if(total_price==0):
       messagebox.showwarning(title="Error", message= "Please select how many fruits do you prefer")
      else:
         title_label=ctk.CTkLabel(bill_frame, text='Bill Receipt', font=font3, bg_color="#EB984E")
         title_label.place(relx=0.25,rely=0.15)
         name_label=ctk.CTkLabel(bill_frame,text=f'Name: {customer_entry.get()}', font=font3, bg_color="#EB984E")
         name_label.place(relx=0.05,rely=0.25)
         price_label=ctk.CTkLabel(bill_frame,text=f'Total Price: ₱{total_price}',font=font3, bg_color="#EB984E")
         price_label.place(relx=0.07,rely=0.50)
         date_label=ctk.CTkLabel(bill_frame,text=f'Date Today: {date.today()}', font=font3, bg_color="#EB984E")
         date_label.place(relx=0.03,rely=0.38)
         twitter_label=ctk.CTkLabel(bill_frame, text='@_RICH_IN_FRUITIES', font=font5, bg_color="#EB984E")
         twitter_label.place(relx=0.15,rely=0.0)

def new():
   if(customer_entry.get()==''):
        messagebox.askyesno(title="Error",message="LOVEY, ARE YOU SURE YOU ARE CREATING NEW? - ILLIA")
   customer_entry.delete(0, END)
   quntity1_combobox.set(0)
   quntity2_combobox.set(0)
   for label in bill_frame.winfo_children():
        label.destroy()

    # Clear the list after removing labels
   bill_frame.pack_forget()

def save():
   if(customer_entry.get()==''):
        messagebox.askretrycancel(title="NOTE THIS! >:( )",message="HEY! PLEASE ENTER FIRST YOUR NICKNAME BEFORE ENTERING SAVE!! - MIKASA")
   f= open(f'{customer_entry.get()} Bill', "w")
   f.write(f'Customer Nickname: {customer_entry.get()}\n')
   f.write(f'Total Price: {total_price}₱ \n')
   f.write(f'Bill Date Purchase: {date.today()}')
   messagebox.showinfo(title="SAVED", message= 'BILL HAS BEEN SAVED')


apple=ctk.CTkLabel(tsu,image=apple_pic, text="APPLES\n Price: ₱ 20", font=font2, text_color="black", fg_color="#E6B0AA", width=270, height=200, compound=TOP, anchor=N)
apple.place(relx=0.06,rely=0.17)

orange=ctk.CTkLabel(tsu,image=orange_pic, text="ORANGES\n Price: ₱ 25", font=font2, text_color="black", fg_color="#E6B0AA", width=270, height=200, compound=TOP, anchor=N)
orange.place(relx=0.06,rely=0.58)

logo=ctk.CTkLabel(tsu,image=logo_shop,text="", font=font2,fg_color="#D7682B", width=130, height=50, compound=TOP, anchor=N)
logo.place(relx=0.73,rely=0.0)

girl_ventor=ctk.CTkLabel(tsu, image=girll_ventor, text="", font=font2,fg_color="#EB984E", width=130, height=50, compound=TOP, anchor=N )
girl_ventor.place(relx=0.52, rely=0.27)

cat=ctk.CTkLabel(tsu, image=cute_cat, text="", font=font2,fg_color="#D7682B", width=130, height=50, compound=TOP, anchor=N )
cat.place(relx=0.62, rely=0.76)


doggy=ctk.CTkLabel(tsu, image=cute_dog, text="", font=font2,fg_color="#D7682B", width=130, height=50, compound=TOP, anchor=N )
doggy.place(relx=0.45, rely=0.76)

duck=ctk.CTkLabel(tsu, image=cute_duck, text="", font=font2,fg_color="#D7682B", width=130, height=50, compound=TOP, anchor=N )
duck.place(relx=0.80, rely=0.76)

girl_baker=ctk.CTkLabel(tsu, image=girll_baker, text="", font=font2,fg_color="#D7682B", width=130, height=50, compound=TOP, anchor=N )
girl_baker.place(relx=0.77, rely=0.42)

quntity1_combobox=ctk.CTkComboBox(tsu,font=font3,text_color="white",fg_color="#1F618D", values=('1','2','3','4', '5'), state="readonly")
quntity1_combobox.place(relx=0.29,rely=0.35)
quntity1_combobox.set(0)

quntity2_combobox=ctk.CTkComboBox(tsu,font=font3,text_color="white",fg_color="#1F618D", values=('1','2','3','4', '5'), state="readonly")
quntity2_combobox.place(relx=0.29,rely=0.73)
quntity2_combobox.set(0)

nickname_label=ctk.CTkLabel(tsu,text= "Your Nickname:", font=font2,text_color="black", fg_color="#AF7AC5", corner_radius=10)
nickname_label.place(relx=0.45, rely=0.58)

customer_entry=ctk.CTkEntry(tsu, font=font2, placeholder_text= "Enter your name", fg_color="#FFBFE9", text_color="black", border_color="black", width=350)
customer_entry.place(relx=0.65, rely=0.58)

total_button=ctk.CTkButton(tsu,command=total, text="TOTAL PRICE:", font=font2, text_color="yellow", border_color="black", fg_color="#2E86C1", corner_radius=20, cursor="hand2")
total_button.place(relx=0.43,rely=0.70)

save_button=ctk.CTkButton(tsu,command=save, text="SAVE TOTAL:", font=font2, text_color="yellow", border_color="black",fg_color="#2E86C1", corner_radius=20, cursor="hand2")
save_button.place(relx=0.61, rely=0.70)

new_button=ctk.CTkButton(tsu,command=new, text="NEW RECEIPT:",font=font2, text_color="yellow", border_color="black", fg_color="#2E86C1",corner_radius=20, cursor="hand2")
new_button.place(relx=0.79,rely=0.70)

quantity_label=ctk.CTkLabel(tsu,text="QUANTITY:", font=font2,text_color="black", fg_color="brown", corner_radius=20)
quantity_label.place(relx=0.27,rely=0.28)

quantity_label=ctk.CTkLabel(tsu,text="QUANTITY:", font=font2,text_color="black", fg_color="brown", corner_radius=20)
quantity_label.place(relx=0.27,rely=0.65)


tsu.mainloop()
