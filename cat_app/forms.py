from django import forms

class CatNameForm(forms.Form):
    name = forms.CharField(label="Введите имя кота", max_length=100)

class InteractionForm(forms.Form):
    ACTIONS = [
        ('feed', 'Покормить'),
        ('play', 'Поиграть'),
        ('sleep', 'Уложить спать'),
    ]
    action = forms.ChoiceField(choices=ACTIONS, label="Действие")
