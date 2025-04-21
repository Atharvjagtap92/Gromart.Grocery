from django.shortcuts import render ,redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    prod = Product.objects.all()
    form = ProductForm(request.POST, request.FILES)  # Ensure request.FILES is included!

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")  # Redirect after adding a product

    return render(request, "Insta_grocery/home.html", {"prod": prod, "form": form})

def update_data(request, id):
    prod = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=prod)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "insta_grocery/update_data.html", {"form": form})

def delete_data(request, id):
    prod = Product.objects.get(id=id)
    if request.method == "POST":
        prod.delete()
        return redirect("home")
    return render(request, "insta_grocery/delete_data.html", {"prod": prod})