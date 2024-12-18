const form = document.querySelector("form")
const loadingSpinner = document.getElementById("loading-spinner")
const spinnerHTML = `<span class="spinner-border sr-only position-relative top-50 start-50"></span>`;
const responseStatus = document.getElementById("response-status")
const successDownloadHTML = `<div id = "success" class="alert alert-success" role="alert">O Download foi concluido</div>`
const failDownloadHTML = `<div id = "fail" class="alert alert-danger" role="alert">Ocorreu um erro no Download</div>`
const emptyHtml = ``;

function atSubmit() {
    loadingSpinner.innerHTML = spinnerHTML;
    responseStatus.innerHTML = emptyHtml;
}

function clearSpinner() {
    loadingSpinner.innerHTML = emptyHtml;
}

function toggleButtonVisibility(isLoading) {
    const button = document.getElementById("submit-btn")
    if (isLoading) {
        button.style.display = "none";
    }
    else { button.style.display = "inline-block" }
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    atSubmit();
    toggleButtonVisibility(true);
    const formData = new FormData(form);
    try {
        const response = await fetch('/baixar_audio', {
            method: 'POST',
            body: formData
        });
        if(response.ok){
            responseStatus.innerHTML = successDownloadHTML;
        }
    }

    catch (error) {
        responseStatus.innerHTML = failDownloadHTML;
    }
    finally {

        toggleButtonVisibility(false);
        clearSpinner();
    }
}
)