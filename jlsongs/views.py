from django.shortcuts import render

def index(request):
    return render(request, "jlsongs/templates/jlsongs/index.html")