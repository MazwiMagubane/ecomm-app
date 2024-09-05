from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product_objects = Products.objects.all()

    # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # paginator code
    paginator = Paginator(product_objects, 12)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects':product_objects})

def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object':product_object})

def checkout(request):

    if request.method == 'POST':
        items = request.POST.get('items', '')
        firstname = request.POST.get('inputFirstname4','')
        lastname = request.POST.get('inputLastname4','')
        email = request.POST.get('inputEmail4','')
        address = request.POST.get('inputAddress','')
        address2 = request.POST.get('inputAddress2','')
        city = request.POST.get('inputCity','')
        province = request.POST.get('inputProvince','')
        postcode = request.POST.get('inputPostcode','')
        print(firstname, lastname, email, address, address2, city, province, postcode)

        order = Order(items=items, firstname=firstname, lastname=lastname, email=email, address=address, address2=address2, city=city, province=province, postcode=postcode)
        order.save()

    return render(request, 'shop/checkout.html')
