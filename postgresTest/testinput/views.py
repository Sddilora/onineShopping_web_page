from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Owner
from .forms import ProductForm

# Create your views here.
def product_form(request):
    # Retrieve owner ID from session data
    user = request.session.get('user')
    # If owner does not exist, create a new owner
    Owner.objects.get_or_create(name=user["userinfo"]["name"], email=user["userinfo"]["email"])
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Set the owner_id attribute of the form instance before saving
            form.instance.owner_id = Owner.objects.get(name=user["userinfo"]["name"], email=user["userinfo"]["email"]).id
            messages.success(request, 'Product added successfully!')
            form.save()
            return redirect('testpages/mypage')
        else :
            messages.error(request, 'Error adding product')
            return redirect('testpages/mypage')
    else:
        # Create a new form instance with initial data if required
        initial_data = {'name': 'Product Name', 'price': 0.0} # Replace with your own initial data
        form = ProductForm(initial=initial_data)
        
    return render(request, 'form.html', {'form': form})

# def product_form(request):
    
#     # Retrieve owner ID from session data
#     user = request.session.get('user')
#     userinfo = user["userinfo"]
#     owner_id = user["userinfo"]["sub"]
#     # form["owner_id"] = owner_id
#     ProductForm["owner_id"]= owner_id
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
            
#             form.save()
#     else:
#         # initial_data = {'name': name, 'email': email}
#         form = ProductForm()
#     return render(request, 'form.html', {'form': form})
