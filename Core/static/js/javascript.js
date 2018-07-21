
$(document).ready(function(){
	
	
	/******************* Type js init */

	  
	  var typed = new Typed("#typed", {
		stringsElement: '#typed-strings',
		typeSpeed: 30,
		backSpeed: 15,
		backDelay: 1000,
		loop: true
	});

	/* ********* WOW JS INIT ****************/
	new WOW().init();
	
	/**********/
	$(window).scroll(function() {
		if($(this).scrollTop() < 1000){
			$('.service').hide();
			$('.service').stop().animate({ left: '100%' });

		}
		else if(($(this).scrollTop() > 1000) && ($(this).scrollTop() < 1600)){
			$('.service').show();
			$('.service').stop().animate({ left: '0%' });
		}
		else if(($(this).scrollTop() > 1600) && ($(this).scrollTop() < 2200)){
			$('.service').show();
			$('.service').stop().animate({ left: '-100%' });
		}
		else if(($(this).scrollTop() > 2200) && ($(this).scrollTop() < 2800)){
			$('.service').show();
			$('.service').stop().animate({ left: '-200%' });
		} else {
			$('.service').hide();
			$('.service').stop().animate({ left: '-300%' });
		}
	});
	/* ********* Parallax js JS INIT ****************/
	
	var scene = document.getElementById('scene');
	var parallaxInstance = new Parallax(scene);
	
	/* ********* PARTICLES JS INIT ****************/
	
	
	var partJson = {
		"particles": {
			"number": {
				"value": 40,
				"density": {
					"enable": true,
					"value_area": 800
				}
			},
			"color": {
				"value": "#fff"
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
				"color": "#fff",
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
	})
	
});

/*************  Contact form validations **************/

function validateForm() {
	console.log('hi');
	var name =  document.getElementById('name').value;
	if (name == "") {
		document.getElementById('status').innerHTML = "Name cannot be empty";
		return false;
	}
	var email =  document.getElementById('email').value;
	if (email == "") {
		document.getElementById('status').innerHTML = "Email cannot be empty";
		return false;
	} else {
		var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
		if(!re.test(email)){
			document.getElementById('status').innerHTML = "Email format invalid";
			return false;
		}
	}
	var subject =  document.getElementById('subject').value;
	if (subject == "") {
		document.getElementById('status').innerHTML = "Subject cannot be empty";
		return false;
	}
	var message =  document.getElementById('message').value;
	if (message == "") {
		document.getElementById('status').innerHTML = "Message cannot be empty";
		return false;
	}
	document.getElementById('status').innerHTML = "Sending...";
	document.getElementById('contact-form').submit();
	
}
