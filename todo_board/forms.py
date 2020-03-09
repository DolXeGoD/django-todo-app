from django import forms
from .models import TbTodoList

class TodoForm(forms.ModelForm):
    class Meta:
        model = TbTodoList
        fields = ('title', 'content', 'end_date')