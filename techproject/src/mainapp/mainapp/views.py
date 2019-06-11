from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # user = request.user
    products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    context = {
        'products' : products,
        'numbers' : [1,3,5,7,9,2,4,6,8,10],
    }

    return render(request, "home.html", context)

    # return HttpResponse(f"<h1>Welcome {request.user}!</h1>")