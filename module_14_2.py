"""To solve this problem, you will need a solution to the previous one.
To solve this, you need to supplement the existing code:
Delete not_telegram from the database.db record with id = 6.
Count the total number of entries.
Calculate the sum of all balances.
Display the average balance of all users in the console.
Example of the program execution result:
The code being executed:
# Code from the previous task
# Deleting a user with id=6
# Counting the number of all users
# Calculating the sum of all balances
print(all_balance / total_users)
connection.close()

Console output:
700.0"""

# Код из предыдущего задания
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


users = cursor.fetchall()
for user in users:
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')


# Удаление пользователя с id=6
cursor.execute("DELETE FROM Users  WHERE id = ?", (f"{6}",))
# Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchall()[0]
# Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)
connection.close()


connection.commit()
connection.close()
