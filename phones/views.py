from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    catalog_phones_sorted_name = Phone.objects.order_by('name')
    catalog_phones_sorted_min = Phone.objects.order_by('price')
    catalog_phones_sorted_max = Phone.objects.order_by('-price')
    catalog_phones = Phone.objects.all()
    sort = request.GET.get('sort', '')
    if sort == 'name':
        context = {'phones': catalog_phones_sorted_name}
    elif sort == 'min_price':
        context = {'phones': catalog_phones_sorted_min}
    elif sort == 'max_price':
        context = {'phones': catalog_phones_sorted_max}
    else:
        context = {'phones': catalog_phones}

    return render(request, template, context)


def show_product(request, slug):
    phone_slug = Phone.objects.filter(slug=str(slug))
    template = 'product.html'
    context = {'phones': phone_slug}
    return render(request, template, context)
