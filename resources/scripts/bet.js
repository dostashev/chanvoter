var handle_vote_response = (text) => {
    if(text == "error: you have already made a bet")
    {
        $("#extra-vote-alert").modal();
    }
    if(text == "error: invalid private key")
    {
        $("#wrong-key-alert").modal();
    }
    if(text == "error: not enough of money")
    {
        $("#less-money-alert").modal();
    }
    if(text == "error: invalid amount of coins")
    {
        $("#wrong-coins-alert").modal();
    }
    if(text == "success") {
        $("#success-alert").modal();
    }
}

var submit_vote = (chosen_girl_id)  => {
    private_key = document.getElementById('private-key').value
    coins = document.getElementById('coins').value

    params = `private_key=${private_key}&coins=${coins}&contest_id=${CONTEST_ID}&chosen_id=${chosen_girl_id}`

    fetch(`/new_bet?${params}`, {method: 'POST'})
    .then(res => res.text())
    .then(text => handle_vote_response(text))
}

window.addEventListener('load', () => { 
    document.getElementById('private-key').value = PRIVATE_KEY;

    document.getElementById('first-girl-card').addEventListener('click', () => submit_vote(FIRST_GIRL_ID));
    document.getElementById('second-girl-card').addEventListener('click', () => submit_vote(SECOND_GIRL_ID));
});
