from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    print(request.session.get("first_name", "Unknown"))
    # request.session
    context = {
        "title":"Hello World!",
        
        
    }
    if request.user.is_authenticated():
        context["premium_content"] = "Premium view for authenticated user"
    return render(request, "home_page.html", context)



def test_page(request):
    return render(request, "test.html")



