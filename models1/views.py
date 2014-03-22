from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
from django.forms.models import model_to_dict
from models1.models import User
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def get_user(request):
	responses = {"errorCode":1001, "message": "User matching query does not exist."}
	if request.GET:
		try:
			get_valid_user = User.objects.get(user_name=request.GET['username'])
			if request.GET['username']:				
				responses = {"errorCode":1000, "message": "no value", "data" : model_to_dict(get_valid_user)}
				return HttpResponse(dumps(responses), content_type="application/json")
		except Exception as e:            
			responses = {"errorCode":1001, "message": str(e.message)}
			return HttpResponse(dumps(responses), content_type="application/json")
	return HttpResponse(dumps(responses), content_type="application/json")


def get_all_users(request):
	try:
		get_all_user = User.objects.all()
		get_all_user = serializers.serialize('python', get_all_user)
		get_all_user = [d['fields'] for d in get_all_user]		
		responses = {"errorCode":1000, "message": "no value", "data" : get_all_user}
		return HttpResponse(dumps(responses), content_type="application/json")
	except Exception as e:            
		responses = {"errorCode":1001, "message": str(e.message)}
		return HttpResponse(dumps(responses), content_type="application/json")


@csrf_exempt
def add_user(request):
	responses = {"errorCode":1002, "message": "No value"}
	if request.POST :
		try:        
			if request.POST['user'] is not None and request.POST['pass'] is not None and request.POST['email'] is not None :
				check_user_exist = User.objects.filter(user_name = request.POST['user']).values()            

				if check_user_exist:
					responses = {"errorCode":1001, "message": "User Already exist"}
				else :                                
				   p = User.objects.create(user_name=request.POST['user'], user_password =request.POST['pass'], user_email=request.POST['email'])      
				   responses = {"errorCode":1000, "message": "Success Add User"}   
				return HttpResponse(dumps(responses), content_type="application/json")
		except Exception as e:                
			return HttpResponse(dumps(responses), content_type="application/json")
	return HttpResponse(dumps(responses), content_type="application/json")

@csrf_exempt
def update_user_email(request):
	responses = {"errorCode":1002, "message": "No value"}
	if request.POST :
		try:        
			if request.POST['user'] is not None :
				user_update = User.objects.get(user_name = request.POST['user'])
				user_update.user_email = request.POST['email']
				user_update.save()
				responses = {"errorCode":1000, "message": "Success Update"}   
				return HttpResponse(dumps(responses), content_type="application/json")
		except Exception as e:                
			return HttpResponse(dumps(str(e.message)), content_type="application/json")
	return HttpResponse(dumps(responses), content_type="application/json")

@csrf_exempt
def delete_user(request):
	responses = {"errorCode":1002, "message": "No value"}
	if request.POST :
		try:        
			if request.POST['user'] is not None :
				user_update = User.objects.get(user_name = request.POST['user'])
				user_update.delete()
				responses = {"errorCode":1000, "message": "Success Delete"}   
				return HttpResponse(dumps(responses), content_type="application/json")
		except Exception as e:                
			return HttpResponse(dumps(str(e.message)), content_type="application/json")
	return HttpResponse(dumps(responses), content_type="application/json")	

                


