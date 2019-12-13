from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


def employee_list(request):
    context = {
        'list': Employee.objects.all()
    }
    return render(request, 'employee/employee_list.html', context)


def employee_form(request, id=None):
    # form = EmployeeForm(request.POST or None)
    if request.method == 'GET':
        if id is None:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        context = {
            'form': form
        }
        return render(request, 'employee/employee_form.html', context)

    elif request.method == 'POST':
        if id is None:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        context = {
            'form': form
        }
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('list')
        return render(request, 'employee/employee_form.html', context)


def employee_delete(request):
    pass
