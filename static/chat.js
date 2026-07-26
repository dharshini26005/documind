document.addEventListener("DOMContentLoaded",()=>{

    const pdf=document.getElementById("pdf");

    const filename=document.getElementById("filename");

    if(pdf){

        pdf.addEventListener("change",()=>{

            if(pdf.files.length){

                filename.innerHTML=
                "Selected : <strong>"+pdf.files[0].name+"</strong>";

            }

        });

    }

});