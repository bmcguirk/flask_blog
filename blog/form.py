from flask_wtf import Form
from wtforms import StringField, validators, TextAreaField
from blog.models import Category
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from author.form import RegisterForm

class SetupForm(RegisterForm):
    name = StringField('Blog Title',[
        validators.Required(),
        validators.Length(max=80)
        ])

def categories():
    return Category.query

class PostForm(Form):
    title = StringField('Title', validators = [
        validators.Required(),
        validators.Length(max=80),
        ])
    body = TextAreaField('Post Content', validators = [
        validators.Required()
        ])
    category = QuerySelectField('Category', query_factory = categories, allow_blank = True)
    new_category = StringField('New Category')