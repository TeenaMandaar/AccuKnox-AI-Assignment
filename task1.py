import requests 
import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS library_books") 
cursor.execute('''
    CREATE TABLE library_books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        publication_year INTEGER
    )
''')

response = requests.get("https://openlibrary.org/subjects/science_fiction.json?limit=5")

if response.status_code == 200:
    data = response.json()
    books = data['works']

    for book in books:
        title = book['title']
        publication_year = book['first_publish_year']
        if len(book.get('authors', [])) > 0:
            author = book['authors'][0]['name']
        else:
            author = "Unknown"
        
        cursor.execute('''
            INSERT INTO library_books (title, author, publication_year)
            VALUES (?, ?, ?)
        ''', (title, author, publication_year))
    
    conn.commit()
    print("Success! Data saved to Database.\n")

else:
    print("Error: API failed.")

print("--- READING DATABASE CONTENTS ---")

cursor.execute("SELECT * FROM library_books")

all_rows = cursor.fetchall()

for row in all_rows:
    print(f"ID: {row[0]} | Book: {row[1]} | By: {row[2]}")

conn.close()