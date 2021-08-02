from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm



def all_products(request):
    """Shows and displays all products."""
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    
    if request.GET:
        
        # Handles sorting by price, rating etc...
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
                
        # Handles categories        
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        
        # Handles Searches
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter a search query!')
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            
    
    current_sorting = f'{sort}_{direction}'
    
    product_context = {
        'products' : products,
        'search_term' : query,
        'current_categories' : categories,
        'current_sorting' : current_sorting,
    }
    
    return render(request, 'products/products.html', product_context)

def product_detail(request, product_id):
    """Displays individual products."""
    product = get_object_or_404(Product, pk=product_id)
    
    product_context = {
        'product' : product,
    }
    
    return render(request, 'products/product_detail.html', product_context)

@login_required
def add_product(request):
    """To quickly add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Nope! Only the store owner can do that')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product! Please check all details and try again.')
    else:
        form = ProductForm()
    
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form' : form,
    }
    
    return render(request, template, context)

@login_required      
def edit_product(request, product_id):
    """Edit product in store"""
    if not request.user.is_superuser:
        messages.error(request, 'Nope! Only the store owner can do that')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product, please check all details and try again.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
    
    template = 'products/edit_product.html'
    context = {
        'form' : form,
        'product' : product,
    }
    
    return render(request, template, context)   

@login_required    
def delete_product(request, product_id):
    """ Delete store product """
    if not request.user.is_superuser:
        messages.error(request, 'Nope! Only the store owner can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product Deleted')
    return redirect(reverse('products'))

