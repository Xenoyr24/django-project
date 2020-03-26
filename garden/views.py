from django.shortcuts import render
from garden.forms import ContactForm

# Create your views here.
def about_page(request):
    context = {
        "title":"About Page",
    }
    return render(request, "garden/about_us.html", context)
    
def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
            "title":"Contact",
            "content":" Welcome to the contact page.",
            "form": contact_form,
            #"brand": "new Brand Name"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        # if request.method == "POST":
        # print(request.POST)
        # print(request.POST.get('fullname'))
        # print(request.POST.get('email'))
        # print(request.POST.get('content'))
    return render(request, "garden/contact_us.html", context)


def testimonial_page(request):
    return render(request, "garden/testimonial.html")


def gallery_page(request):
    return render(request, "garden/gallery.html")


def services_page(request):
    return render(request, "garden/services.html")


def estimation_tool(request):
    return render(request, "garden/tool.html")
