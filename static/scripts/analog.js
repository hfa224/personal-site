

function addViewBoxListeners() {
    const first_viewbox = document.getElementById('viewbox1');
    const second_viewbox = document.getElementById('viewbox2');
    const third_viewbox = document.getElementById('viewbox3');
    const book_cover = document.getElementById('book-cover');
    const empty_page = document.getElementById('empty-page');
    const written_page = document.getElementById('written-page');
    const close_up_popover = document.getElementById('close-up-popover');

    book_cover.addEventListener('click', () => {
        first_viewbox.style.display = 'none';
        second_viewbox.style.display = 'block';
    });

    empty_page.addEventListener('click', () => {
        second_viewbox.style.display = 'none';
        third_viewbox.style.display = 'block';
    });


    written_page.addEventListener('click', () => {
        close_up_popover.showPopover();
    });
}
