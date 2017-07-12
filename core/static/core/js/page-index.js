
$(document).ready(function() {
	var image_width = 900;
	var image_height = 600;

	var slideshow = $('#slideshow');
	var slideshow_height = window.innerWidth * image_height / image_width;
	slideshow_height = Math.min(slideshow_height, window.innerHeight - 40);

	var max_height = slideshow.data('max-height');
	if (typeof max_height !== 'undefined') {
		slideshow_height = Math.min(slideshow_height, max_height);
	}

	slideshow.slidesjs({
		width: window.innerWidth,
		height: slideshow_height,
		navigation: {
		  active: false,
		},
		effect: {
		  slide: {
		    speed: 1000,
		  },
		},
		play: {
		  active: false,
		  effect: "slide",
		  interval: 4000,
		  auto: true,
		  pauseOnHover: false,
		  restartDelay: 2500,
		},
    });

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
});
