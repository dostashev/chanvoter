var handle_vote_response = (text) => {
    if(text != "success") {
        alert(text);
    }
    else {
        window.location.href = "/";
    }
}

var submit_vote = (chosen_girl_id)  => {
    private_key = document.getElementById('private-key').value
    params = `private_key=${private_key}&contest_id=${CONTEST_ID}&chosen_id=${chosen_girl_id}`
    //window.location = `/vote?${params}`

    fetch(`/vote?${params}`, {method: 'POST'})
    .then(res => res.text())
    .then(text => handle_vote_response(text))
}

window.addEventListener('load', () => { 
    document.getElementById('first-girl-card').addEventListener('click', () => submit_vote(FIRST_GIRL_ID));
    document.getElementById('second-girl-card').addEventListener('click', () => submit_vote(SECOND_GIRL_ID));
});
