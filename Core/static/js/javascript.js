function collapseNavbar() {
    if ($('.navbar')['offset']()['top'] > 500) {
        $('.navbar-fixed-top')['addClass']('top-nav-collapse')
    } else {
        $('.navbar-fixed-top')['removeClass']('top-nav-collapse')
    }
}

function validate_name() {
    var _0xce37x3 = document['getElementById']('exampleInputName1');
    var _0xce37x4 = document['getElementById']('exampleInputEmail1');
    var _0xce37x5 = /^[a-zA-Z]*$/;
    if (!_0xce37x5['test'](_0xce37x3['value'])) {
        alert('Please enter valid name')
    }
}

function validate_contact() {
    var _0xce37x4 = document['getElementById']('exampleInputcontact1');
    var _0xce37x5 = /^[7-9][0-9]{9}$/;
    if (!_0xce37x5['test'](_0xce37x4['value'])) {
        alert('invalid contact no')
    }
}

function validate_student_no() {
    var _0xce37x8 = document['getElementById']('exampleInputstudent1');
    var _0xce37x5 = /^[1][5-6]\d{5}$/;
    if (!_0xce37x5['test'](_0xce37x8['value'])) {
        alert('invalid student no')
    }
}
$(window)['scroll'](collapseNavbar);
$(document)['ready'](collapseNavbar);
$(function() {
    $('a.page-scroll')['bind']('click', function(_0xce37x9) {
        var _0xce37xa = $(this);
        $('html, body')['stop']()['animate']({
            scrollTop: $(_0xce37xa['attr']('href'))['offset']()['top']
        }, 1500, 'easeInOutExpo');
        _0xce37x9['preventDefault']()
    })
});
$('.navbar-collapse ul li a')['click'](function() {
    if ($(this)['attr']('class') != 'dropdown-toggle active' && $(this)['attr']('class') != 'dropdown-toggle') {
        $('.navbar-toggle:visible')['click']()
    }
});
jQuery['easing']['jswing'] = jQuery['easing']['swing'];
jQuery['extend'](jQuery['easing'], {
    def: 'easeOutQuad',
    swing: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return jQuery['easing'][jQuery['easing']['def']](_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf)
    },
    easeInQuad: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return _0xce37xe * (_0xce37xc /= _0xce37xf) * _0xce37xc + _0xce37xd
    },
    easeOutQuad: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return -_0xce37xe * (_0xce37xc /= _0xce37xf) * (_0xce37xc - 2) + _0xce37xd
    },
    easeInOutQuad: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        if ((_0xce37xc /= _0xce37xf / 2) < 1) {
            return _0xce37xe / 2 * _0xce37xc * _0xce37xc + _0xce37xd
        };
        return -_0xce37xe / 2 * ((--_0xce37xc) * (_0xce37xc - 2) - 1) + _0xce37xd
    },
    easeInCubic: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return _0xce37xe * (_0xce37xc /= _0xce37xf) * _0xce37xc * _0xce37xc + _0xce37xd
    },
    easeOutCubic: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return _0xce37xe * ((_0xce37xc = _0xce37xc / _0xce37xf - 1) * _0xce37xc * _0xce37xc + 1) + _0xce37xd
    },
    easeInOutCubic: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        if ((_0xce37xc /= _0xce37xf / 2) < 1) {
            return _0xce37xe / 2 * _0xce37xc * _0xce37xc * _0xce37xc + _0xce37xd
        };
        return _0xce37xe / 2 * ((_0xce37xc -= 2) * _0xce37xc * _0xce37xc + 2) + _0xce37xd
    },
    easeInQuart: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return _0xce37xe * (_0xce37xc /= _0xce37xf) * _0xce37xc * _0xce37xc * _0xce37xc + _0xce37xd
    },
    easeOutQuart: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return -_0xce37xe * ((_0xce37xc = _0xce37xc / _0xce37xf - 1) * _0xce37xc * _0xce37xc * _0xce37xc - 1) + _0xce37xd
    },
    easeInOutQuart: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        if ((_0xce37xc /= _0xce37xf / 2) < 1) {
            return _0xce37xe / 2 * _0xce37xc * _0xce37xc * _0xce37xc * _0xce37xc + _0xce37xd
        };
        return -_0xce37xe / 2 * ((_0xce37xc -= 2) * _0xce37xc * _0xce37xc * _0xce37xc - 2) + _0xce37xd
    },
    easeInQuint: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return _0xce37xe * (_0xce37xc /= _0xce37xf) * _0xce37xc * _0xce37xc * _0xce37xc * _0xce37xc + _0xce37xd
    },
    easeOutQuint: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return _0xce37xe * ((_0xce37xc = _0xce37xc / _0xce37xf - 1) * _0xce37xc * _0xce37xc * _0xce37xc * _0xce37xc + 1) + _0xce37xd
    },
    easeInOutQuint: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        if ((_0xce37xc /= _0xce37xf / 2) < 1) {
            return _0xce37xe / 2 * _0xce37xc * _0xce37xc * _0xce37xc * _0xce37xc * _0xce37xc + _0xce37xd
        };
        return _0xce37xe / 2 * ((_0xce37xc -= 2) * _0xce37xc * _0xce37xc * _0xce37xc * _0xce37xc + 2) + _0xce37xd
    },
    easeInSine: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return -_0xce37xe * Math['cos'](_0xce37xc / _0xce37xf * (Math['PI'] / 2)) + _0xce37xe + _0xce37xd
    },
    easeOutSine: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return _0xce37xe * Math['sin'](_0xce37xc / _0xce37xf * (Math['PI'] / 2)) + _0xce37xd
    },
    easeInOutSine: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return -_0xce37xe / 2 * (Math['cos'](Math['PI'] * _0xce37xc / _0xce37xf) - 1) + _0xce37xd
    },
    easeInExpo: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return (_0xce37xc == 0) ? _0xce37xd : _0xce37xe * Math['pow'](2, 10 * (_0xce37xc / _0xce37xf - 1)) + _0xce37xd
    },
    easeOutExpo: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return (_0xce37xc == _0xce37xf) ? _0xce37xd + _0xce37xe : _0xce37xe * (-Math['pow'](2, -10 * _0xce37xc / _0xce37xf) + 1) + _0xce37xd
    },
    easeInOutExpo: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        if (_0xce37xc == 0) {
            return _0xce37xd
        };
        if (_0xce37xc == _0xce37xf) {
            return _0xce37xd + _0xce37xe
        };
        if ((_0xce37xc /= _0xce37xf / 2) < 1) {
            return _0xce37xe / 2 * Math['pow'](2, 10 * (_0xce37xc - 1)) + _0xce37xd
        };
        return _0xce37xe / 2 * (-Math['pow'](2, -10 * --_0xce37xc) + 2) + _0xce37xd
    },
    easeInCirc: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return -_0xce37xe * (Math['sqrt'](1 - (_0xce37xc /= _0xce37xf) * _0xce37xc) - 1) + _0xce37xd
    },
    easeOutCirc: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return _0xce37xe * Math['sqrt'](1 - (_0xce37xc = _0xce37xc / _0xce37xf - 1) * _0xce37xc) + _0xce37xd
    },
    easeInOutCirc: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        if ((_0xce37xc /= _0xce37xf / 2) < 1) {
            return -_0xce37xe / 2 * (Math['sqrt'](1 - _0xce37xc * _0xce37xc) - 1) + _0xce37xd
        };
        return _0xce37xe / 2 * (Math['sqrt'](1 - (_0xce37xc -= 2) * _0xce37xc) + 1) + _0xce37xd
    },
    easeInElastic: function(_0xce37xc, _0xce37xe, _0xce37xb, _0xce37x10, _0xce37x11) {
        var _0xce37x12 = 1.70158;
        var _0xce37x13 = 0;
        var _0xce37xf = _0xce37x10;
        if (_0xce37xe == 0) {
            return _0xce37xb
        };
        if ((_0xce37xe /= _0xce37x11) == 1) {
            return _0xce37xb + _0xce37x10
        };
        if (!_0xce37x13) {
            _0xce37x13 = _0xce37x11 * 0.3
        };
        if (_0xce37xf < Math['abs'](_0xce37x10)) {
            _0xce37xf = _0xce37x10;
            var _0xce37x12 = _0xce37x13 / 4
        } else {
            var _0xce37x12 = _0xce37x13 / (2 * Math['PI']) * Math['asin'](_0xce37x10 / _0xce37xf)
        };
        return -(_0xce37xf * Math['pow'](2, 10 * (_0xce37xe -= 1)) * Math['sin']((_0xce37xe * _0xce37x11 - _0xce37x12) * (2 * Math['PI']) / _0xce37x13)) + _0xce37xb
    },
    easeOutElastic: function(_0xce37xc, _0xce37xe, _0xce37xb, _0xce37x10, _0xce37x11) {
        var _0xce37x12 = 1.70158;
        var _0xce37x13 = 0;
        var _0xce37xf = _0xce37x10;
        if (_0xce37xe == 0) {
            return _0xce37xb
        };
        if ((_0xce37xe /= _0xce37x11) == 1) {
            return _0xce37xb + _0xce37x10
        };
        if (!_0xce37x13) {
            _0xce37x13 = _0xce37x11 * 0.3
        };
        if (_0xce37xf < Math['abs'](_0xce37x10)) {
            _0xce37xf = _0xce37x10;
            var _0xce37x12 = _0xce37x13 / 4
        } else {
            var _0xce37x12 = _0xce37x13 / (2 * Math['PI']) * Math['asin'](_0xce37x10 / _0xce37xf)
        };
        return _0xce37xf * Math['pow'](2, -10 * _0xce37xe) * Math['sin']((_0xce37xe * _0xce37x11 - _0xce37x12) * (2 * Math['PI']) / _0xce37x13) + _0xce37x10 + _0xce37xb
    },
    easeInOutElastic: function(_0xce37xc, _0xce37xe, _0xce37xb, _0xce37x10, _0xce37x11) {
        var _0xce37x12 = 1.70158;
        var _0xce37x13 = 0;
        var _0xce37xf = _0xce37x10;
        if (_0xce37xe == 0) {
            return _0xce37xb
        };
        if ((_0xce37xe /= _0xce37x11 / 2) == 2) {
            return _0xce37xb + _0xce37x10
        };
        if (!_0xce37x13) {
            _0xce37x13 = _0xce37x11 * (0.3 * 1.5)
        };
        if (_0xce37xf < Math['abs'](_0xce37x10)) {
            _0xce37xf = _0xce37x10;
            var _0xce37x12 = _0xce37x13 / 4
        } else {
            var _0xce37x12 = _0xce37x13 / (2 * Math['PI']) * Math['asin'](_0xce37x10 / _0xce37xf)
        };
        if (_0xce37xe < 1) {
            return -0.5 * (_0xce37xf * Math['pow'](2, 10 * (_0xce37xe -= 1)) * Math['sin']((_0xce37xe * _0xce37x11 - _0xce37x12) * (2 * Math['PI']) / _0xce37x13)) + _0xce37xb
        };
        return _0xce37xf * Math['pow'](2, -10 * (_0xce37xe -= 1)) * Math['sin']((_0xce37xe * _0xce37x11 - _0xce37x12) * (2 * Math['PI']) / _0xce37x13) * 0.5 + _0xce37x10 + _0xce37xb
    },
    easeInBack: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37x12, _0xce37xe, _0xce37xf) {
        if (_0xce37xf == undefined) {
            _0xce37xf = 1.70158
        };
        return _0xce37x12 * (_0xce37xc /= _0xce37xe) * _0xce37xc * ((_0xce37xf + 1) * _0xce37xc - _0xce37xf) + _0xce37xd
    },
    easeOutBack: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37x12, _0xce37xe, _0xce37xf) {
        if (_0xce37xf == undefined) {
            _0xce37xf = 1.70158
        };
        return _0xce37x12 * ((_0xce37xc = _0xce37xc / _0xce37xe - 1) * _0xce37xc * ((_0xce37xf + 1) * _0xce37xc + _0xce37xf) + 1) + _0xce37xd
    },
    easeInOutBack: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37x12, _0xce37xe, _0xce37xf) {
        if (_0xce37xf == undefined) {
            _0xce37xf = 1.70158
        };
        if ((_0xce37xc /= _0xce37xe / 2) < 1) {
            return _0xce37x12 / 2 * (_0xce37xc * _0xce37xc * (((_0xce37xf *= (1.525)) + 1) * _0xce37xc - _0xce37xf)) + _0xce37xd
        };
        return _0xce37x12 / 2 * ((_0xce37xc -= 2) * _0xce37xc * (((_0xce37xf *= (1.525)) + 1) * _0xce37xc + _0xce37xf) + 2) + _0xce37xd
    },
    easeInBounce: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        return _0xce37xe - jQuery['easing']['easeOutBounce'](_0xce37xb, _0xce37xf - _0xce37xc, 0, _0xce37xe, _0xce37xf) + _0xce37xd
    },
    easeOutBounce: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        if ((_0xce37xc /= _0xce37xf) < (1 / 2.75)) {
            return _0xce37xe * (7.5625 * _0xce37xc * _0xce37xc) + _0xce37xd
        } else {
            if (_0xce37xc < (2 / 2.75)) {
                return _0xce37xe * (7.5625 * (_0xce37xc -= (1.5 / 2.75)) * _0xce37xc + 0.75) + _0xce37xd
            } else {
                if (_0xce37xc < (2.5 / 2.75)) {
                    return _0xce37xe * (7.5625 * (_0xce37xc -= (2.25 / 2.75)) * _0xce37xc + 0.9375) + _0xce37xd
                } else {
                    return _0xce37xe * (7.5625 * (_0xce37xc -= (2.625 / 2.75)) * _0xce37xc + 0.984375) + _0xce37xd
                }
            }
        }
    },
    easeInOutBounce: function(_0xce37xb, _0xce37xc, _0xce37xd, _0xce37xe, _0xce37xf) {
        if (_0xce37xc < _0xce37xf / 2) {
            return jQuery['easing']['easeInBounce'](_0xce37xb, _0xce37xc * 2, 0, _0xce37xe, _0xce37xf) * 0.5 + _0xce37xd
        };
        return jQuery['easing']['easeOutBounce'](_0xce37xb, _0xce37xc * 2 - _0xce37xf, 0, _0xce37xe, _0xce37xf) * 0.5 + _0xce37xe * 0.5 + _0xce37xd
    }
});
$(window)['load'](function() {
    $('.se-pre-con')['fadeOut']('slow');;
});
$['fn']['moveIt'] = function() {
    var _0xce37x14 = $(window);
    var _0xce37x15 = [];
    $(this)['each'](function() {
        _0xce37x15['push'](new moveItItem($(this)))
    });
    window['onscroll'] = function() {
        var _0xce37x16 = _0xce37x14['scrollTop']();
        _0xce37x15['forEach'](function(_0xce37x17) {
            _0xce37x17['update'](_0xce37x16)
        })
    }
};
var moveItItem = function(_0xce37x19) {
    this['el'] = $(_0xce37x19);
    this['speed'] = parseInt(this['el']['attr']('data-scroll-speed'))
};
moveItItem['prototype']['update'] = function(_0xce37x16) {
    var _0xce37x1a = _0xce37x16 / this['speed'];
    this['el']['css']('transform', 'translateY(' + -_0xce37x1a + 'px)')
};
$(function() {
    $('[data-scroll-speed]')['moveIt']()
});
$(document)['ready'](function() {
    $(window)['scroll'](function() {
        $('#snackbar')['hide']()
    })
})


$(function () {

    var $body = $(document);
    $body.bind('scroll', function () {
        // "Disable" the horizontal scroll.
        if ($body.scrollLeft() !== 0) {
            $body.scrollLeft(0);
        }
    });

});