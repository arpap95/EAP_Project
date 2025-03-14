from tkinter import *

root = Tk()
root.title("Appointments")
root.geometry("1600x1020")
root.configure(background = "black")
root.resizable(width= True, height=True)
label1 = Label(root, text="Προσθήκη πελάτη", bg="black", fg="white", font= "arial 12")
label1.place(x=10, y=20)


label2 = Label(root, text="Name", bg="black", fg="white", font= "arial 12")
label2.place(x=10, y=50)
text1 =Entry(root, width=20, bg="black", font="aria 12")
text1.place(x=100, y=50)

label3 = Label(root, text="Surname", bg="black", fg="white", font= "arial 12")
label3.place(x=10, y=100)
text2 =Entry(root, width=20, bg="black", font="aria 12")
text2.place(x=100, y=100)

label4 = Label(root, text="Email", bg="black", fg="white", font= "arial 12")
label4.place(x=10, y=150)
text3 =Entry(root, width=20, bg="black", font="aria 12")
text3.place(x=100, y=150)

label5 = Label(root, text="Phone", bg="black", fg="white", font= "arial 12")
label5.place(x=10, y=200)
text4 =Entry(root, width=20, bg="black", font="aria 12")
text4.place(x=100, y=200)

b1=Button(root, text="Cancel", width=10, height=1, bg="red", font="arial 12")
b1.place(x=10, y=300)
b1=Button(root, text="Submit", width=10, height=1, font="arial 12")
b1.place(x=160, y=300)

root.mainloop()

