function classifyImage() {
    const input = document.getElementById('imageInput');
    const resultDiv = document.getElementById('result');

    const file = input.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('image', file);

        fetch('/classify', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `Prediction: ${data.prediction}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        resultDiv.innerHTML = 'Please select an image.';
    }
}
