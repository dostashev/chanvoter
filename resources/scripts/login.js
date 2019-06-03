window.addEventListener('load', () => {
    document.getElementById('login-btn').addEventListener('click', () => {
        private_key = document.getElementById('private-key-form').value

        fetch(`/auth?private_key=${private_key}`, {
            method : 'POST'
        })
        .then((resp) => {return resp.text() })
        .then((text) => {
            if(text == "denied") {
                $('#wrong-key-alert').modal();
            }
            else {
                document.location.href = "/"
            }
        });
    });
});
