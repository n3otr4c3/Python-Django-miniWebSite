from django.shortcuts import render
from datetime import datetime


def index(request):
    return render(request, "docBlog/index.html", context={"date": datetime.today()})
