import os

from flask import Blueprint, render_template, request

from werkzeug.utils import secure_filename

from config import UPLOAD_FOLDER

from services.pdf_service import PDFService
from services.chunk import ChunkService
from services.embedding import EmbeddingService

upload_bp = Blueprint("upload", __name__)


@upload_bp.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "GET":
        return render_template("upload.html")

    file = request.files["pdf"]

    if file.filename == "":
        return "No file selected"

    # Secure filename
    filename = secure_filename(file.filename)

    # Create full file path
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    # Save PDF
    file.save(filepath)

    # Extract text
    text = PDFService.extract_text(filepath)

    with open("uploads/document.txt", "w", encoding="utf-8") as f:
        f.write(text)

    # Create chunks
    chunks = ChunkService.create_chunks(text)

    # Store embeddings
    EmbeddingService.save_embeddings(
        "doc1",
        chunks
    )

    return "Uploaded Successfully"