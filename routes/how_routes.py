from flask import Blueprint, render_template

how_bp = Blueprint(
    "how",
    __name__
)


@how_bp.route("/how-it-works")
def how_page():

    return render_template(
        "how_it.html"
    )