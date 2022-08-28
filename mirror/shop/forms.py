from django import forms
from .models import Cloth,Cloth_data

class ClothesModelForm(forms.ModelForm):
    class Meta:
        model = Cloth
        fields=('image',)
        widgets={
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }
class ClothesDataModelForm(forms.ModelForm):
   
    class Meta:
        model = Cloth_data
        fields=('image_ID','shoulder_s','shoulder_m','shoulder_l','shoulder_xl','shoulder_2l',
        'chest_s','chest_m','chest_l','chest_xl','chest_2l',
        'length_s','length_m','length_l','length_xl','length_2l')
        widgets={
            'image_ID':forms.NumberInput(attrs={'value':"{{shop.id}}"}),
            'shoulder_s':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            'shoulder_m':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            'shoulder_l':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            'shoulder_xl':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            'shoulder_2l':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            
            'chest_s':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            'chest_m':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            'chest_l':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            'chest_xl':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            'chest_2l':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            
            'length_s':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            'length_m':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            'length_l':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            'length_xl':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
            'length_2l':forms.NumberInput(attrs={'class': 'form-control','placeholder':'cm','min':"1", 'max':"100"}),
        }
class ClothesSelectModelForm(forms.Form):
    select=forms.ChoiceField(widget=forms.RadioSelect)
