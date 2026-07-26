from flask import Blueprint, render_template,request

import os

from werkzeug.utils import secure_filename

from config import UPLOAD_FOLDER
from services.pdf_service import PDFService
from services.summary import SummaryService

summary_bp = Blueprint(
    "summary",
    __name__
)

@summary_bp.route("/summary")
def summary_page():

    return render_template("summary.html")
@summary_bp.route("/summary/generate", methods=["POST"])
def generate_summary():

    file = request.files["pdf"]

    if file.filename == "":
        return "Please select a PDF"

    filename = secure_filename(file.filename)

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    text = PDFService.extract_text(filepath)

    summary = SummaryService.generate_summary(text)

    return render_template(
        "summary.html",
        summary=summary,
        filename=filename
    )