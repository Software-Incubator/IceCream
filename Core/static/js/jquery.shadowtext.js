/*jslint devel: true, bitwise: true, regexp: true, browser: true, confusion: true, unparam: true, eqeq: true, white: true, nomen: true, plusplus: true, maxerr: 50, indent: 4 */
/*globals jQuery */

/*!
 * ShadowText
 *
 * Copyright (c) 2011-2015 Martijn W. van der Lee
 * Licensed under the MIT.
 */
/* Creates shadow text that follows the mouse pointer.
 */

(function($, undefined) {
	$.widget('vanderlee.shadowtext', {
		options: {
			axis:			'',		// 'x', 'y'
			blurClose:		0,
			blurFar:		10,
			color:			"#000000",
			distance: 		10,
			easing:			'',
			framerate:		25,
			hideText:		false,
			mouseRange:		500,
			opacityClose:	1,
			opacityFar:		1
		},
		
		_$shadow: null,
		_$original: null,
		_$symbols: null,

		_create: function() {						
			var self	= this,
				html	= this.element.html(),
				left	= this.element.position().left,
				top		= this.element.position().top,
				offset	= this.element.offset();
		
			this.option(this.options);

			this._span(this.element);
			this.element.wrapInner('<span class="vanderlee-shadowtext-shadow" style="display:inline-block"/>');
			this._$shadow = this.element.children().first();	
			
			if (!this.options.hideText) {
				this._$original = $('<span class="vanderlee-shadowtext-original" style="position:absolute">'+html+'</span>').appendTo(this.element);				
			}

			$('html').mousemove(function(event) {
				self._animate(event.pageX, event.pageY);
			});
			
			this._animate(offset.left, offset.top);

			return this;
		},

		_span: function(element) {
			var self = this;

			if (element.nodeType === 3) {
				var chars = '';
				for (var x = 0; x < element.data.length; ++x) {
					chars += '<span class="vanderlee-shadowtext-symbol" style="color:transparent;">'+element.data.charAt(x)+'</span>';
				}
				$(element).after(chars);
				element.data = '';
			} else {
				$(element).contents().each( function() { self._span(this); } );
			}
			
			this._$symbols = $('.vanderlee-shadowtext-symbol', this.element);
		},	

		_scale: function(n, from_min, from_max, to_min, to_max) {
			return ((n - from_min) * (to_max - to_min) / (from_max - from_min)) + to_min;
		},

		_toPixels: function(size) {
			if		(size == '0')				return 0;	
			else if (parseFloat(size) == size)	return size;
			else if ($.fn.px)					return $(this.element).px(size);
			else								return size;
		},

		_ease: function(method, fraction) {
			return fraction >= 0? $.easing[method](null, fraction, 0, 1, 1)
								: -$.easing[method](null, -fraction, 0, 1, 1);	
		},

		_animationTimer: 0,
		
		_animate: function(x, y) {
			var self = this,
				time = new Date().getTime();
		
			// Limit number of frames-per-second
			if (time < this._animationTimer + (1000 / this.options.frameTime)) {
				return;
			}
			this._animationTimer = time;		

			// px corrected
			var o_range		= this._toPixels(this.options.mouseRange),
				o_distance	= this._toPixels(this.options.distance),
				o_blurClose	= this._toPixels(this.options.blurClose),
				o_blurFar	= this._toPixels(this.options.blurFar),
				position	= this._$shadow.position();

			if (this._$original) {
				this._$original.css('left', position.left).css('top', position.top);
			}

			this._$symbols.each(function(index) {		
				var	height		= $(this).height() * -.5,
					width		= $(this).width() * -.5,
					offset		= $(this).offset(),
					shadow_x	= self.options.axis != 'y'? (offset.left - x - width) / o_range : 0,
					shadow_y	= self.options.axis != 'x'? (offset.top  - y - height) / o_range : 0,
					distance	= Math.sqrt((shadow_x * shadow_x) + (shadow_y * shadow_y));
						
				if (distance > 1.) {
					var scale = 1. / distance;
					shadow_x *= scale;
					shadow_y *= scale;
					distance *= scale;
				}

				// apply easing
				if (self.options.easing) {
					shadow_x = self._ease(self.options.easing, shadow_x);
					shadow_y = self._ease(self.options.easing, shadow_y);
					distance = self._ease(self.options.easing, distance);
				}

				var radius		= self._scale(distance, 0, 1, o_blurClose, o_blurFar),
					opacity		= self._scale(distance, 0, 1, self.options.opacityClose, self.options.opacityFar),
					rgb			= self._colorToRGB(self.options.color);
					
				$(this).css('text-shadow',	(shadow_x * o_distance)+'px '
										+	(shadow_y * o_distance)+'px '
										+	radius+'px '
										+	'rgba('+rgb+','+opacity+')');
			});
		},

		/* Based on FLOT/jquery.colorhelpers.js
		 * Released under the MIT license by Ole Laursen, October 2009.
		 */
		_colorToRGB: function(color) {
			var m;

			// Look for #a0b1c2
			if (m = /^#([a-fA-F0-9]{2})([a-fA-F0-9]{2})([a-fA-F0-9]{2})$/.exec(color)) {
				return [parseInt(m[1], 16), parseInt(m[2], 16), parseInt(m[3], 16)];
			}

			// Look for #fff
			if (m = /^#([a-fA-F0-9])([a-fA-F0-9])([a-fA-F0-9])$/.exec(color)) {
				return [parseInt(m[1]+m[1], 16), parseInt(m[2]+m[2], 16), parseInt(m[3]+m[3], 16)];
			}

			// rgb{a}(#,#,#{,#})
			if (m = /^rgba?\(\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*(?:,\s*([0-9]+(?:\.[0-9]+)?)\s*)?\)$/.exec(color)) {
				return m.slice(1,4);
			}

			// rgb{a}(%,%,%{,%})
			if (m = /^rgba?\(\s*([0-9]+(?:\.[0-9]+)?)\%\s*,\s*([0-9]+(?:\.[0-9]+)?)\%\s*,\s*([0-9]+(?:\.[0-9]+)?)\%\s*(?:,\s*([0-9]+(?:\.[0-9]+)?)\s*)?\)$/.exec(color)) {
				return [parseFloat(m[1]) * 2.55, parseFloat(m[2]) * 2.55, parseFloat(m[3]) * 2.55];
			}

			// Otherwise, we're most likely dealing with a named color
			var name = $.trim(color).toLowerCase();
			return name === 'transparent' ? [255, 255, 255] : this.colors[name];
		},

		colors: {
			aqua:			[0,255,255],
			azure:			[240,255,255],
			beige:			[245,245,220],
			black:			[0,0,0],
			blue:			[0,0,255],
			brown:			[165,42,42],
			cyan:			[0,255,255],
			darkblue:		[0,0,139],
			darkcyan:		[0,139,139],
			darkgrey:		[169,169,169],
			darkgreen:		[0,100,0],
			darkkhaki:		[189,183,107],
			darkmagenta:	[139,0,139],
			darkolivegreen:	[85,107,47],
			darkorange:		[255,140,0],
			darkorchid:		[153,50,204],
			darkred:		[139,0,0],
			darksalmon:		[233,150,122],
			darkviolet:		[148,0,211],
			fuchsia:		[255,0,255],
			gold:			[255,215,0],
			green:			[0,128,0],
			indigo:			[75,0,130],
			khaki:			[240,230,140],
			lightblue:		[173,216,230],
			lightcyan:		[224,255,255],
			lightgreen:		[144,238,144],
			lightgrey:		[211,211,211],
			lightpink:		[255,182,193],
			lightyellow:	[255,255,224],
			lime:			[0,255,0],
			magenta:		[255,0,255],
			maroon:			[128,0,0],
			navy:			[0,0,128],
			olive:			[128,128,0],
			orange:			[255,165,0],
			pink:			[255,192,203],
			purple:			[128,0,128],
			violet:			[128,0,128],
			red:			[255,0,0],
			silver:			[192,192,192],
			white:			[255,255,255],
			yellow:			[255,255,0]
		}
	});
})(jQuery);