from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Post

# Create your views here.
def index(request):
    return render(request, "blog/index.html", {
        "posts_authors":  User.objects.all()
    })

def users(request):
    return