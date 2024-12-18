const form = document.querySelector("form")
const responseElement = document.getElementById("response")

function clearAtSubmit(){
        responseElement.innerHTML=``
}

function toggleButtonVisibility(isLoading){
    const button = document.getElementById("submit-btn")
    if (isLoading){
        button.style.display = "none";
    }
    else{button.style.display = "inline-block"}
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    clearAtSubmit();
    toggleButtonVisibility(true);
    const formData = new FormData(form);
    try {
        const response = await fetch('/baixar_audio', {
            method: 'POST',
            body: formData
        });
    }
    catch (error) {
    }
    finally{
        toggleButtonVisibility(false)
    }
}
)