
from django.shortcuts import render

# Create your views here.
def demo1(request):
    return render(request, "home.html")
def operations(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res = x+y
    sub = x-y
    mul = x*y
    div = x/y

    return render(request, "result.html",
                  {'addition': res, 'subtraction': sub, 'product': mul, 'division': div})

