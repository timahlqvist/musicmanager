from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Welcome to Music Manager</h2><h4>Here you can manage your record collection and your mixtapes for free</h4>')