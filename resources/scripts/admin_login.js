function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
        if (decodeURIComponent(pair[0]) == variable) {
            return decodeURIComponent(pair[1]);
        }
    }
}

window.addEventListener("load", () => {
    document.getElementById('sumbit-btn').addEventListener('click', () => {
        var next_url = getQueryVariable('next')

        key = document.getElementById("key-form").value;
        fetch(`/admin_auth?key=${ key }`)
        .then( (resp) => {
            return resp.text()
        })
        .then( (text) => {
            if(text == "success")
                document.location.href = next_url;
            else
                alert(text);
        });
    });
});
