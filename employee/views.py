from django.shortcuts import render


def employee_list(request):
    return render(request, 'employee/employee_list.html', {})


def employee_form(request):
    return render(request, 'employee/employee_form.html', {})


def employee_delete(request):
    pass
