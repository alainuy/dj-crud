from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

#list all employees
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', context)

#create / edit employee
def employee_form(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request, 'employee_register/employee_form.html', {'form': form})
    # return render(request, 'employee_register/employee_form.html', {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/employee')



#delete employee
def employee_delete(request):
    return

