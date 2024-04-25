from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UploadedFile
from .forms import UploadFileForm

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadedFile(file=request.FILES['file'], user=request.user)
            new_file.save()
            return redirect('file_upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
