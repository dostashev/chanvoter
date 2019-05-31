var date_diff_to_str = () => { 
    var msec = diff; 
    var dd = Math.floor(msec / 1000 / 60 / 60 / 24);
    msec -= dd * 1000 * 60 * 60 * 24;
    var hh = Math.floor(msec / 1000 / 60 / 60);
    msec -= hh * 1000 * 60 * 60;
    var mm = Math.floor(msec / 1000 / 60);
    msec -= mm * 1000 * 60;
    var ss = Math.floor(msec / 1000);
    msec -= ss * 1000;

    return `${dd} д., ${hh} ч., ${mm} м., ${ss} с.`;
}

var updateCountdown = (countdown) => {
    end_date = new Date(countdown.getAttribute('endtime'))
    diff = end_date - Date.now();
    countdown.innerHTML = date_diff_to_str(diff);
}


var updateWaitingCountdown = (countdown) => {
    begin_time = new Date(countdown.getAttribute('begintime'))
    diff = begin_time - Date.now();
    countdown.innerHTML = date_diff_to_str(diff);
}

window.addEventListener("load", () => {
    countdowns = Array.from(document.getElementsByClassName("countdown"));
    waiting_countdowns = Array.from(document.getElementsByClassName("waiting-countdown"));

    countdowns.forEach( (cd) => {
        setInterval(() => updateCountdown(cd), 1000);
    });

    waiting_countdowns.forEach( (cd) => {
        setInterval(() => updateWaitingCountdown(cd), 1000);
    });
})

