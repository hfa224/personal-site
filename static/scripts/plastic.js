

function addPopoverListeners() {
    const target = document.getElementById('pete-martell');
    const popover = document.getElementById('my-popover');

    target.addEventListener('click', () => {
        popover.showPopover();
    });
}

function addBeach3PopoverListeners() {
    
    const target2 = document.getElementById('laura-palmers-body-close-up');
    const popover2 = document.getElementById('face-popover');

    target2.addEventListener('click', () => {
        popover2.showPopover();
    });
}


