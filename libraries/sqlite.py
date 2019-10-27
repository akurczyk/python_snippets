# Raises sqlite3.Error with SQL error inside
import sqlite3

#
# Connect to database engine
# This should be enclosed in try/finally or with statement to close the cursor and connection!
#
connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()


#
# Create table
#
cursor.execute('''
    create table posts
    (
        id int primary key,
        title varchar(200) null,
        content text null,
        author varchar(200) null
    )
''')
connection.commit()


#
# Insert single row
#
cursor.execute('insert into posts (title, content, author) values (?, ?, ?)', (
    'Lorem Ipsum',
    'Blah blah blah',
    'akurczyk',
))
connection.commit()
print(cursor.lastrowid)


#
# Insert multiple rows
#
cursor.executemany('insert into posts (title, content, author) values (?, ?, ?)', [
    ('Lorem Ipsum 2', 'Bla bla bla', 'akurczyk',),
    ('Lorem Ipsum 3', '...', 'akurczyk',),
])
connection.commit()


#
# Retrieve all rows
#
cursor.execute('select * from posts')
rows = cursor.fetchall()
for row in rows:
    print(f'ID: {row[0]}; Title: {row[1]}; Content: {row[2]}; Author: {row[3]}')


#
# Drop table
#
cursor.execute('drop table posts')
connection.commit()


# Disconnect from database engine
cursor.close()
connection.close()
