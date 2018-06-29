$(window).on('load', function() {      //Do the code in the {}s when the window has loaded 
$("#loader").fadeOut("fast");  //Fade out the #loader div
});
$(document).ready(function(){
	
	/*************** mavbar ******/
	$(document).delegate('.open', 'click', function(event){
		$(this).addClass('oppenned');
		event.stopPropagation();
	})
	$(document).delegate('body', 'click', function(event) {
		$('.open').removeClass('oppenned');
	})
	$(document).delegate('.cls', 'click', function(event){
		$('.open').removeClass('oppenned');
		event.stopPropagation();
	});
	
	/************* navbar scroll  *****************/
	
	// Add smooth scrolling to all links
	$(".navilink").on('click', function(event) {
		
		// Make sure this.hash has a value before overriding default behavior
		if (this.hash !== "") {
			// Prevent default anchor click behavior
			event.preventDefault();
			
			// Store hash
			var hash = this.hash;
			
			// Using jQuery's animate() method to add smooth page scroll
			// The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
			$('html, body').animate({
				scrollTop: $(hash).offset().top
			}, 800, function(){
				
				// Add hash (#) to URL when done scrolling (default click behavior)
				window.location.hash = hash;
			});
		} // End if
	});
	
	/*********** Slider ***********/
	
	var slideStart;
	
	function startSlide() {
		slideStart = setInterval(slideShow, 5000);
	};
	function slideShow() {
		
		var slideCurrent = $(".slide-active");
		var slideNext = slideCurrent.next();
		var dotCurrent = $("li.active");
		var dotNext = dotCurrent.next();
		
		if (slideNext.length == 0) {
			slideNext = $(".slide").first();
			dotNext = $(".slide-indicator li").first();
		}
		
		var slideIndex = slideNext.index();
		
		$('.slide').css({
			'transform': 'translate(-' + (slideIndex) * 100 + '%)'
		});
		
		$('.slide').removeClass('slide-active');
		slideNext.addClass('slide-active');
		
		var captionNext = slideNext.find(".caption");
		
		$('.slide-indicator li').removeClass('active');
		dotNext.addClass('active');
	};
	function siteNav() {
		
		$(".nav-menu").on("click", function() {
			$("body").animate({
				'right': '320'
			});
			$(".nav-container").animate({
				'right': '0'
			});
			$("<div class=\"nav-wrapper\"></div>").appendTo("body");
		});
		
		$(".close-button").on("click", buttonClose);
		$("body").on("click", '.nav-wrapper', buttonClose);
		
		function buttonClose() {
			$(".nav-wrapper").remove();
			$(".caret").removeClass("open");
			$(".dropdown-nav").slideUp();
			$("body").animate({
				'right': '0'
			});
			$(".nav-container").animate({
				'right': '-100%'
			});
		}
		
		$(".dropdown-container a").on("click", function(){
			$(this).children(".caret").toggleClass("open");
			$(this).next(".dropdown-nav").slideToggle(300);
		});
		
	};
	
	$('.slide-indicator li').on("click", function() {
		
		clearInterval(slideStart);
		var goToSlide = $(this).index();
		
		$('.slide-indicator li').removeClass('active');
		$('.slide').removeClass('slide-active');
		$('.slide').eq(goToSlide).addClass('slide-active');
		$(this).addClass('active');
		
		$('.slide').css({
			'transform': 'translate(-' + (goToSlide) * 100 + '%)'
		});
		startSlide();
	});
	
	startSlide();
	siteNav();
	
	
	/* ********* PARTICLES JS INIT ****************/
	
	
	var partJson = {
		"particles": {
			"number": {
				"value": 100,
				"density": {
					"enable": true,
					"value_area": 800
				}
			},
			"color": {
				"value": "#5e5e5e"
			},
			"shape": {
				"type": "circle",
				"stroke": {
					"width": 0,
					"color": "#000000"
				},
				"polygon": {
					"nb_sides": 5
				},
				"image": {
					"src": "img/github.svg",
					"width": 100,
					"height": 100
				}
			},
			"opacity": {
				"value": 0.5,
				"random": false,
				"anim": {
					"enable": false,
					"speed": 1,
					"opacity_min": 0.1,
					"sync": false
				}
			},
			"size": {
				"value": 3,
				"random": true,
				"anim": {
					"enable": false,
					"speed": 40,
					"size_min": 0.1,
					"sync": false
				}
			},
			"line_linked": {
				"enable": true,
				"distance": 80,
				"color": "#5e5e5e",
				"opacity": 0.4,
				"width": 0.6413648243462091
			},
			"move": {
				"enable": true,
				"speed": 6,
				"direction": "none",
				"random": false,
				"straight": false,
				"out_mode": "out",
				"bounce": false,
				"attract": {
					"enable": false,
					"rotateX": 600,
					"rotateY": 1200
				}
			}
		},
		"interactivity": {
			"detect_on": "window",
			"events": {
				"onhover": {
					"enable": false,
					"mode": "repulse"
				},
				"onclick": {
					"enable": true,
					"mode": "push"
				},
				"resize": true
			},
			"modes": {
				"grab": {
					"distance": 400,
					"line_linked": {
						"opacity": 1
					}
				},
				"bubble": {
					"distance": 400,
					"size": 40,
					"duration": 2,
					"opacity": 8,
					"speed": 3
				},
				"repulse": {
					"distance": 200,
					"duration": 0.4
				},
				"push": {
					"particles_nb": 4
				},
				"remove": {
					"particles_nb": 2
				}
			}
		},
		"retina_detect": true
	};
	var jsonUri = "data:text/plain;base64,"+window.btoa(JSON.stringify(partJson));
	particlesJS.load('particles-js', jsonUri);
	
	/*******  Ticker  *******/
	
	$(".default-ticker").ticker({
		
		// item selector
		item: 'div',
		
		// Toggles whether the ticker should pause on mouse hover
		pauseOnHover: true,
		
		// <a href="https://www.jqueryscript.net/animation/">Animation</a> speed
		speed: 70,
		
		// Decides whether the ticker breaks when it hits a new item or if the track has reset
		pauseAt: '',
		
		// delay in milliseconds
		delay: 500
		
	});
	
	/************ Tooltip init *****************/
	
	$(function () {
		$('[data-toggle="tooltip"]').tooltip()
	});
	
	/*************  Lazy Loading **************/
	
	registerListener('load', setLazy);
	registerListener('load', lazyLoad);
	registerListener('scroll', lazyLoad);
	
	var lazy = [];
	
	function setLazy(){
		lazy = document.getElementsByClassName('lazy');
	} 
	
	function lazyLoad(){
		for(var i=0; i<lazy.length; i++){
			if(isInViewport(lazy[i])){
				if (lazy[i].getAttribute('data-src')){
					lazy[i].src = lazy[i].getAttribute('data-src');
					lazy[i].removeAttribute('data-src');
				}
			}
		}
		
		cleanLazy();
	}
	
	function cleanLazy(){
		lazy = Array.prototype.filter.call(lazy, function(l){ return l.getAttribute('data-src');});
	}
	
	function isInViewport(el){
		var rect = el.getBoundingClientRect();
		
		return (
			rect.bottom >= 0 && 
			rect.right >= 0 && 
			rect.top <= (window.innerHeight || document.documentElement.clientHeight) && 
			rect.left <= (window.innerWidth || document.documentElement.clientWidth)
		);
	}
	
	function registerListener(event, func) {
		if (window.addEventListener) {
			window.addEventListener(event, func)
		} else {
			window.attachEvent('on' + event, func)
		}
	}
	
});



