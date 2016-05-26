/**
 * Created by lb on 5/24/16.
 */

$(document).ready(function () {
    var $svg = $('.header-svg').first();
    var addSvg = function ($elem) {
        $elem.append(
            $svg.clone().addClass('floating-minus')
        )
    }
    $('.header-svg', 'li').on('click', function () {
        var $previousLine = $(this).parent().prev('li');
        $previousLine.after($previousLine.clone());
        addSvg($(this).parent().prev('li'));

    });
    $('input[name="line"]').slice(1).each(function() {
        addSvg($(this).parent());
    });

    var target = '.dynamic-section';
    $('.add-section').on('click', function () {
        var $elem = $(this).closest(target);
        $elem.after($elem.clone().removeClass('highlight'));
    }).on('mouseenter', function () {
        $(this).closest(target).addClass('highlight')
    }).on('mouseleave', function () {
        $(this).closest(target).removeClass('highlight')
    });
});