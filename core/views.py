from django.shortcuts import render
from .forms import PostUrl
# Create your views here.

# def url_list(request):
#     return render(request,'core/url_list.html',{})

def url_new(request):
    form=PostUrl()
    return render(request,'core/url_list.html',{'form':form})

