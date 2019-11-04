#
# Declare tables
#
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    post = relationship('Post')

    def __repr__(self):
        return f'<User(id={self.id}, name={self.name})>'


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    id_author = Column(Integer, ForeignKey('user.id'))
    author = relationship('User', back_populates='post')
    published = Column(DateTime)

    def __repr__(self):
        return f'<Post(id={self.id}, title={self.title})>'


#
# Connect with DB engine
#
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)


#
# Create tables in empty DB
#
Base.metadata.create_all(engine)


#
# Create session in order to communicate with the DB
#
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


#
# Fill the DB with data
#
from datetime import datetime, timedelta

user1 = User(name='Jan Kowalski')
session.add(user1)
session.commit()

post1 = Post(title='Lorem Ipsum',
             content='Blah blah blah',
             author=user1,
             published=datetime.now())
post2 = Post(title='Lorem Ipsum 2',
             content='Bla bla bla',
             author=user1,
             published=datetime.now() - timedelta(minutes=5))
post3 = Post(title='Lorem Ipsum 3',
             content='...',
             author=user1,
             published=datetime.now() - timedelta(minutes=10))
session.add_all([post1, post2, post3])
session.commit()


#
# Query the DB
#
session = Session()
for post in session.query(Post).filter(Post.published < datetime.now() - timedelta(minutes=2)):
    print('-- Post:', post)
    print('-- Content:', post.content)
    print('-- Author:', post.author)
    print('-- Author Name:', post.author.name)
    print('-- Published:', post.published)
    print()
