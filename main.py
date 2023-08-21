from tkinter import *
from tkinter import messagebox
from pyqrcode import QRCode
from barcode import Code128
from barcode.writer import ImageWriter
root=Tk()
root.title("برنامه کیو آر کد")
root.geometry("500x500")

menu=Menu(root)
amenu=Menu(menu)
def message_1():
    messagebox.showinfo("درباره برنامه","برنامه ما هر متن انگلیسی را به کیو آر کد تبدیل می کند")
amenu.add_command(label="درباره برنامه",command=message_1)
def message_2():
    messagebox.showinfo("درباره من","من دانش آموز کلاس هشتم مدرسه بحرالعلوم هستم و این برنامه را برای مسابقه پژوهش سرا درست کردم")
amenu.add_command(label="ﺩرباره من",command=message_2)
menu.add_cascade(label="درباره",menu=amenu)
root.config(menu=menu)
def gen():
    f=open("number.txt","r")
    num=f.read()
    z=a.get("1.0","end")
    aa=QRCode(z)
    aa.png(f"Qrcode/file-{num}.png",8)
    f.close()
    f=open("number.txt","w")
    num=int(num)
    f.write(f"{num+1}")
def gen1():
    f=open("num.txt","r")
    num=f.read()
    z=a.get("1.0","end")
    print(type(z))
    z=str(z)
    print(type(z))
    aa=Code128(z,writer=ImageWriter())
    aa.save(f"Barcode/file-{num}")
    f.close()
    f=open("num.txt","w")
    num=int(num)
    f.write(f"{num+1}")

a1=StringVar()
a=Text(root)
a.pack(fill = BOTH, expand = True)
b=Button(root,command=gen,text="ساختن کیو آر کد")
c=Button(root,command=gen1,text="ساختن بارکد")
b.pack(side = LEFT,fill = BOTH, expand = True)
c.pack(side = LEFT,fill = BOTH, expand = True)


root.mainloop()
