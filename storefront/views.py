from django.http import HttpResponse

def home_page(request):
    return HttpResponse("This is Home page")