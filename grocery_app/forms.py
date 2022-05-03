from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, FloatField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore, ItemCategory, User

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button

    title = StringField('Name of Store', validators=[DataRequired(), Length(min=3, max=80)])
    address = StringField('Address of Store', validators=[DataRequired(), Length(min=3, max=120)])
    submit = SubmitField('Add this New Store')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    
    name = StringField('Name of Product', validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField('Price of Product', validators=[DataRequired()])
    category = SelectField('Category of Product', choices=ItemCategory.choices())
    photo_url = StringField('URL of Product Photo')
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query, allow_blank=False)
    submit = SubmitField('Add this New Product')
