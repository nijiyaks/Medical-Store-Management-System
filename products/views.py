from django.shortcuts import render
from django.core.paginator import Paginator
from .form import MedicineForm
from .form import Product
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product
from django.shortcuts import get_object_or_404, render, redirect

def search_products(request):
    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(name__istartswith=query)
    else:
        products = Product.objects.all()
    data = [{'id': product.id,'name': product.name, 'available_stock': product.available_stock, 'description': product.description,'time': product.time} for product in products]  
    return JsonResponse(data ,safe=False)
@login_required
def live_search(request):
     return render(request, 'retrieve.html')



@login_required(login_url='/login/')

def product_create(request):
    current_user = request.user

    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            if Product.objects.filter(user=current_user).count() >= 5:
                error_message = "You have already added the maximum number of medicines."
                return render(request, 'create.html', {'form': form, 'error_message': error_message})

            product = form.save(commit=False)                                                                       
            product.user = current_user  # Associate the product with the current user
            product.save()
            return redirect('page_list')
    else:
        form = MedicineForm()    
        return render(request, 'create.html', {'form':form})
    


def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('page_list')
    else:
        form =MedicineForm(instance=product)           
    return render(request, 'update.html', {'product': product,'form': form})




def product_delete(request,pk):
    product=Product.objects.get(pk=pk)  
    if request.method == 'POST':
        product.delete()
        return redirect('page_list')
    
    return render(request,'retrieve.html',{'product':product})

@login_required(login_url='/login/')
def listing(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 3)  # Set the number of items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'retrieve.html', {'page_obj': page_obj})

