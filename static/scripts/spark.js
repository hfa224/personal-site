

function addButtonListeners() {

    const button = document.getElementById('lighter-button');
    const content = document.getElementById('text-content');

    // Show when the mouse button goes down
    button.addEventListener('mousedown', () => {
        content.style.display = 'block';
    });

    // Hide when the mouse button is released
    button.addEventListener('mouseup', () => {
        content.style.display = 'none';
    });

    // Hide if the user drags the mouse off the button and releases it
    button.addEventListener('mouseleave', () => {
        content.style.display = 'none';
    });
}

var count = 0;

function onIncrementOnClick() {
    count = count + 1;
    if (count < 4) {
        const content = document.getElementById('message' + count);
        content.style.display = 'block';
    }
}

document.addEventListener("DOMContentLoaded", function () {
    console.log("dom loaded")
    addButtonListeners();
});