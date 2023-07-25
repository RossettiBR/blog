from blog.models import Page


def blog(request):
    blog = Page.objects.order_by('-id').first()
    return {
        'blog':  blog,
    }
