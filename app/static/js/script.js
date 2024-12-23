const form = document.querySelector("form");
const loadingSpinner = document.getElementById("loading-spinner");
const responseStatus = document.getElementById("response-status");

const spinnerHTML = `<span class="spinner-border sr-only position-relative top-50 start-50"></span>`;
const successDownloadHTML = `<div id="success" class="alert alert-success" role="alert">O Download foi bem sucedido e começará em breve.</div>`;
const failDownloadHTML = `<div id="fail" class="alert alert-danger" role="alert">Ocorreu um erro no Download.</div>`;
const emptyHtml = ``;

function atSubmit() {
    loadingSpinner.innerHTML = spinnerHTML;
    responseStatus.innerHTML = emptyHtml;
}

function clearSpinner() {
    loadingSpinner.innerHTML = emptyHtml;
}

function toggleButtonVisibility(isLoading) {
    const button = document.getElementById("submit-btn");
    button.style.display = isLoading ? "none" : "inline-block";
}

form.addEventListener("submit", (event) => {
    atSubmit();
    toggleButtonVisibility(true);
    try{
        setTimeout(() => {
        toggleButtonVisibility(false);
        clearSpinner();
        responseStatus.innerHTML = successDownloadHTML;
    }, 3000); // dá um desconto pq foi o primeiro programa web    
    }
    catch(error){
        responseStatus.innerHTML = failDownloadHTML;
    }
});
