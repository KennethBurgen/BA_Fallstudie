============
UploadFileApp
============

UploadFileApp ist eine Django App für das Hochladen, sowie Löschen von Dateien.

Einbinden
-----------

1. "UploadFileApp" muss folgendermaßen zu INSTALLED_APPS in der Settings.py des Projektes hinzugefügt::

    INSTALLED_APPS = [
        ...,
        "Django_UploadFileApp",
    ]

2. Anschließend muss die URLconf von "UploadFileApp" noch in die urls.py des Projektes wie folgt eingebunden werden::

    path('fileUpload/', include('Django_UploadFileApp.urls')),

3. Als nächstes muss der Befehl ``python manage.py migrate`` durchgeführt werden, um die `models` zu erstellen.

4. Nun muss der Entwicklungsserver gestartet werden (z.B. mittels ``python manage.py runserver``).

5. Abschließend kann die ``/fileUpload/`` URL besucht werden.