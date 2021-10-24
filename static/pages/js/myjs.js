$(document).ready(main);

function main() {
    // Main nav sub menu  
    $('.dropdown').click(function() {
        $(this).children('.dropdown-content').slideToggle();
    })
}

// Language dropdown menu
$(document).ready(function() {
    $('button').click(function() {
        $('.languages-dropdown-content ul').slideToggle();
    });
});