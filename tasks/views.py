from django.shortcuts import render

# Create your views here.


def home(request):
	a = {"ENGLISH":87,"MATHS":94,"SCIENCE":88}
	return render(request,'index.html',{'subjects':a})