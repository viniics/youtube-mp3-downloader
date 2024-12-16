const form = document.querySelector("form")
const response = document.getElementById("response")

form.addEventListener("submit", async (event) => {
    const formData = new FormData(form);

    try {
        const response = await fetch('/baixar_audio', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        if (response.ok) {
            response.innerHTML = `<p>tudo ok</p>`
        }
    }
    catch (error) {
        response.innerHTML = `<p>Deu ruim</p>`
    }
}
)