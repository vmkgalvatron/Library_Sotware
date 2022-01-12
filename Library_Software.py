import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime as dt
import time
import pandas as pd
from pandas import ExcelWriter

user_name = ['Vedant', 'Baba', 'Aai']
user_passwords = ['9401', '9194', '8922']
users = ['Vedant', 'Baba', 'Aai']
books = ['Basics', 'Intermediate', 'Advance', 'Beginner', 'Excellent']
dates = []
times = []
user = []
book = []
status = []
books_available = [1, 2, 3, 4, 5]
create_catageories = {'ARDUINO': ['Basics', ',Intermediate', ',Advance'],
                      'PYTHON': ['Beginner', 'Excellent']}

large_font = ("times new roman", 30, 'bold')


class libraryManagement(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'Library Management System')
        container = tk.Frame(self)
        container.configure(height=1080, width=1920)
        container.pack()

        self.frames = {}
        for f in (loginpage, pageone, pagetwo, pagethree):
            frame = f(container, self)

            self.frames[f] = frame

            frame.place(relheight=1, relwidth=1)

        self.show_frame(loginpage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class loginpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg='#f2f4eb')
        frame90 = tk.Frame(self, bg='#817d8d')
        frame90.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        label = tk.Label(self, text='Login', bg='#817d8d', fg='white', font=large_font)
        label.pack()
        button = tk.Button(self, text="Submit", font=15,
                           command=lambda: test(entry.get(), password_entry.get()))
        button.place(relx=0.45, rely=0.6)

        entry = ttk.Entry(self, font=15)
        entry.place(relx=0.34, rely=0.4)
        name_label = tk.Label(self, text='Name :', border=0, font=15)
        name_label.place(relx=0.2, rely=0.4)
        password_entry = ttk.Entry(self, font=15)
        password_entry.place(relx=0.34, rely=0.47)

        password_label = tk.Label(self, text='Password :', border=0, font=15)
        password_label.place(relx=0.2, rely=0.47)

        def test(x, y):
            li = []
            if x == "" or y == "":
                messagebox.showerror('Empty Credentials', 'Fill all credentials!')
                controller.show_frame(loginpage)

            elif x != '' and y != '':
                for i in range(2):
                    if user_name[i] == x and user_passwords[i] == y:
                        '''messagebox.showinfo('Greet', 'Login successful')'''
                        entry.option_clear()
                        li.append('1')
                        controller.show_frame(pageone)
                if '1' not in li:
                    messagebox.showerror('error', "invalid credentials")
                    controller.show_frame(loginpage)


class pageone(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg='#f2f4eb')
        frame90 = tk.Frame(self, bg='#bab1b6')
        frame90.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        label1 = tk.Label(self, text='Transaction', bg='#bab1b6', font=large_font)
        label1.pack()
        frame4 = tk.Frame(self, bg="grey")
        frame4.place(relx=0, rely=0.05, relwidth=1, relheight=0.04)
        button2 = tk.Button(frame4, text='logout', command=lambda: controller.show_frame(loginpage))
        button2.place(relx=0.95, rely=0.2)
        frame8 = tk.Frame(self, bg='grey')
        frame8.place(relx=0, rely=0.09, relheight=0.91, relwidth=0.15)
        button5 = tk.Button(frame8, text='Transaction', font=('verdana', 15),
                            command=lambda: controller.show_frame(pageone))
        button5.pack(fill='x')
        button3 = tk.Button(frame8, text='Enquiry', font=('verdana', 15),
                            command=lambda: controller.show_frame(pagetwo))
        button3.pack(fill='x')
        storeButton = tk.Button(frame8, text='Inventory', font=('verdana', 15),
                                command=lambda: controller.show_frame(pagethree))
        storeButton.pack(fill='x')
        entry1 = ttk.Entry(self, font=15)
        entry1.place(relx=0.45, rely=0.4)
        studentno_label1 = tk.Label(self, text='Student ID :', border=0, font=(15))
        studentno_label1.place(relx=0.3, rely=0.4)
        bookno_entry1 = ttk.Entry(self, font=15)
        bookno_entry1.place(relx=0.45, rely=0.49)

        password_label1 = tk.Label(self, text='Book ID  :', border=0, font=(15))
        password_label1.place(relx=0.3, rely=0.49)
        button7 = tk.Button(self, text="Return", bg='white', fg='black', font=('times new roman', 15),
                            command=lambda: test1(entry1.get(), bookno_entry1.get(), 'return'))
        button7.place(relx=0.4, rely=0.6)

        button8 = tk.Button(self, text="Issue", bg='white', fg='black', font=('times new roman', 15),
                            command=lambda: test1(entry1.get(), bookno_entry1.get(), 'issue'))
        button8.place(relx=0.6, rely=0.6)

        def test1(x, y, z):
            li = []
            if x == "" or y == "":
                messagebox.showerror('Empty Credentials', 'Fill all credentials!')
                controller.show_frame(pageone)

            elif x != '' and y != '':
                for i in range(len(users)):
                    if users[i] == x:
                        t=time.asctime()
                        if z == 'issue':
                            dates.append(str(dt.date.today()))
                            times.append(t[11:19])
                            user.append(users[i])
                            book.append(books[books.index(y)])
                            status.append('Issued')
                            books_available[books.index(y)] -= 1
                            messagebox.showinfo('Success', 'Issued Successfully')
                            li.append(1)
                            controller.show_frame(pageone)
                        elif z == 'return':
                            dates.append(str(dt.date.today()))
                            times.append(t[11:19])
                            user.append(users[i])
                            book.append(books[books.index(y)])
                            status.append('Returned')
                            books_available[books.index(y)] += 1
                            messagebox.showinfo('Success', 'Returned Successfully')
                            li.append(1)
                            controller.show_frame(pageone)

                if 1 not in li:
                    messagebox.showerror('invalid', 'invalid credentials')
                    controller.show_frame(pageone)


class pagetwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg='#f2f4eb')
        frame90 = tk.Frame(self, bg='#bab1b6')
        frame90.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        label2 = tk.Label(self, text='Enquiry', font=large_font, bg='#bab1b6')
        label2.pack()
        frame4 = tk.Frame(self, bg="grey")
        frame4.place(relx=0, rely=0.05, relwidth=1, relheight=0.04)
        button4 = tk.Button(frame4, text='logout', command=lambda: controller.show_frame(loginpage))
        button4.place(relx=0.95, rely=0.2)
        frame8 = tk.Frame(self, bg='grey')
        frame8.place(relx=0, rely=0.09, relheight=0.91, relwidth=0.15)
        button5 = tk.Button(frame8, text='Transaction', font=('verdana', 15),
                            command=lambda: controller.show_frame(pageone))
        button5.pack(fill='x')
        button3 = tk.Button(frame8, text='Enquiry', font=('verdana', 15),
                            command=lambda: controller.show_frame(pagetwo))
        button3.pack(fill='x')
        storeButton = tk.Button(frame8, text='Inventory', font=('verdana', 15),
                                command=lambda: controller.show_frame(pagethree))
        storeButton.pack(fill='x')
        lable6 = tk.Label(self, text='Availability :', font=(15))
        lable6.place(relx=0.26, rely=0.4)
        entry2 = ttk.Entry(self, font=15)
        entry2.place(relx=0.35, rely=0.4)
        lable9 = tk.Label(self, text='Catageory :', font=15)
        lable9.place(relx=0.51, rely=0.4)
        entry3 = ttk.Entry(self, font=15)
        entry3.place(relx=0.6, rely=0.4)
        button56 = tk.Button(self, text='find', font=15, command=lambda: catageory_search(entry3.get()))
        button56.place(relx=0.6, rely=0.6)
        button90 = tk.Button(self, text='Check', font=15, command=lambda: avail(entry2.get()))
        button90.place(relx=0.4, rely=0.6)

        def avail(x):
            li = []
            for i in range(len(books)):
                if books[i] == x:
                    print(books_available[i])
                    messagebox.showinfo('availability', 'books available: {}'.format(books_available[i]))
                    li.append(1)
                    controller.show_frame(pagetwo)
            if 1 not in li:
                messagebox.showerror('Unavailable', 'Book not available')
                controller.show_frame(pagetwo)

        def catageory_search(x):
            if x.upper() in create_catageories:
                messagebox.showinfo('books', create_catageories[x.upper()])
            else:
                messagebox.showerror('error', 'unable to find')


class pagethree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg='#f2f4eb')
        frame90 = tk.Frame(self, bg='#bab1b6')
        frame90.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        label2 = tk.Label(self, text='Inventory', font=large_font, bg='#bab1b6')
        label2.pack()
        frame4 = tk.Frame(self, bg="grey")
        frame4.place(relx=0, rely=0.05, relwidth=1, relheight=0.04)
        button4 = tk.Button(frame4, text='logout', command=lambda: controller.show_frame(loginpage))
        button4.place(relx=0.95, rely=0.2)
        frame8 = tk.Frame(self, bg='grey')
        frame8.place(relx=0, rely=0.09, relheight=0.91, relwidth=0.15)
        button5 = tk.Button(frame8, text='Transaction', font=('verdana', 15),
                            command=lambda: controller.show_frame(pageone))
        button5.pack(fill='x')
        button3 = tk.Button(frame8, text='Enquiry', font=('verdana', 15),
                            command=lambda: controller.show_frame(pagetwo))
        button3.pack(fill='x')
        storeButton = tk.Button(frame8, text='Inventory', font=('verdana', 15),
                                command=lambda: controller.show_frame(pagethree))
        storeButton.pack(fill='x')
        lable6 = tk.Label(self, text='Catageory :', font=(15))
        lable6.place(relx=0.26, rely=0.4)
        entry2 = ttk.Entry(self, font=15)
        entry2.place(relx=0.35, rely=0.4)
        lable9 = tk.Label(self, text='Book :', font=15)
        lable9.place(relx=0.51, rely=0.4)
        entry3 = ttk.Entry(self, font=15)
        entry3.place(relx=0.6, rely=0.4)
        button56 = tk.Button(self, text='Add', font=15, command=lambda: add())
        button56.place(relx=0.55, rely=0.6)

        def add():
            x = entry2.get().upper()
            y = entry3.get()
            if x != "" and y != "":
                if x not in create_catageories:
                    create_catageories[x.upper()] = [y]
                    messagebox.showinfo('Success', 'Book  added with new Catageory')
                if x in create_catageories:
                    create_catageories[x].append(y)
                    messagebox.showinfo('Success', 'Book added to existing Catageory')
            if x == '' or y == '':
                messagebox.showerror('Error', 'Fill all credentials')


app = libraryManagement()
app.mainloop()

df = pd.DataFrame({'date': dates,
                   'time': times,
                   'student': user,
                   'book': book,
                   'status': status})

excel_df = pd.read_excel('Library_Register.xlsx')

new_df = pd.concat([excel_df, df])

writer = ExcelWriter('Library_Register.xlsx')

new_df.to_excel(writer, 'Sheet1', index=False)

writer.save()
