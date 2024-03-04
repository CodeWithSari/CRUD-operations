from django.shortcuts import render, redirect
from django.http import HttpRequest

from .forms import CreateUserForm, LoginForm, AddStudentForm, UpdateStudentForm

from django.contrib import messages
from .models import StudentRegister

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
# Create your views here

def home(request):
    return render(request, 'index.html')



def admin_login(request):
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form': form}

    return render(request, 'admin_login.html', context=context)


def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("admin_login")

    context = {'form': form}

    return render(request, 'register.html', context=context)

def admin_logout(request):
    auth.logout(request)
    messages.success(request, "Logout successfully!")
    return redirect("admin_login")



# - Dashboard

@login_required(login_url='admin_login')
def dashboard(request):

    my_students = StudentRegister.objects.all()

    context = {'students': my_students}

    return render(request, 'dashboard.html', context=context)


# - Create a record

@login_required(login_url='admin_login')
def add_student(request):

    form = AddStudentForm()

    if request.method == "POST":

        form = AddStudentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "New Student Registered  !")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'add_student.html', context=context)



# - Update a record

@login_required(login_url='admin_login')
def update_student(request, pk):

    student = StudentRegister.objects.get(id=pk)
    form = UpdateStudentForm(instance=student)
    if request.method == 'POST':

        form = UpdateStudentForm(request.POST, instance=student)

        if form.is_valid():

            form.save()

            messages.success(request, "student details updated!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'update_student.html', context=context)


# - Read / View a singular record

@login_required(login_url='admin_login')
def singular_student(request, pk):

    all_students = StudentRegister.objects.get(id=pk)

    context = {'student': all_students}

    return render(request, 'view_student.html', context=context)


# - Delete a record

@login_required(login_url='admin_login')
def delete_student(request, pk):

   student = StudentRegister.objects.get(id=pk)
   student.delete()
   messages.success(request, "student details deleted!")
   return redirect("dashboard")




