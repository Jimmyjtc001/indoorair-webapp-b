from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.models import User # STEP 1: Import the user0
def login_page(request):
  user = request.user
  context = {
      'user': user,
  }
  return render(request, "gateway/login.html", context)
def register_page(request):
  user = request.user
  context = {
      'user': user,
  }
  return render(request, "gateway/register.html", context)

def register_success_page(request):
  return render(request, "gateway/register_success.html", {})

def post_login_api(request):
   username = request.POST.get("username")
   password = request.POST.get("password")
   print("For debugging purposes", username, password)
   try:
       user = authenticate(username=username, password=password)
       if user:
           print("PRE-LOGIN", user.get_full_name())
           login(request, user)
           print("POST-LOGIN", user.get_full_name())
           return JsonResponse({
                "was_successful": True,
                "reason": None,
           })
       else:
           return JsonResponse({
                "was_successful": False,
                "reason": "Sorry, You Cannot log in, username or password is wrong.",
           })
   except Exception as e:
       print(e)
       return JsonResponse({
            "was_successful": False,
            "reason": "Sorry, You Cannot log in, username or password is wrong.",
       })

def post_register_api(request):

  first_name = request.POST.get("first_name")
  last_name = request.POST.get("last_name")
  username = request.POST.get("username")
  email = request.POST.get("email")
  password = request.POST.get("password")
  print(first_name, last_name, username, email, password)
  try:
      user = User.objects.create_user(username, email, password)
      user.last_name = last_name
      user.first_name = first_name
      user.save()
      return JsonResponse({
           "was_registered": True,

      })
  except Exception as e:
      return JsonResponse({
           "was_registered": False,
           "reason": str(e)
      })

def post_logout_api(request):
    logout(request)
    return JsonResponse({
         "was_successful": True,
         "reason": None,
    })
