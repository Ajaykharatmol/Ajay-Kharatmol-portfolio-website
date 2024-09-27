from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")
    #return HttpResponse("Hello, world. You're at the polls index.")
'''
def showalldepts(request):
    #depts = Dept.objects.all()
    #return render(request,"showalldepts.html",{'depts':depts})
    return render(request,"showalldepts.html")

'''

def about(request):
    return render(request,"about_me.html")

def portfolio(request):
    return render(request,"my_portfolio.html")

def contact(request):
    return render(request,"my_contact.html")