from django import forms  
from artmgmt.models import Seller  
class SellerForm(forms.ModelForm):  
    class Meta:  
        model = Seller 
        fields = "__all__"  
        widgets = {
            'sgender' : forms.RadioSelect(),
            'tnc' : forms.CheckboxInput(),
        }