from django.shortcuts import render

# Create your views here.
from .models import Task

def home(request):
	a = {"ENGLISH":87,"MATHS":94,"SCIENCE":88}
	return render(request,'index.html',{'subjects':a})


def alltasks(request):
	t = Task.objects.all()
	return render(request,"alltasks.html",{'alltasks':t})