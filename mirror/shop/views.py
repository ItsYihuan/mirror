from asyncio.windows_events import NULL
from django.shortcuts import render
from .forms import ClothesModelForm,ClothesDataModelForm,ClothesSelectModelForm
from .models import Cloth,Cloth_data
import cv2
# Create your views here.
def home(request):
    return render(request, 'home_page.html',{})

def cloth_img(request):
    cloths = Cloth.objects.all()
    form = ClothesModelForm()
    if request.method == "POST":
        form = ClothesModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("save_id:",len(cloths))
            if(len(cloths)>=1):
                cloths=cloths[len(cloths)-1]
            else:
                cloths=cloths[0]
    context = {
        'shop': cloths,
        'form': form
    }
    return render(request, 'cloth_img.html', context)
    
def cloth_data(request):
    form = ClothesDataModelForm()
    
    cloths = Cloth.objects.all()
    if(len(cloths)>=1):
        cloths=cloths[len(cloths)-1]
    else:
        cloths=cloths[0]
    print(cloths.image)
    print("media/"+str(cloths.image))
    cloth_img = cv2.imread("media/"+str(cloths.image))
    if request.method == "POST":
        form = ClothesDataModelForm(request.POST)
        #print(request.POST['image_ID'])
        if form.is_valid():
            print('yes')
            cloth_info=form.cleaned_data
            cloth_info['image_ID']=cloths.id
            print(cloth_info)
            Cloth_data.objects.create(**cloth_info)
            #form.save()

    context = {
        'shop':cloths,
        'form': form
    }
    context['form'].fields['image_ID'].initial=cloths.id
    return render(request,'cloth_data.html',context)

def user_selectCloth(request):
    cloth = Cloth.objects.all()
    context = {
        'shop': cloth,
    }
    return render(request, 'user_selectCloth.html', context)

def user_show(request):
    cloth = NULL
    cloth_data=NULL
    if request.method == "POST":
        print(request.POST['cloth'])
        cloth=Cloth.objects.get(id=request.POST['cloth'])
        cloth_data=Cloth_data.objects.get(image_ID=request.POST['cloth'])
        print(cloth_data)
    context = {
        'shop':cloth,
        'text':cloth_data
    }
    return render(request, 'user_show.html', context)


