
$(document).ready(function() {
	$(window).scroll(function() {
		var scrollTop = $(window).scrollTop();

		if (scrollTop > 0) {
			$('nav').addClass('fixed');
		} else {
			$('nav').removeClass('fixed');
		}
	});

	/*
	if (slideshow_height >= window.innerHeight / 2) {
		$('nav').addClass('bottomup');
		$('nav').removeClass('topdown');
	}

	var fixed = false;
	var bottomup = true;

	$(window).scroll(function() {
		var scrollTop = $(window).scrollTop();

		if (scrollTop >= slideshow_height / 2) {
			if (bottomup) {
				$('nav').removeClass('bottomup');
				$('nav').addClass('topdown');
				bottomup = false;
			}
		} else if (!bottomup) {
			$('nav').addClass('bottomup');
			$('nav').removeClass('topdown');
			bottomup = true;
		}

		if (scrollTop >= slideshow_height) {
			if (!fixed) {
				$('nav').addClass('fixed');
				fixed = true;
			}
		} else {
			if (fixed) {
				$('nav').removeClass('fixed');
				fixed = false;
			}
		}
	});

	$(window).resize(function() {
		slideshow_height = window.innerWidth * image_height / image_width;
		$(window).scroll();
	});

	$(window).scroll();
	*/
});
