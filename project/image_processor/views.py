from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .forms import ImageForm, ModificationForm
from .utils import apply_filter_and_adjustment
from .models import ImageModel
from PIL import UnidentifiedImageError
import os
import shutil
import zipfile

def home(request):  
    image_form = ImageForm(request.POST, request.FILES)
    modification_form = ModificationForm(request.POST)
    
    if request.method == "POST":      
        try:
            images = request.FILES.getlist("image")
            uploaded_image_ids = []
            modification_object = modification_form.save(commit=False)
            
            if images:
                for image in images:
                    image_ins = ImageModel(image=image)
                    image_ins.save()
                    uploaded_image_ids.append(image_ins.pk)

                    apply_filter_and_adjustment(image_ins, modification_object)

                request.session["uploaded_image_ids"] = uploaded_image_ids
                return redirect("result")
            else:
                request.session["upload_error"] = "No files were uploaded."
                return render(request, "home.html", {
                    "image_form": image_form,
                    "modification_form": modification_form,
                    "upload_error": "No files were uploaded."
                })
        
        except (ValidationError, UnidentifiedImageError) as error_message:
            messages.error(request, str(error_message))
            return redirect("home") 
            
    request.session.pop("upload_error", None)
    
    return render(request, "home.html", {
        "image_form": image_form,
        "modification_form": modification_form,
        "upload_error": request.session.pop("upload_error", None)
    })

def result(request):
    uploaded_image_ids = request.session.get("uploaded_image_ids", [])
    images = ImageModel.objects.filter(pk__in=uploaded_image_ids)

    #render result page
    if request.method == "GET":
        arguments = {
            "images": images
        }

        return render(request, "result.html", arguments)

    #download all modified images in .zip format if button is clicked
    elif request.method == "POST" and "download_all" in request.POST:
        temp_dir = "temp_images"
        os.makedirs(temp_dir, exist_ok = True)

        for image in images:
            modified_image_path = os.path.join(temp_dir, f"modified_{image.filename}.{image.file_extension}")
            with open(modified_image_path, "wb") as f:
                f.write(image.image.read())

        zip_filename = "modified_images.zip"
        with zipfile.ZipFile(zip_filename, "w") as zip_file:
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    archive_name = os.path.relpath(file_path, temp_dir)
                    zip_file.write(file_path, arcname = archive_name)

        with open(zip_filename, "rb") as zip_file:
            response = HttpResponse(zip_file.read(), content_type = "application/zip")
            response["Content-Disposition"] = f"attachment; filename = {zip_filename}"

        shutil.rmtree(temp_dir)
        os.remove(zip_filename)

        return response
    
    
    
