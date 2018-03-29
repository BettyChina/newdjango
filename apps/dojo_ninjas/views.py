
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .models import Item
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request, 'dojo_ninjas/index.html')

def register(request):
    if User.userManager.isValidRegistration(request.POST, request):
        flag = True
        return redirect (reverse('success'))
    else:
        flag = False
        return redirect(reverse('index'))

def success(request):
    Item.objects.filter(id = request.session['user_id'])

    context = { "users": User.objects.all(), "items" : Item.objects.all(), 
    "myitems" : Item.objects.filter(id = request.session['user_id'])
   
    }

    return render(request, 'dojo_ninjas/success.html', context)

def login(request):
    if User.userManager.UserExistsLogin(request.POST, request):
        flag = True
        return redirect (reverse('success'))
    else:
        flag = False
        return redirect (reverse('index'))

def create(request):
    if Item.itemManager.isValid(request.POST, request):
      if request.method == "POST":   
        this_user = User.objects.get(id=request.session['user_id'])
        Item.objects.create(item= request.POST['quote'], user=this_user)
        flag = True
        #this_user = User.objects.get(id=1)
        #Item.objects.create(item="Quote3", user=this_user)
       # Item.objects.create(item = itemInfo['item'], desc = itemInfo['desc'], items = User.objects.get(id = 1)) 
        return redirect (reverse('success'))
    else:
        flag = False
        return redirect(reverse('index'))

def addtolist(request):
    if request.method == "POST":   
        this_user = User.objects.get(id=request.session['user_id'])
        Item.objects.create(item= request.POST['quote'], user=this_user)
  
       # Item.objects.create(item = itemInfo['item'], desc = itemInfo['desc'], items = User.objects.get(id = 1)) 
        return redirect (reverse('success'))
    else:
        flag = False
        return redirect(reverse('create'))



def update(request):
    if request.method == "POST": 
        this_user = User.objects.get(id=request.session['user_id'])
        Item.objects.create(item= request.POST['quote'], user=this_user)
  
       # Item.objects.create(item = itemInfo['item'], desc = itemInfo['desc'], items = User.objects.get(id = 1)) 
        return redirect (reverse('success'))
    else:
        flag = False
        return redirect(reverse('create'))

def logout(request):
    request.session.flush()
    return render(request, 'dojo_ninjas/index.html')