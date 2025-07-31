from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fullname', 'empid', 'email', 'position']
        labels = {
            'fullname': 'Full Name',
            'empid': 'Employee ID',
            'email': 'Email Address',
            # 'position': 'Position'
        }
        widgets = {
            'fullname': forms.TextInput(attrs={'id':'icon_prefix', 'class': 'validate'}),
            'empid': forms.TextInput(attrs={'id':'icon_prefix', 'class': 'form-control validate'}),
            'email': forms.EmailInput(attrs={'id':'icon_prefix','class': 'form-control validate'}),
            'position': forms.Select(attrs={'id':'icon_prefix','class': 'validate'})
        }

#insert a "select position" option at the top of the position dropdown and sort the rest alphabetically
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Position"

        # Sort choices alphabetically by display name
        choices = self.fields['position'].choices

        # Skip the empty label if present, sort the rest
        if choices and choices[0][0] == '':
            empty = [choices[0]]
            sorted_choices = sorted(choices[1:], key=lambda x: x[1])
            self.fields['position'].choices = empty + sorted_choices
        else:
            self.fields['position'].choices = sorted(choices, key=lambda x: x[1])