
var clickCounter = 0;
function onClickEventHandler() {
    console.log("Clicker clicked " + clickCounter);
    var clicker = document.getElementById("clicker")
    createOwDiv(document);
    clickCounter = clickCounter + 1;
    if (clickCounter >= 10) {
        clicker.classList.add("green")
    } if (clickCounter >= 20) {
        clicker.style.display = "none";
        var prize = document.getElementById("prize")
        prize.style.display = "block";
    } else {
    }
}

const wordsArray = ["up", "down", "right", "left"]

function createOwDiv(document) {

    var paras = document.getElementsByClassName('words');
    if (paras) {
        console.log("Removing old words")
        while (paras[0]) {
            paras[0].parentNode.removeChild(paras[0]);
        }
    }
    // create a new div element
    const newDiv = document.createElement("div");

    // and give it some content
    const newContent = document.createTextNode("Ow!");

    // add the text node to the newly created div
    newDiv.appendChild(newContent);
    newDiv.setAttribute("class", "words")
    newDiv.classList.add(wordsArray[Math.floor(Math.random() * 4)]);
    newDiv.classList.add("elementToFadeInAndOut")

    // add the newly created element and its content into the DOM
    const currentDiv = document.getElementById("clicker");
    currentDiv.appendChild(newDiv)
}

document.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");
    var clicker = document.getElementById("clicker")
    clicker.addEventListener('click', this.onClickEventHandler);
});