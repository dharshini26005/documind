import os

from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

from config import UPLOAD_FOLDER

from services.pdf_service import PDFService
from services.chunk import ChunkService
from services.embedding import EmbeddingService
from services.semantic import SemanticSearchService


search_bp = Blueprint(
    "search",
    __name__
)


# ----------------------------
# Open Semantic Search Page
# ----------------------------

@search_bp.route("/search")
def search_page():

    return render_template(
        "search.html",
        results=[]
    )


# ----------------------------
# Upload PDF
# ----------------------------

@search_bp.route("/search/upload", methods=["POST"])
def upload_document():

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

    chunks = ChunkService.create_chunks(text)

    EmbeddingService.save_embeddings(
        filename,
        chunks
    )

    return render_template(
        "search.html",
        uploaded=True,
        filename=filename,
        results=[]
    )


# ----------------------------
# Semantic Search
# ----------------------------

@search_bp.route("/search/document", methods=["POST"])
def search_document():

    query = request.form.get("query")

    data = SemanticSearchService.search(query)

    results = []

    if data and "documents" in data:

        results = data["documents"][0]

    return render_template(
        "search.html",
        uploaded=True,
        query=query,
        results=results
    )