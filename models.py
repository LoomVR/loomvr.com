# # models work
# basic user info
# whether or not they paid
import datetime
from flask import flash
from peewee import *
from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin

DATABASE = SqliteDatabase('loomy.db')

class User(Model, UserMixin):

    class Meta:
        datebase = DATABASE
        order_by = ('-joined_at',)

    username = CharField(unique=True)
    first_name = CharField()
    last_name = CharField()
    email = CharField(unique=True) # validation is handled through forms
    password = CharField(max_length=120)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin= BooleanField(default=False)
    testimonial = TextField(null=True)

    @classmethod
    def create_user(cls, username, first_name, last_name, email, passwordinput, is_admin=False):
        try:
            with DATABASE.transaction():
                cls.get_or_create(
                #order matters
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = generate_password_hash(passwordinput),
                is_admin = is_admin
                )
        except IntegrityError:
            flash("We already have a user like that. Try logging in!")

class Purchase(Model):
    #add foriegn key field
    # user = ForiegnKeyField(model=User.username)
    # sendToEmailOnFile = BooleanField()
    paid = BooleanField(default=False)
    userFeedback = CharField()

class Contact(Model):
    message = CharField()
    # sender = # foriegn key field

class BlogPost(Model):
    title = CharField()
    body = TextField()
    author = CharField()

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Contact,BlogPost], safe=True)
    # User.create_user("david", "David","Axelrod", "daxaxelrod@gmail.com","Axelpods",True)
    # User.create_user("alex", "David","Jackson", "daxaxelrod@gmail.com","alex",True)
    # User.create_user("jack", "David","Guinta", "daxaxelrod@gmail.com","jack",True)
    # User.create_user("jesse", "David","Pelzar", "daxaxelrod@gmail.com","jesse",True)
    DATABASE.close()
