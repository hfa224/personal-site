



function rotateStyle () {
  document.body.id = document.body.id == 'pastel' ? '' : 'pastel';
  document.getElementsByTagName("main")[0].id = document.getElementsByTagName("main")[0].id == 'pastel' ? '' : 'pastel';
}



document.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");
    var html = document.getElementsByName("body")
    html.classList.add("gothic-gradient")

});