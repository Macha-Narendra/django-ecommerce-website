from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'store/product_list.html', {'products': products})


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect('store:product_list')
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form})
