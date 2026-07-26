import os

from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

from config import UPLOAD_FOLDER

from services.pdf_service import PDFService
from services.chunk import ChunkService
from services.embedding import EmbeddingService
from services.rag import RAGService


chat_bp = Blueprint(
    "chat",
    __name__
)


# -----------------------------
# Open Chat Page
# -----------------------------

@chat_bp.route("/chat")
def chat_page():

    return render_template(
        "chat.html"
    )


# -----------------------------
# Upload PDF
# -----------------------------

@chat_bp.route("/chat/upload", methods=["POST"])
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
        "chat.html",
        uploaded=True,
        filename=filename
    )


# -----------------------------
# Ask AI
# -----------------------------

@chat_bp.route("/chat/ask", methods=["POST"])
def ask_question():

    question = request.form.get("question")

    answer = RAGService.ask(question)

    return render_template(
        "chat.html",
        uploaded=True,
        question=question,
        answer=answer
    )