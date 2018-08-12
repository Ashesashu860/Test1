from django.http import HttpResponse

def index(request):
    return HttpResponse("<H1>This is the homepage</H1>")