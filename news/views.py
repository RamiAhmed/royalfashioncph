from django.shortcuts import render, get_object_or_404

from news.models import NewsPost

# Create your views here.
def index(request):
    #news_posts = get_list_or_404(NewsPost, active=True)
    news_posts = NewsPost.objects.all().filter(active=True)
    
    return render(request, 'news/news_index.html', {'news_posts': news_posts})

#def year(request, year):
#    pass

#def month(request, year, month):
#    pass

#def day(request, year, month, day):
#    pass

def post(request, year, month, day, news_slug):
    news_post = get_object_or_404(NewsPost, slug=news_slug)
    
    return render(request, 'news/news_post.html', {'news': news_post})