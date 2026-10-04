

function addPopoverListeners() {
    const target = document.getElementById('pete-martell');
    const popover = document.getElementById('my-popover');

    target.addEventListener('click', () => {
        popover.showPopover();
    });
}

document.addEventListener("DOMContentLoaded", function () {
  console.log("dom loaded")
  addPopoverListeners()
});