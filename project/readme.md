Bulk Image Modifier
#### Video Demo:  <URL HERE>
#### Description: Django-based web application for modifying (filters & adjustments) images in bulk using Pillow and pilgram. Final Project for CS50x.

For my final project in CS50x, I decided to make a Django web application that allows the user to upload images, apply filters and/or other adjustments to them and download the altered images, either one-by-one or all at once in a .zip file. 

Since the project consists of far too many files for me to go over each of them, I will only cover the ones that are not mostly pre-made by Django. Those include: models.py, forms.py, views.py, utils.py, all 3 html templates (layout.html, home.html, result.html), and the 2 urls.py files. Small changes were made to other files as well, like to the settings.py file to configure where media files are stored, but there were not many significant ones, so I will omit these files. 

The project uses 2 different models defined in models.py, each with their corresponding form defined in forms.py. First, there is the ImageModel, which has 3 fields - image(FileField), filename(CharField), and file_extension(CharField), such that relevant information about each ImageModel object can be stored. ImageModel objects are created via the ImageForm defined in forms.py, which is rendered on the home page and which has the "multiple": "True" attribute, allowing for multi-file uploads, and for each valid uploaded image, a new ImageModel object is created. The filename and file_extension fields get their values in the utils.py file. Second, there is the ModificationModel class in models.py, which is quite straightforward; it is made up of fields filter_type, adjustment_type and factor, which are quite self explanatory, and their values are inputted by the user filling out an instance of ModificationForm on the home page, which offers all the adjustment_type options offered by the Pillow library (these use the factor value to determine adjustment strength, e.g. 100% is the value before any changes, 200% is double the original value, etc.) and filter_type options offered by the pilgram library. The intention of the program is to add the same filter/adjustment to all uploaded images, so the user only fills out this form once even if multiple images are uploaded.

The project's views are contained in views.py, and there are 2 of them:

The home view creates two forms, retrieves the uploaded data upon form submission (if any uploaded files are not valid images, the program will redirect the user back to the home page and render an error message), creates a single instance of ModificationModel and iterates over all uploaded files to create an instance of ImageModel for each. And importantly, in the uploaded_image_ids array, all of the ImageModel objects' primary keys are stored, which is later significant in the result view. Then, for each ImageModel object, the function apply_filter_and_adjustment is called, with both the ImageModel and ModificationModel objects as its arguments. This function uses the Pillow library to open the image and apply adjustments (if any were chosen), the pilgram library to apply filters (if any were chosen), the os library to determine the object's filename and the io and django.core.files.uploadedfile libraries to save the modified version of the image. Furthermore, this function prevents issues by changing the image mode to RGBA if the original mode is not either RGB or RGBA. Afterwards, the user is redirected to the result view.

The result view first retrieves all the modified images from the current session by checking their primary key values, and because the first request is always "GET", renders the result.html template, passing in all the relevant ImageModel objects as arguments. The rest of the result view is dedicated to creating a .zip file, which consists of all modified images and can be downloaded on the result page of the web app. This is done by using the os library for working with file paths, the shutil library for deleting the temp_dir directory and the zipfile library for creating a .zip file and writing to it.

The home.html and result.html templates inherit from layout.html, which contains a very basic html structure and links to bootstrap, which is used for styling both home.html and result.html. The home.html file creates a form with the "post" method, which is made up of ImageForm and ModificationForm type forms, and is the way for the user to input data. As mentioned earlier, if the user uploads an invalid image, they will be redirected back to home.html and an alert will be rendered, prompting the user to input a valid image and displaying the error message/messages provided by the django.contrib library. Furthermore, home.html contains JavaScript that hides the factor form and label when "No Adjustment" is selected and shows the user the exact factor value that they have selected, updating dynamically as the user adjusts the slider widget. The result.html template is made up of 2 parts; first, it displays 2 buttons at the top, one for returning back to the home page and the other for downloading all images in .zip, and second, it iterates over all ImageModel objects, which are passed in as arguments to the template, and displays the images in rows of 3 from left to right, with each image having its own download button in case the user only wants to download specific images. The filename and file_extension fields are also used here for naming the downloadable files. 

When building this web app, I first got started by learning how to work with pilgram and Pillow in a simple Python program. After that, I made a Django web app that took an uploaded image and just displayed it back to the user, allowing them to download it again. Then, I added the filter/adjustment functionality to this app, which was still for single-image uploads only. Next, I yet again set aside the filters and adjustments, and made an app that was able to display all uploaded images with download links for each of them. And finally, I re-implemented the filters and adjustments, made the web app look better with bootstrap, added some finishing touches (handling invalid input, JavaScript, downloading all images in .zip), and that was it.

This is my final project for the CS50x course, and while the course itself does not teach Django and instead focuses on Flask, as I was simultaneously doing the CS50w course, which goes in depth with Django, I decided to use this framework for my web app. I realize that for such a small project like this one, using Flask could have been easier, but I simply chose the option I was more comfortable with. 

Resources used for building this project:
-CS50x (basic html, css, JavaScript, bootstrap, Python)
-CS50w (working with Django)
-the Pillow library's handbook: https://pillow.readthedocs.io/en/stable/handbook/index.html
-The pilgram library's documentation: https://pypi.org/project/pilgram/
-The zipfile library's documentation: https://docs.python.org/3/library/zipfile.html
-ChatGPT 3.5 - debugging, fixing issues, understanding error messages
-https://www.youtube.com/watch?v=Ws7Wy5EHaXY (uploading multiple files to a website, making things look pretty)
-several other web tutorials/youtube videos, mostly related to uploading files, displaying them and modifying them