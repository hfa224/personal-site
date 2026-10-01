function wiggleWitIt() {
     wiggles = document.getElementsByTagName("w");
  
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

document.addEventListener("DOMContentLoaded", wiggleWitIt());
