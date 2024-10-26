"""Create a not_telegram database file.db and connect to it using the built-in sqlite3 library.
Create a cursor object and follow these steps using SQL queries:
Create a Users table if it hasn't been created yet. The following fields must be present in this table:
id - integer, primary key
username - text (not empty)
email - text (not empty)
age - integer
balance is an integer (not empty)
Fill it with 10 entries:
User1, example1@gmail.com, 10, 1000
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 1000
...
User10, example10@gmail.com, 100, 1000
Update the balance for each 2nd entry starting from the 1st by 500:
User1, example1@gmail.com, 10, 500
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 500
...
User10, example10@gmail.com, 100, 1000
Delete every 3rd entry in the table starting from the 1st:
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 500
User5, example5@gmail.com, 50, 500
...
User9, example9@gmail.com, 90, 500

Make a selection of all records using fetchall(), where the age is not equal to 60 and output them to the console in the following format (without id):
Name: <username> | Email: <email> | Age: <age> | Balance: <balance>"""
import  sglite3
from pythonProject1.codewars.nob import result
from urllib3 import connection_from_url

connection = sglite3.commect("not_telegram.db")
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL 
)
''')

for i in range(10):
   cursor.execute("INSER INFO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
                  (f"nemuser{i}", f"{i}ex@mail.ru", f"{i*10}", "1000"))


for i in range(10):
    if i % 2 == 0:
        cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, "namuser"))

for i in range(10):
    if i % 3 == 0:
        cursor.execute("DELETE FROM Users  WHERE id = ?", (f"{i}",))


cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')


connection.commit()
connection.close()
