from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Gift, Claim
from .forms import ClaimForm
# Create your views here.
def registry(request):
    gifts = Gift.objects.all()
    if 'sort' in request.GET:
        sort = request.GET['sort']
        match sort:
            case 'price_low':
                gifts = gifts.order_by('price')
            case 'price_high':
                gifts = gifts.order_by('-price')
            case 'name':
                gifts = gifts.order_by('name')

    if 'filter' in request.GET:
        filter =  request.GET['filter']
        match filter:
            case 'donation':
                gifts = gifts.filter(price_range_low__ne=None)
            case 'gift':
                gifts = gifts.filter(price_range_low__eq=None)
                
    giftinfo = ([(g, 
        len(Claim.objects.filter(claimed_gift=g, visible=True)),
        sum([x.amount for x in Claim.objects.filter(claimed_gift=g, visible=True) if x.amount]),)
        for g in gifts])
    context = {'giftinfo': giftinfo}
    return render(request, 'registry/registry.html', context)

def gift_page(request, slug):
    gift_obj = get_object_or_404(Gift, slug=slug)
    claims = Claim.objects.filter(claimed_gift=gift_obj, visible=True)
    total = sum([x.amount for x in claims if x.amount])
    context = {'gift': gift_obj, 'claims': claims, 'total':total}
    return render(request, 'registry/gift_page.html', context)

def claim_gift(request, slug):
    if request.method == 'POST':
        print(request.POST)
        form = ClaimForm(request.POST)

        if form.is_valid():
            gift = get_object_or_404(Gift, slug=slug)
            claim = Claim()
            claim.name = form['name'].value()
            if form['amount'].value():
                claim.amount = form['amount'].value()
            else:
                claim.amount = gift.price
            claim.claimed_gift = gift
            supercede = Claim.objects.filter(name=claim.name, claimed_gift=gift)
            if len(supercede) > 0:
                for x in supercede:
                    x.visible = False
                    x.save()
            claim.save()
            return HttpResponseRedirect(reverse("registry:gift_page",args=[slug]))
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse("registry:gift_page",args=[slug]))
    return HttpResponseRedirect(reverse("registry:gift_page",args=[slug]))