from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dic ={'insert_me':" hello i am from tunisia "}
    return render (request,'index.html',context=my_dic )

def help(request): 
    help_dict={'help_insert': "HELP PAGE "}
    return render (request , 'appClient/help.html',context=help_dict)