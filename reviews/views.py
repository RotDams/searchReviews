from django.db.models import Q
from django.shortcuts import render

from .models import Review


def search_view(request):
    all_reviews = Review.objects.all()
    word = request.POST['searchname']

    if request.method == "POST" and word:
        all_reviews = all_reviews.filter(Q(title__contains=word) | Q(body__contains=word))

    context = {
        'all_reviews': all_reviews,
        'word_researched': word,
    }

    return render(request, "search/search.html", context)
