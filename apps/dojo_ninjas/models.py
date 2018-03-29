# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def isValidRegistration(self, userInfo, request):
        flag = True
        if not userInfo['first_name'].isalpha():
            messages.warning(request, 'First name should only contain alpha character(s)')
            flag = False
        if len(userInfo['first_name']) < 2:
            messages.warning(request, 'First name should be atleast 2 characters.')
            flag = False
        if not userInfo['last_name'].isalpha():
            messages.warning(request, 'Last name contains non-alpha character(s)')
            flag = False
        if len(userInfo['last_name']) < 2:
            messages.warning(request, 'Last name should be atleast 2 characters.')
            flag = False
        if not EMAIL_REGEX.match(userInfo['email']):
            messages.warning(request, 'Email is invalid')
            flag = False
        if len(userInfo['password']) < 7:
            messages.warning(request, 'Password should be atleast 7 characters')
            flag = False
        if userInfo['password'] != userInfo['confirm_password']:
            messages.warning(request, 'Password match not confirmed.')
            flag = False
        if User.objects.filter(email = userInfo['email']):
			messages.error(request, "This email already exists in database.")
			flag = False

        if flag == True:
    
            hashed = bcrypt.hashpw(userInfo['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name = userInfo['first_name'], last_name = userInfo['last_name'], email = userInfo['email'], password = hashed)
          #  User.objects.last().id
            request.session["user_id"] = User.objects.get(email = userInfo['email']).id
            messages.success(request, "Success! Welcome, " + userInfo['first_name'] + str(User.objects.last().id) + "!")        
        return flag

    def UserExistsLogin(self, userInfo, request):
        flag = True
        if User.objects.filter(email = userInfo['email']):
            hashed = User.objects.get(email = userInfo['email']).password
            hashed = hashed.encode('utf-8')
            password = userInfo['password']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                request.session["user_id"] = User.objects.get(email = userInfo['email']).id
                messages.success(request, "Welcome: " + User.objects.get(email = userInfo['email']).first_name +" "+str(request.session['user_id']) +" "+ str(User.objects.get(email = userInfo['email']).id) +"!")
                
                flag = True
            else:
                messages.warning(request, "Invalid password.")
                flag = False
        else:
            messages.warning(request, "Your email is invalid.")
            flag = False
        return flag

class ItemManager(models.Manager):
    def isValid(self, itemInfo, request):
        flag = True
        print Item.objects.first()
       
       # if len(itemInfo['item']) < 2:
        #    messages.warning(request, 'First name should be atleast 2 characters.')
        #    flag = False
       # if not itemInfo['desc'].isalpha():
        #    messages.warning(request, 'Last name contains non-alpha character(s)')
        #    flag = False
        
        #if flag == True:
    
        #Item.objects.create(item = itemInfo['item'], desc = itemInfo['desc'], items = User.objects.get(id = 1))  
         #   messages.success(request, "Successfully added : , " + str(Item.objects.last().item) + "!")        
        return flag
    

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add = True)
    userManager = UserManager()
    objects = models.Manager()

class Item(models.Model):
    item = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="items")
    itemManager = ItemManager()
    objects = models.Manager()


