// Show selected filename

const pdfInput = document.getElementById("pdf");
const filename = document.getElementById("filename");

if (pdfInput) {

    pdfInput.addEventListener("change", function () {

        if (this.files.length > 0) {

            filename.innerHTML = "📄 " + this.files[0].name;

        }

    });

}


// Loading Animation

const form = document.getElementById("summaryForm");

if (form) {

    form.addEventListener("submit", function () {

        document.getElementById("loading").style.display = "block";

    });

}


// Copy Summary

function copySummary() {

    const text = document.getElementById("summaryText").innerText;

    navigator.clipboard.writeText(text);

    alert("Summary copied successfully!");

}