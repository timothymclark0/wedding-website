from django.shortcuts import render
from .models import Photo
from django.http import Http404 

# Create your views here.
def savethedate(request):
    photos = Photo.objects.all()
    return render(request,'savedate/savedate.html', context = {'gallery': photos})


def notion_page(request, page):
    pages = {'faq': """<iframe src="https://notjessytang.notion.site/ebd/219c2a181f0280efacfac946959716fd" width="100%" height="900" frameborder="0" allowfullscreen />""",
             'gallery': """<iframe src="https://notjessytang.notion.site/ebd/219c2a181f02809bb911d9d22f373e3a" width="100%" height="900" frameborder="0" allowfullscreen />""",
             'travel': """<iframe src="https://notjessytang.notion.site/ebd/219c2a181f0280ff97d2c8430660ce2b" width="100%" height="900" frameborder="0" allowfullscreen />""",
             'details': """<iframe src="https://notjessytang.notion.site/ebd/219c2a181f028057a6cad4c09dde51c0" width="100%" height="900" frameborder="0" allowfullscreen />""",
             'rsvp': """<iframe src="https://iu.co1.qualtrics.com/jfe/form/SV_3BE0DYMaghtLUmq" width="100%" height=900" frameborder="0" allowfullscreen />""",}
    try:
        html = pages[page]
    except KeyError:
        raise Http404()
    return render(request, 'savedate/notion.html', context = {'html':html, 'page':page})

def registry(request):
    return render(request,'savedate/registry.html')
