from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "minutes/index.html", {
        "current_hour": datetime.now().hour,
        "current_minute": datetime.now().minute,
        "current_second": datetime.now().second,
        "minute": datetime.now().minute < 30
    })