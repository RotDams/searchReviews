from django.db.models import Q
from django.shortcuts import render

from .models import Comment


def search_view(request):
    all_comments = Comment.objects.all()
    word = request.POST['searchname']

    if request.method == "POST" and word:
        all_comments = all_comments.filter(Q(title__contains=word) | Q(body__contains=word))

    context = {
        'all_comments': all_comments,
        'word_researched': word,
    }

    return render(request, "search/search.html", context)
