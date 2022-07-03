from wtforms import Form
from wtforms.fields import (
    HiddenField,StringField, IntegerField, TelField, SubmitField)


class CreateForm(Form):
    name = StringField('名前')
    age = IntegerField('年齢')
    comment = TelField('コメント')
    submit = SubmitField('submit')

class UpdateForm(Form):
    id = HiddenField()
    name = StringField('名前')
    age = IntegerField('年齢')
    comment = TelField('コメント')
    submit = SubmitField('update')

class DeleteForm(Form):
    id = HiddenField()
    submit = SubmitField('delete')


