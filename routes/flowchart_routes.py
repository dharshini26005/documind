import os
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER
from services.pdf_service import PDFService
from services.flowchart import FlowchartService


flowchart_bp = Blueprint(
    "flowchart",
    __name__
)


@flowchart_bp.route("/flowchart")
def flowchart_page():

    return render_template("flowchart.html")


@flowchart_bp.route("/flowchart/generate", methods=["POST"])
def generate_flowchart():

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

    diagram = FlowchartService.generate_flowchart(text)

    print("\n========== GROQ OUTPUT ==========\n")
    print(diagram)
    print("\n===============================\n")

    return render_template(
    "flowchart.html",
    diagram=diagram,
    filename=filename
)