function activateSection($section, toggleFix) {
    var isActive = $section.hasClass('active'),
        isFixed = $section.hasClass('fixed');

    if (toggleFix) {
        if (isFixed) {
            removeFixed($section);
        } else {
            setFixed($section);
        }
    } else if (isFixed) {
        removeFixed($section);
    }

    $('.active').not('.fixed')
        .removeClass('active')
        .find('article').slideToggle();

    if (!isActive) {
        $section.addClass('active')
            .find('article').slideToggle();
    }
}
function setFixed($section) {
    $section.addClass('fixed');
    $section.find('span.header-svg').attr('title', 'allow collapse');
    $section.find('#minus').show();
    $section.find('#plus').hide();
}
function removeFixed($section) {
    $section.removeClass('fixed');
    $section.find('span.header-svg').attr('title', 'keep expanded');
    $section.find('#minus').hide();
    $section.find('#plus').show();
}


$(document).ready(function() {
    'use strict';
    if (window.location.href.indexOf('static') !== -1) {
        setTimeout(function() {
            $('section').addClass('active');
        }, 3000);
    }
    $('h1, span.header-svg').on('click', function() {
        var $section = $(this).closest('section');
        var toggleSvg = $(this).is('span');
        activateSection($section, toggleSvg);
    });
});
