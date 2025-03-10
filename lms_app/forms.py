from django import forms 
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
       model = Category
       fields = ['name']
       widgets = {
           'name' : forms.TextInput(attrs={'class':'form-control'})
       }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'auther',
            'photo_book',
            'photo_auther',
            'pages',
            'price',
            'rental_price_day',
            'rental_period',
            'total_rental',
            'status',
            'category',
        ]

        widgets ={
            'title' : forms.TextInput(attrs={'class':'form-control col-6'}),
            'auther' : forms.TextInput(attrs={'class':'form-control col-6'}),
            'photo_book' : forms.FileInput(attrs={'class':'form-control col-6'}),
            'photo_auther' : forms.FileInput(attrs={'class':'form-control col-6'}),
            'pages' : forms.NumberInput(attrs={'class':'form-control col-6'}),
            'price' : forms.NumberInput(attrs={'class':'form-control col-6'}),
            'rental_price_day' : forms.NumberInput(attrs={'class':'form-control col-6', 'id':'rentalprice'}),
            'rental_period' : forms.NumberInput(attrs={'class':'form-control col-6', 'id':'rentaldays'}),
            'total_rental' : forms.NumberInput(attrs={'class':'form-control col-6', 'id':'totalrental'}),
            'status' : forms.Select(attrs={'class':'form-control col-6'}),
            'category' : forms.Select(attrs={'class':'form-control col-6'}),


        } 