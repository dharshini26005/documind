import os

from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

from config import UPLOAD_FOLDER

from services.pdf_service import PDFService
from services.notes import NotesService


notes_bp = Blueprint(
    "notes",
    __name__
)


@notes_bp.route("/notes")
def notes_page():

    return render_template("notes.html")


@notes_bp.route("/notes/generate", methods=["POST"])
def generate_notes():

    file = request.files["pdf"]

    if file.filename == "":
        return "Please select a PDF"

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(filepath)

    text = PDFService.extract_text(filepath)

    notes = NotesService.generate_notes(text)

    return render_template(

        "notes.html",

        notes=notes,

        filename=filename

    )