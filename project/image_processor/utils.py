from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import ImageEnhance, Image
import pilgram
from io import BytesIO
import os

filters = {
    # pilgram instagram filters:
    "_1977": pilgram._1977,
    "aden": pilgram.aden,
    "brannan": pilgram.brannan,
    "brooklyn": pilgram.brooklyn,
    "clarendon": pilgram.clarendon,
    "earlybird": pilgram.earlybird,
    "gingham": pilgram.gingham,
    "hudson": pilgram.hudson,
    "inkwell": pilgram.inkwell,
    "kelvin": pilgram.kelvin,
    "lark": pilgram.lark,
    "lofi": pilgram.lofi,
    "maven": pilgram.maven,
    "mayfair": pilgram.mayfair,
    "moon": pilgram.moon,
    "nashville": pilgram.nashville,
    "perpetua": pilgram.perpetua,
    "reyes": pilgram.reyes,
    "rise": pilgram.rise,
    "slumber": pilgram.slumber,
    "stinson": pilgram.stinson,
    "toaster": pilgram.toaster,
    "valencia": pilgram.valencia,
    "walden": pilgram.walden,
    "willow": pilgram.willow,
    "xpro2": pilgram.xpro2,
    # pilgram css filters:
    "contrast": pilgram.css.contrast,
    "grayscale": pilgram.css.grayscale,
    "sepia": pilgram.css.sepia   
}

adjustments = {
    # Image adjustment tools from Pillow
    "brightness": ImageEnhance.Brightness,
    "contrast": ImageEnhance.Contrast,
    "sharpness": ImageEnhance.Sharpness,
    "saturation": ImageEnhance.Color
}

# apply filter and/or adjust image, save
def apply_filter_and_adjustment(image_ins, modification_object):
    image = Image.open(image_ins.image)
    image_ins.file_extension = image.format.lower()
    image_ins.filename = os.path.splitext(image_ins.image.name)[0].replace("results/", "")

    if image.mode not in ("RGB", "RGBA"):
        image = image.convert("RGBA")
    
    if modification_object.filter_type:
        image = filters[modification_object.filter_type](image)

    if modification_object.adjustment_type and modification_object.factor:
        adjustment_function = adjustments[modification_object.adjustment_type](image)
        image = adjustment_function.enhance(modification_object.factor)
        
    output_buffer = BytesIO()
    image.save(output_buffer, format = image_ins.file_extension)
    output_buffer.seek(0)
    
    image_ins.image = InMemoryUploadedFile(
        output_buffer,
        "ImageField",
        f"modified_{image_ins.filename}.{image_ins.file_extension}",
        f"image/{image_ins.file_extension}",
        output_buffer.tell(),
        None
    )

    image_ins.save()