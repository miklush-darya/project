from django.forms import IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import Equal

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, EqualTo



class ProductrForm(FlaskForm):

    name_product = StringField('Name product', validators=[DataRequired(),])
    description = TextAreaField('description', validators=[DataRequired(),])
    characteristics = TextAreaField('characteristics', validators=[DataRequired(),])
    category = StringField('category', validators=[DataRequired(),])

    submit = SubmitField('Добавить продукт')


class CategoryForm(FlaskForm):

    name_category = StringField('Name category', validators=[DataRequired(),])

    submit = SubmitField('Добавить категорию')


class ShopProductForm(FlaskForm):

    price = StringField('Name product', validators=[DataRequired(),])
    quantity = IntegerField('description', validators=[DataRequired(),])
    product = StringField('characteristics', validators=[DataRequired(),])
    shop = StringField('shop', validators=[DataRequired(),])

    submit = SubmitField('Добавить продукт в магазин')