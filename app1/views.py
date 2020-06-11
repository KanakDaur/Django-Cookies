from django.shortcuts import render

# Create your views here.
def name_form(request):
    return render(request,'app1/name.html')

def age_form(request):
    name = request.GET['uname'] # to get the name as cookie (getting cookie)
    response = render(request,'app1/age.html')
    response.set_cookie('name',name) # to set the name as cookie (setting cookie)
    return response

def email_form(request):
    age = request.GET['uage']
    response = render(request,'app1/email.html')
    response.set_cookie('age',age)
    return response

def all_details(request):
    email = request.GET['uemail']
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    my_dict = {'name':name,'age':age,'email':email}
    return render(request,'app1/allinfo.html',context = my_dict)
