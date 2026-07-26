import os

from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

from config import UPLOAD_FOLDER
from services.pdf_service import PDFService
from services.mindmap import MindMapService

mindmap_bp = Blueprint(
    "mindmap",
    __name__
)


@mindmap_bp.route("/mindmap")
def mindmap_page():
    return render_template("mindmap.html")


@mindmap_bp.route("/mindmap/generate", methods=["POST"])
def generate_mindmap():

    file = request.files["pdf"]

    if file.filename == "":
        return "Please select a PDF."

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(filepath)

    text = PDFService.extract_text(filepath)

    diagram = MindMapService.generate_mindmap(text)

    return render_template(
        "mindmap.html",
        diagram=diagram,
        filename=filename
    )