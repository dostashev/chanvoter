var updateCountdown = (countdown) => {
    end_date = new Date(countdown.getAttribute('endtime'))
    diff = end_date - Date.now()
    
    var msec = diff; 
    var hh = Math.floor(msec / 1000 / 60 / 60);
    msec -= hh * 1000 * 60 * 60;
    var mm = Math.floor(msec / 1000 / 60);
    msec -= mm * 1000 * 60;
    var ss = Math.floor(msec / 1000);
    msec -= ss * 1000;

    countdown.innerHTML = hh + " часов, " + mm + " минут, " + ss + " секунд. "
}

window.addEventListener("load", () => {
    countdowns = Array.from(document.getElementsByClassName("countdown"))

    countdowns.forEach( (cd) => {
        setInterval(() => updateCountdown(cd), 1000)
    })
})

