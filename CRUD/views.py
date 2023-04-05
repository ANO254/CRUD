from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student


def Home(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, 'index.html', context)


#def index(request):
 #   return render(request, 'index.html')


#def edit(request):
 #   return render(request, 'edit.html')


#


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, 'index.html')


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST('email')
        age = request.POST('age')
        gender = request.POST('gender')

        edit = Student.objects.get(id=id)
        edit.name = name
        edit.emai = email
        edit.age = age
        edit.gender = gender
        edit.save()
        return redirect("/")
    d = Student.object.get(id=id)
    context = {"d": d}

    return render(request, 'edit.html', context)


def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, 'index.html', )


def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        myuser = authenticate(username=username, password=password)

        if myuser is not None:
            login(request, myuser)
            return redirect("/")
        else:
            return redirect('/login')

    return render()


def handlelogout(request):
    logout(request)
    return render('/signup')


def handlesignup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username,password)
        myuser = User.objects.create_user(username,password)
        myuser.save()
    return render(request, "signup.html")
