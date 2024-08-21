// set the target dates

// write an update counter method that given the target date, calculates the time since then
// and updates an elemnt with the text every minute

// months are indexed 0
var targetDate1 = new Date(2024, 2, 8) // 08/03/2024 since i totaled my car
var targetDate2 = new Date(2024, 3, 25) // 25/04/2024 started sertraline
var targetDate3 = new Date(2023, 5, 29) // 29/05/2023 fred asked me out
var targetDate4 = new Date(2023, 10, 10) // 10/10/2023 passed my driving test
var targetDate5 = new Date(2024, 3, 27) // 27/04/2024 (ish) last cigarette

function update(targetDate, id) {
    var now = new Date();

    // get the duration between now and target date
    var duration = now.getTime() - targetDate.getTime();

    // convert duration to hours, minutes, seconds, days, 
    // it's in millseconds
    var durationSeconds = duration / 1000;
    var durationMinutes = durationSeconds / 60;
    var durationHours = durationSeconds / 60;

    var days = Math.floor(duration / (1000 * 60 * 60 * 24));
    var hours = Math.floor(duration / (1000 * 60 * 60)) - (days*24);
    var minutes = Math.floor(duration / (1000 * 60)) - (hours*60) - (days*60*24);
    var seconds = Math.floor(duration / (1000)) - (hours*60*60) - (days*60*24*60) - (minutes*60);

    var durationString = "" + days + " days, " + hours + " hours, " + minutes + " minutes, " + seconds + " seconds."

    document.getElementById(id).textContent=durationString;

}

function updateCounters() {
    update(targetDate1, "targetDate1");
    update(targetDate2, "targetDate2");
    update(targetDate3, "targetDate3");
    update(targetDate4, "targetDate4");
    update(targetDate5, "targetDate5");
}

setInterval(updateCounters, 1000);
