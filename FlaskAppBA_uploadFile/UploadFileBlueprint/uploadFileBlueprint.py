import os
import uuid
from flask import Blueprint, render_template, request, send_file
from .db_models import UploadedFile, db
from .blueprint_forms import UploadFileForm


uploadFile_BP = Blueprint("uploadFile", __name__, url_prefix="/fileUpload",
                          static_folder="static", template_folder='templates')

FILESAVEPATH = 'uploads'


@uploadFile_BP.route('/', methods=['GET'])
def home():
    # Alle hochgeladenen Dateien dem Template mitgeben
    uploaded_files = UploadedFile.query.all()
    return render_template("uploadFile_templates/home.html", uploaded_files=uploaded_files)


@uploadFile_BP.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        form = UploadFileForm()
        if form.validate_on_submit():

            # infos aus Formular entnehmen
            file = form.file.data
            filename = file.filename

            # Datei & speicherpfad zusammenfügen
            filepath = os.path.join(uploadFile_BP.root_path, FILESAVEPATH+f'/{filename}')

            # Auf Namenskonflikte prüfen und ggf. Suffix hinzufügen
            while os.path.exists(filepath):
                file_extension = os.path.splitext(filename)[1]
                suffix = str(uuid.uuid4().hex[:6])
                filename = f"{os.path.splitext(filename)[0]}_{suffix}{file_extension}"
                file.filename = filename
                filepath = os.path.join(uploadFile_BP.root_path, FILESAVEPATH+f'/{filename}')

            # Datei in Ordner sicher
            file.save(filepath)

            # Datenbankeintrag zur Datei erstellen
            uploaded_file = UploadedFile(filename=filename, filepath=filepath)
            db.session.add(uploaded_file)
            db.session.commit()

            # Die Datei dem Template zum Download mitgeben
            uploaded_file_id = uploaded_file.id
            returning_uploaded_file = UploadedFile.query.get_or_404(uploaded_file_id)
            return render_template("uploadFile_templates/uploadFile_success.html", file=returning_uploaded_file)

    elif request.method == 'GET':
        form = UploadFileForm()

    return render_template("uploadFile_templates/uploadFile.html", form=form)


@uploadFile_BP.route('/delete', methods=['GET', 'POST'])
def delete_file():
    if request.method == 'POST':

        file_id = request.form['file_id']
        file_to_delete = UploadedFile.query.get_or_404(file_id)

        # Die Datei an sich löschen (aus uploads Ordner)
        if os.path.exists(file_to_delete.filepath):
            os.remove(file_to_delete.filepath)

        # Die Datei aus der DB löschen
        db.session.delete(file_to_delete)
        db.session.commit()

        #Löschen erfolgreich Template übermitteln
        return render_template("uploadFile_templates/deleteFile_success.html")

    elif request.method == 'GET':
        # Alle hochgeladenen Dateien dem Template mitgeben
        uploaded_files = UploadedFile.query.all()
        return render_template("uploadFile_templates/deleteFile.html", uploaded_files=uploaded_files)


@uploadFile_BP.route("/file/<int:file_id>", methods=['GET'])
def download_file(file_id):
    if request.method == 'GET':
        # Nach Datei mit übermittelter ID suchen und zurückgeben
        uploadedFile = UploadedFile.query.get_or_404(file_id)
        filepath = os.path.join(uploadFile_BP.root_path, FILESAVEPATH+f'/{uploadedFile.filename}')
        return send_file(filepath, as_attachment=True)