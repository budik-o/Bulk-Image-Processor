from django import forms
from .models import ImageModel, ModificationModel

FILTER_CHOICES = [
    ("", "No Filter"),
    ("_1977", "_1977"),
    ("aden", "Aden"),
    ("brannan", "Brannan"),
    ("brooklyn", "Brooklyn"),
    ("clarendon", "Clarendon"),
    ("earlybird", "Earlybird"),
    ("gingham", "Gingham"),
    ("hudson", "Hudson"),
    ("inkwell", "Inkwell"),
    ("kelvin", "Kelvin"),
    ("lark", "Lark"),
    ("lofi", "Lofi"),
    ("maven", "Maven"),
    ("mayfair", "Mayfair"),
    ("moon", "Moon"),
    ("nashville", "Nashville"),
    ("perpetua", "Perpetua"),
    ("reyes", "Reyes"),
    ("rise", "Rise"),
    ("slumber", "Slumber"),
    ("stinson", "Stinson"),
    ("toaster", "Toaster"),
    ("valencia", "Valencia"),
    ("walden", "Walden"),
    ("willow", "Willow"),
    ("xpro2", "Xpro2"),
    ("contrast", "Contrast"),
    ("grayscale", "Grayscale"),
    ("sepia", "Sepia")
]

ADJUSTMENT_CHOICES = [
        ("", "No Adjustment"),
        ("brightness", "Brightness"),
        ("contrast", "Contrast"),
        ("sharpness", "Sharpness"),
        ("saturation", "Saturation"),
]

class ImageForm(forms.ModelForm):
    
    image = forms.FileField(required = False, widget = forms.TextInput(attrs = {"name": "images", "type": "File", "class": "form-control", "multiple": "True"}), label = "")
    
    class Meta:
        model = ImageModel
        fields = ["image"]

            
class ModificationForm(forms.ModelForm):
    
    filter_type = forms.ChoiceField(choices = FILTER_CHOICES, required = False, widget = forms.Select(attrs = {"class": "form-select"}))
    adjustment_type = forms.ChoiceField(choices = ADJUSTMENT_CHOICES, required = False, widget = forms.Select(attrs = {"class": "form-select"}))
    factor = forms.FloatField(required = False, widget = forms.NumberInput(attrs = {"step": 0.01, "class": "form-control-range", "type": "range", "min": 0.01, "max": 10, "style": "width: 80%"}))
    
    class Meta:
        model = ModificationModel
        fields = ["filter_type", "adjustment_type", "factor"]
        
        