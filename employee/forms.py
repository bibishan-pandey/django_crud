from django.forms import ModelForm
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'emp_code', 'mobile', 'position']
        labels = {
            'full_name': 'Full Name',
            'emp_code': 'Employee Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = '----SELECT----'
