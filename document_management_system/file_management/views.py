from django.shortcuts import redirect, render

from .forms import FileUploadForm
from .models import UploadedFile


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            description = form.cleaned_data.get('description', '')
            # Save file to server
            file_instance = UploadedFile(file=uploaded_file, description=description)
            file_instance.save()
            return redirect('upload_success')
    else:
        form = FileUploadForm()
    return render(request, 'file_management/upload_file.html', {'form': form})

def upload_success(request):
    return render(request, 'file_management/upload_success.html')

def list_uploads(request):
    uploads = UploadedFile.objects.all()
    return render(request, 'file_management/list_uploads.html', {'uploads': uploads})