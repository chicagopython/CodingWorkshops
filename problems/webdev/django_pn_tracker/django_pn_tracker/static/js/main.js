(function ($, win, UNDEFINED) {

    $(".nav-list-expandable.nav-list-expanded > ul:eq(0)").show();

    $(".nav-list-expandable > a").click(function() {
        var a = $(this),
            li = a.parent(),
            ul = li.children('ul').first();

        if (ul.length > 0) {
            if (ul.is(":visible")) {
                li.removeClass("nav-list-expanded");
                ul.slideUp(150);
            }
            else {
                li.addClass("nav-list-expanded");
                ul.slideDown(250);
            }
        }
    });

})(jQuery, this);