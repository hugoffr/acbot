from mongoengine import Document, StringField, DateField, IntField

class TurnipPrice(Document):
  user_id = IntField(required=True, unique_with=['date', 'time_of_day'])
  date = DateField(required=True)
  time_of_day=StringField(choices=['AM', 'PM'])
  price=IntField(min_value=0)