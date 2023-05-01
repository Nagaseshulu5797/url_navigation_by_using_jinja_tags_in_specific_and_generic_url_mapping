from django.shortcuts import render

# Create your views here.
def generic_url(request):
    d={'name':'seshulu','age':21}
    return render(request,'generic_url.html',d)