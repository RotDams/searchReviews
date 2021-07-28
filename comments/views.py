# Create your views here.
from django.shortcuts import render

from .models import Comment


def search_view(request):
    obj = Comment.objects.get(id=1)
    context = {
        'obj': obj
    }
    return render(request, "search/search.html", context)
