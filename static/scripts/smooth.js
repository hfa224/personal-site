

function onClickEventHandler() {
  console.log("Dog has been smooved");
  var clicker = document.getElementById("dog")
  clicker.src = "https://bear-images.sfo2.cdn.digitaloceanspaces.com/bluebottles/ezgif-maker.gif"
}

function onClickEndHandler() {
  setTimeout(() => {
    var clicker = document.getElementById("dog")
  clicker.src = "https://bear-images.sfo2.cdn.digitaloceanspaces.com/bluebottles/westie-1.webp"
  }, 1000);
}

addEventListener("DOMContentLoaded", (event) => {
  var clicker = document.getElementById("dog")
  clicker.addEventListener("touchstart", this.onClickEventHandler);
  clicker.addEventListener("touchend", this.onClickEndHandler);
clicker.addEventListener("touchcancel", this.onClickEndHandler);
  clicker.addEventListener('mousedown', this.onClickEventHandler);
  clicker.addEventListener('mouseup', this.onClickEndHandler);
  clicker.addEventListener('mouseenter', this.onClickEventHandler);
  clicker.addEventListener('mouseleave', this.onClickEndHandler);})