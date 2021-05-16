from django.shortcuts import render,redirect
import bcrypt
from django.contrib import messages
from .models import *
import re

def index(request):
    return render(request, 'index.html')


def regPage(request):
    return render(request, 'register.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.user_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/registerPage")
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(
                first_name=request.POST["first_name"], 
                last_name= request.POST["last_name"],
                email = request.POST["email"], 
                password=pw_hash,
                birthday = request.POST["birthday"],
                gender = request.POST["gender"],
                )
            request.session['user_id'] = new_user.id
            return redirect("/dashboard")
    return redirect("/")

def login(request):
    users_with_email = User.objects.filter(email=request.POST['email'])
    if users_with_email:
        user = users_with_email[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session["user_id"] = user.id
            return redirect("/dashboard")
    messages.error(request, "Incorrect email or password")
    return redirect("/")

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect("/")
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': this_user,
        'new_workout': Workout.objects.all(),
        'all_category': Category.objects.all(),
    }

    return render(request, "dashboard.html", context)

def logout(request):
    request.session.flush()
    return redirect("/")

def newWorkout(request):
    if 'user_id' not in request.session:
        return redirect("/")
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': this_user,
        
    }
    return render(request,"add.html",context)  

def add(request):
    if request.method == "POST":
        
        new_workout = Workout.objects.create(
            workout_date = request.POST['workout_date'],
            exercise = request.POST['exercise'],
            weight = request.POST['weight'],
            reps = request.POST['reps'],
            sets = request.POST['sets'],
            description = request.POST['description'],
            user = User.objects.get(id=request.session['user_id'])
        )
        new_workout.categories.add(Category.objects.get(category=request.POST['category']))
        new_workout.save()
    return redirect("/dashboard")

def edit(request, workout_id):
    if 'user_id' not in request.session:
        return redirect("/")
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': this_user,
        'workout': Workout.objects.get(id=workout_id)
    }

    return render(request, 'edit.html', context)

def update(request, workout_id):
    if request.method =="POST":
        update_workout = Workout.objects.get(id=workout_id)
        update_workout.category = request.POST['category']
        update_workout.workout_date = request.POST['workout_date']
        update_workout.exercise = request.POST['exercise']
        update_workout.weight = request.POST['weight']
        update_workout.reps = request.POST['reps']
        update_workout.sets = request.POST['sets']
        update_workout.description = request.POST['description']
        update_workout.save()
    return redirect("/dashboard")

def delete(request, workout_id):
    if 'user_id' not in request.session:
        return redirect("/")
    delete_workout = Workout.objects.get(id=workout_id)
    delete_workout.delete()
    return redirect("/dashboard")

def category(request, category):
    if 'user_id' not in request.session:
        return redirect("/")
    this_user = User.objects.get(id=request.session['user_id'])
    this_category = Category.objects.get(category= category)

    context = {
        'user': this_user,
        'new_workout': Workout.objects.all(),
        'all_category': Category.objects.all(),
        'category': this_category
    }  

    return render(request, "dashboard.html/", context)