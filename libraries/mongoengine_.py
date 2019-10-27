import datetime

import mongoengine

mongoengine.connect('first_database', host='localhost', port=27017)


class Post(mongoengine.Document):
    title = mongoengine.StringField(required=True, max_length=200)
    content = mongoengine.StringField(required=True)
    author = mongoengine.StringField(required=True, max_length=50)
    value = mongoengine.IntField(required=True)
    published = mongoengine.DateTimeField(default=datetime.datetime.now)


# Insertion
post_1 = Post(title='Lorem Ipsum', content='Blah blah blah', author='akurczyk', value=100,)
post_1.save()

post_2 = Post(title='Lorem Ipsum 2', content='Bla bla bla', author='akurczyk', value=50,)
post_2.save()

post_3 = Post(title='Lorem Ipsum 3', content='...', author='akurczyk', value=10,)
post_3.save()

# Change
post_1.title = 'Lorem Ipsum Changed'
post_1.save()

# Retrieve every document
print('*:')
for document in Post.objects:
    print(document.title)
print()

# Retrieve every documents with 'author' field == 'akurczyk'
print('"author" == "akurczyk":')
for document in Post.objects.filter(author='akurczyk'):
    print(document.title)
print()

# Retrieve every documents with 'value' field > 20
print('"value" > 20')
for document in Post.objects.filter(value__gt=20):
    print(document.title)
print()

# Drop all documents
Post.drop_collection()
