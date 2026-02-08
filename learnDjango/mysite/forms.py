from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image']

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Enter item name",
                "required" : True
            }),

            "description": forms.Textarea(attrs={
                "placeholder": "Enter item description",
                "required" : True,
            }),

            "price": forms.NumberInput(attrs={
                "placeholder": "Enter price",
                "required" : True,
            }),
            "image": forms.URLInput(attrs={
                "placeholder": "Enter image URL",
                "required" : False
            })
        }

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero")
        return price
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name and description and name.lower() in description.lower():
            self.add_error(
                "description",
                "Description should not contain the item name."
            )

        return cleaned_data

