from django import forms
from .models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= ['task', 'due_datetime','is_completed']

        widgets={
            'task':forms.TextInput(attrs={'placeholder':"Add Task"}),
            'due_datetime':forms.DateInput(attrs={"type":"date"}),
            'is_completed':forms.CheckboxInput(attrs={"class":"'class': 'required checkbox form-control'"})
        }