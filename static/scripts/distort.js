

function addListeners() {
    // TODO get target and add hue mouseover 
    const catTarget = document.getElementById("cat");

    catTarget.addEventListener("mouseenter", (event) => {
        // highlight the mouseenter target
        console.log(event);
        event.target.classList.add('multiply');

    });

    catTarget.addEventListener("mouseleave", (event) => {
        // highlight the mouseenter target
        console.log(event);
        event.target.classList.remove('multiply');
    });

    // TODO get target and add hue mouseover 
    const birdTarget = document.getElementById("bird");

    birdTarget.addEventListener("mouseenter", (event) => {
        // highlight the mouseenter target
        console.log(event);
        event.target.classList.add('jay-hue');

    });

    birdTarget.addEventListener("mouseleave", (event) => {
        // highlight the mouseenter target
        console.log(event);
        event.target.classList.remove('jay-hue');
    });

    // TODO get target and add hue mouseover 
    const eyeTarget = document.getElementById("eye");

    eyeTarget.addEventListener("mouseenter", (event) => {
        // highlight the mouseenter target
        console.log(event);
        event.target.classList.add('eye-hue');

    });

    eyeTarget.addEventListener("mouseleave", (event) => {
        // highlight the mouseenter target
        console.log(event);
        event.target.classList.remove('eye-hue');
    });

    eyeTarget.addEventListener("touchstart", (event) => {
        // highlight the mouseenter target
        console.log(event);
        if (event.target.classList.contains('eye-hue')) {

            event.target.classList.remove('eye-hue');
        } else {
            event.target.classList.add('eye-hue');
        }
    });
}


document.addEventListener("DOMContentLoaded", (event) => {
    addListeners();
});


