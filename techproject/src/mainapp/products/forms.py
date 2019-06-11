from django.forms import ModelForm
from .models import Product

# Enables form validation
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'






