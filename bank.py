import tkinter as tk

from mysql.connector import cursor


import mysql.connector  # database connection
connection= mysql.connector.connect(
    host="localhost",
    user="root",
    password="abcd1234",
    database="bank"
)
cursor = connection.cursor() # cursor is used to execute sql queries.

# create main window
root = tk.Tk()
root.title("BANK SYSTEM")
root.geometry("800x500")
root.configure(bg="sky blue")


# title
title = tk.Label(root,
     text="BANK MANAGEMENT SYSTEM",bg="sky blue",
     fg="royal blue",font = ("Verdana",14, "bold"))
title.pack(pady=15)
# main frame( CENTER EVERYTHING)
main_frame = tk.Frame(root, bg="sky blue")

main_frame.pack()

# label and entry
form_frame = tk.Frame(main_frame, bg="pink")
form_frame.grid(row=0, column=0, padx=10, pady=40)

tk.Label(form_frame, text="Account Number", bg="pink",
         fg="midnight blue", font=("calibri", 14)).grid(row=0, column=0, pady=10)
acc_entry = tk.Entry(form_frame, bg="white", fg="black",
                     font=("calibri", 14))
acc_entry.grid(row=0, column=1, pady=10)

tk.Label(form_frame, text="Name", bg="pink", fg="midnight blue",
         font=("calibri", 14)).grid(row=1, column=0, pady=10)
name_entry = tk.Entry(form_frame, bg="white", fg="black", font=("arial", 12))
name_entry.grid(row=1, column=1, pady=10)

tk.Label(form_frame, text="Amount", bg="pink", fg="midnight blue",
         font=("calibri", 14)).grid(row=2, column=0, pady=10)
amount_entry = tk.Entry(form_frame, bg="white", fg="black", font=("arial", 12))
amount_entry.grid(row=2, column=1, pady=10)


# function
def create_account():
    acc = acc_entry.get()
    name = name_entry.get()
    balance = float(amount_entry.get())
    sql = "insert into bank_account values(%s,%s,%s)"
    cursor.execute(sql, (acc, name, balance))
    connection.commit()

    result.config(text="Account Created Successfully")


def deposit():
    acc = acc_entry.get()
    amount = float(amount_entry.get())
    cursor.execute("select balance from bank_account where account_number=%s", (acc,))
    data = cursor.fetchone()
    if data:
        new_balance = data[0] + amount
        cursor.execute("update bank_account set balance=%s where account_number=%s",
                       (new_balance, acc))
        connection.commit()
        result.config(text="Account deposit Successfully")
    else:
        result.config(text="Account Not Found")


def withdraw():
    acc = acc_entry.get()
    amount = float(amount_entry.get())
    cursor.execute("select balance from bank_account where account_number=%s",
                   (acc,))
    data=cursor.fetchone()
    if data:
        new_balance = data[0] - amount
        cursor.execute("update bank_account set balance=%s where account_number=%s",
                        (new_balance, acc))
        connection.commit()
        result.config(text="Account Withdraw Successfully")
    else:
         result.config(text="Account Withdraw Failed")

def check_balance():
    acc = acc_entry.get()
    cursor.execute("select balance from bank_account where account_number = %s",
                   (acc,))
    date = cursor.fetchone()
    if date:
        result.config(text="Balance=" + str(date[0]))
    else:
        result.config(text="Account Not Found")



# buttons
button_frame = tk.Frame(main_frame, bg="sky blue")
button_frame.grid(row=1, column=0, padx=10, pady=20)

tk.Button(button_frame, text="CREATE ACCOUNT",
          command=create_account,
          bg="lime green", fg="black", width=30).grid(row=0, column=0, pady=5)
tk.Button(button_frame, text="DEPOSIT",
          command=deposit,
          bg="lime green", fg="black", width=30).grid(row=1, column=0, pady=5)

tk.Button(button_frame, text="WITHDRAW",
          command=withdraw,
          bg="lime green", fg="black", width=30).grid(row=2, column=0, pady=5)

tk.Button(button_frame, text="CHECK BALANCE",
          command=check_balance,
          bg="lime green", fg="black", width=30).grid(row=3, column=0, pady=5)
# RESULT
result = tk.Label(button_frame, text="Result", bg="sky blue",fg="red", font=("arial", 12))
result.grid(row=4, column=0, pady=5)

result.mainloop()

