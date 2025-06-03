from django import template
from posts.models import Post

register = template.Library()


@register.inclusion_tag('articles.html')  # -> It was for Testing // I have to make new .html page
def show_articles():
    articles = Post.objects.all()
    return {'articles': articles}

# I have to load 'my_tag' in html and then wherever I want to use {% show_article %}
