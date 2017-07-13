
$(document).ready(function() {
	var slideshow = $('#slideshow');
	var image_width = slideshow.data('image-width');
	var image_height = slideshow.data('image-height');

	var slideshow_height = window.innerWidth * image_height / image_width;

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
});
