import sqlite3
import csv

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute('''
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY, 
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        gender TEXT,
        age INTEGER,
        group_name TEXT
    )
''')
print("Table 'users' created successfully.")

print("Reading CSV file...")

with open('user.csv', 'r') as file:
    reader = csv.reader(file)
    
    next(reader) 
    
    count = 0
    
    for row in reader:
        if count == 10:
            break  
            
        u_id = row[0]
        f_name = row[1]
        l_name = row[2]
        email = row[3]
        gender = row[4]
        age = row[5]
        group = row[6]
        
        cursor.execute('''
            INSERT INTO users (user_id, first_name, last_name, email, gender, age, group_name)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (u_id, f_name, l_name, email, gender, age, group))
        
        print(f"Inserted #{count + 1}: {f_name} {l_name}")
        
        count += 1

conn.commit()
print("Success! Saved the top 10 users to users.db")

cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()

for user in all_users:
    print(user)

conn.close()