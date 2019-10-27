from pymongo import MongoClient

client = MongoClient('localhost', 27017)
first_database = client.first_database
first_collection = first_database.first_collection

document_1 = {
    'title': 'Lorem Ipsum',
    'content': 'Blah blah blah',
    'author': 'akurczyk',
    'value': 50,
    '123': 123,
}

document_2 = {
    'title': 'Lorem Ipsum 2',
    'content': 'Bla bla bla',
    'author': 'akurczyk',
    'value': 10,
    'abc': 'abc',
}

document_3 = {
    'title': 'Lorem Ipsum 3',
    'content': '...',
    'author': 'akurczyk',
    'value': 100,
    'xyz': 'xyz',
}

# Create index on 'value' field
first_collection.create_index('value')

# Insert first document
result_1 = first_collection.insert_one(document_1)
print(result_1.inserted_id)
print()

# Insert 3nd and 3rd document
result_2 = first_collection.insert_many([document_2, document_3])
print(result_2.inserted_ids)
print()

# Retrieve first document entitled 'Lorem Ipsum'
print('First entitled "Lorem Ipsum":')
result_3 = first_collection.find_one({'title': 'Lorem Ipsum'})
print(result_3)
print()

# Retrieve every document
print('Every document:')
result_4 = first_collection.find({})
for document in result_4:
    print(document)
print()

# Retrieve all documents with 'akurczyk' value in the 'author' field
print('With "akurczyk" value in the "author" field:')
result_5 = first_collection.find({'author': 'akurczyk'})
for document in result_5:
    print(document)
print()

# Retrieve all documents with value > 20
print('With "value" > 20:')
result_6 = first_collection.find({'value': {'$gt': 20}})
for document in result_6:
    print(document)
print()

print(first_collection.count_documents({}))  # Get number of records

first_collection.delete_many({})  # Delete all records

first_collection.drop()  # Drop collection

client.drop_database('first_database')  # Drop entire database
