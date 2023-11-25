from django import forms 
from .models import Item

INPUT_CLASS='w-full px-6 py-3 rounded-xl'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','image','price')
        widgets={
            'category':forms.Select(attrs={
                'class':INPUT_CLASS
            }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASS
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASS
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASS
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASS
            }),
           
            
            
        }
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','description','image','price','is_sold')
        widgets={
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASS
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASS
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASS
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASS
            }),
           
            
            
        }
    
