from django.shortcuts import render, HttpResponse, redirect
from models import User
def index(request):
    context = {
    'user': User.objects.all()
    }
    return render(request, 'REST_users/index.html', context)
def new(request):
    return render(request, 'REST_users/new.html')
def create(request):
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], age = request.POST['age'])
    return redirect('/users')
def info(request, user_id):
    if request.method == 'POST':
        a = User.objects.get(id = user_id)
        a.first_name = request.POST['first_name']
        a.last_name = request.POST['last_name']
        a.age = request.POST['age']
        a.save()
        return redirect('/users/' + user_id)
    else:
        the_user = User.objects.get(id = user_id)
        context = {
        'user': the_user
        }
        return render(request, 'REST_users/info.html', context)
def destroy(request, user_id):
    User.objects.get(id = user_id).delete()
    return redirect('/users')
def edit(request, user_id):
    the_user = User.objects.get(id = user_id)
    context = {
    'user': the_user
    }
    return render(request, 'REST_users/edit.html', context)
