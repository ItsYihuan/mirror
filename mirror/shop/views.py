from django.shortcuts import render
from .forms import ClothseModelForm,ClothseDataModelForm
from .models import Cloth,Cloth_data
# Create your views here.
def home(request):
    return render(request, 'shop/home_page.html',{})

def cloth_img(request):
    cloths = Cloth.objects.all()
    print(type(cloths))
    form = ClothseModelForm()
    if request.method == "POST":
        form = ClothseModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cloths=cloths[len(cloths)-1]
    context = {
        'shop': cloths,
        'form': form
    }
    return render(request, 'shop/cloth_img.html', context)
    
def cloth_data(request):
    form = ClothseDataModelForm()
    if request.method == "POST":
        form = ClothseDataModelForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {
        'form': form
    }
    return render(request,'shop/cloth_data.html',context)