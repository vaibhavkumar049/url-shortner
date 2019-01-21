from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostUrl
from .models import UrlLink
import math

BASE = 62

UPPERCASE_OFFSET = 55
LOWERCASE_OFFSET = 61
DIGIT_OFFSET = 48

def true_ord(char):
    """
    Turns a digit [char] in character representation
    from the number system with base [BASE] into an integer.
    """
    
    if char.isdigit():
        return ord(char) - DIGIT_OFFSET
    elif 'A' <= char <= 'Z':
        return ord(char) - UPPERCASE_OFFSET
    elif 'a' <= char <= 'z':
        return ord(char) - LOWERCASE_OFFSET
    else:
        raise ValueError("%s is not a valid character" % char)
def true_chr(integer):
    """
    Turns an integer [integer] into digit in base [BASE]
    as a character representation.
    """
    if integer < 10:
        return chr(integer + DIGIT_OFFSET)
    elif 10 <= integer <= 35:
        return chr(integer + UPPERCASE_OFFSET)
    elif 36 <= integer < 62:
        return chr(integer + LOWERCASE_OFFSET)
    else:
        raise ValueError("%d is not a valid integer in the range of base %d" % (integer, BASE))

def url_list(request,pk):
    url = get_object_or_404(UrlLink,pk=pk)
    integer=pk
    if integer == 0:
        return '0'
    
    string = ""
    while integer >= 0:
        remainder = integer % BASE
        string = true_chr(remainder) + string
        # fix string startwith 0
        if integer == 0:
            break
        integer = integer//BASE   
    final_string = string[1:]
    return render(request,'core/url_detail.html',{'url':url,'fs':final_string})


def url_new(request):
    if request.method == "POST":
        form=PostUrl(request.POST) 
        if form.is_valid():
            url=form.save()
            return redirect('url_detail',pk=url.pk)
    else:
        form=PostUrl()
        return render(request,'core/url_list.html',{'form':form})

def redirect_to_website(request,key):
    int_sum = 0
    reversed_key = key[::-1]
    for idx, char in enumerate(reversed_key):
        int_sum += true_ord(char) * int(math.pow(BASE, idx))
    url=get_object_or_404(UrlLink,pk=int_sum)
    return redirect(url.website)
      
# Create your views here.
'''
redirect website me string to pk mean saturate

converting me pk to string banana hai
'''