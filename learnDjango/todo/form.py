from django import forms
from .models import Todo

class PersonForm(forms.Form):
    name = forms.CharField(label="name", max_length=100, required=True)
    age = forms.IntegerField(label="age", )

#“This form should be connected to the Todo table.”
#A ModelForm = blueprint of the model’s fields
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo #This points to the database table ie class Todo of models.py
        fields = ['title', 'description', 'done', 'deadline', 'importance']  # table column from models.py
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }
