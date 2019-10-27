# Raises psycopg2.Error with SQL error inside
import psycopg2


#
# Connect to database engine
# This should be enclosed in try/finally or with statement to close the cursor and connection!
#
connection = psycopg2.connect(host='localhost', port=5432, user='olo', password='olo', database='python_snippets')
cursor = connection.cursor()


#
# Create table
#
cursor.execute('''
    create table posts
    (
        id serial,
        title varchar(200),
        content text,
        author varchar(200)
    )
''')
connection.commit()


#
# Insert single row
#
cursor.execute('insert into posts (title, content, author) values (%s, %s, %s) returning id', (
    'Lorem Ipsum',
    'Blah blah blah',
    'akurczyk',
))
connection.commit()
print(cursor.fetchone()[0])


#
# Insert multiple rows
#
cursor.executemany('insert into posts (title, content, author) values (%s, %s, %s)', [
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


#
# Disconnect from database engine
#
cursor.close()
connection.close()
