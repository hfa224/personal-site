function wiggleWitIt() {
     wiggles = document.getElementsByTagName("w");

     console.log("wrigling");
     console.log(wiggles);
    console.log(wiggles[0]);
    console.log(wiggles.length);
  
    [...wiggles].forEach((wiggle) => {
      wiggle.innerHTML = wiggle
        .innerText
        .split("")
        .map((char, index) => {
          return `<span style='--animation-order: ${index + 1};'>${char}</span>`;
        })
        .join("");
    });
};


document.addEventListener("DOMContentLoaded", function () {
  console.log("dom loaded")
  wiggleWitIt()
});