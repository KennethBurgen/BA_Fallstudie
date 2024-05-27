from django.shortcuts import render, get_object_or_404
from .forms import UploadFileForm
from .models import UploadedFile


def home(request):
    # Home Seite anzeigen
    if request.method == 'GET':
        # Alle hochgeladenen Dateien dem Template mitgeben
        uploaded_files = UploadedFile.objects.all()
        return render(request, 'uploadFile_templates/home.html', {'uploaded_files': uploaded_files})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            # Die Datei in DB und Uploads Ordner speichern
            uploaded_file = form.save()

            # Die Datei dem Template zum Download mitgeben
            uploaded_file_id = uploaded_file.id
            returning_uploaded_file = get_object_or_404(UploadedFile, id=uploaded_file_id)
            return render(request, 'uploadFile_templates/uploadFile_success.html', {'file': returning_uploaded_file})
    else:
        form = UploadFileForm()

    return render(request, 'uploadFile_templates/uploadFile.html', {'form': form})


def delete_file(request):
    if request.method == 'POST':

        file_id = request.POST.get('file_id')
        file_to_delete = get_object_or_404(UploadedFile, id=file_id)

        # Die Datei an sich löschen (aus uploads Ordner)
        file_to_delete.file.delete(save=False)

        # Die Datei aus der DB löschen
        file_to_delete.delete()

        # Löschen erfolgreich Template übermitteln
        return render(request, 'uploadFile_templates/deleteFile_success.html')
    elif request.method == 'GET':
        # Alle hochgeladenen Dateien dem Template mitgeben
        uploaded_files = UploadedFile.objects.all()
        return render(request, 'uploadFile_templates/deleteFile.html', {'uploaded_files': uploaded_files})