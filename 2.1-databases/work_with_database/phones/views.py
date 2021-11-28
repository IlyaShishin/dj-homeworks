from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    if sort:
        if sort == 'name':
            context = {
                'phones': Phone.objects.all().order_by('name')
            }
            return render(request, template, context)
        elif sort == 'min_price':
            context = {
                'phones': Phone.objects.all().order_by('price')
            }
            return render(request, template, context)
        elif sort == 'max_price':
            context = {
                'phones': Phone.objects.all().order_by('-price')
            }
            return render(request, template, context)
    else:
        context = {
            'phones': Phone.objects.all
        }
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }

    return render(request, template, context)
