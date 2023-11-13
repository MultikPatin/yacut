from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField
from wtforms.validators import DataRequired, Length, URL, Optional


class URLForm(FlaskForm):
    original_link = URLField(
        "Введите оригинальную ссылку",
        validators=[
            DataRequired(message="Обязательное поле"),
            URL(message="Введите URL"),
        ],
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=[Length(1, 16), Optional()],
    )
    submit = SubmitField("Добавить")
