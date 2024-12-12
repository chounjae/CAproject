from django.http import HttpResponse


app_name = 'UseapiConfig'
def start(request):
    return HttpResponse("안녕")