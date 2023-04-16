from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from .models import Product
# from .forms import ProductForm

# Create your views here.
def mypage(request):
    return render(request, "mypage.html", context={ "session": request.session.get("user") })

# def product_list(request):
#     user_info = request.session.get("user")
#     products = Product.objects.filter(user=request.user)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.user = request.user
#             product.save()
#     else:
#         form = ProductForm()
#     context = {
#         'form': form,
#         'products': products,
#         'user_info': user_info
#     }
#     return render(request, 'product_list.html', context)

