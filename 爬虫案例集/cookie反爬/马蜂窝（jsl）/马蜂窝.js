function get_enviroment(proxy_array) {
    for(var i=0; i<proxy_array.length; i++){
        handler = '{\n' +
            '    get: function(target, property, receiver) {\n' +
            '        console.log("方法:", "get  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return target[property];\n' +
            '    },\n' +
            '    set: function(target, property, value, receiver) {\n' +
            '        console.log("方法:", "set  ", "对象:", ' +
            '"' + proxy_array[i] + '" ,' +
            '"  属性:", property, ' +
            '"  属性类型:", ' + 'typeof property, ' +
            // '"  属性值:", ' + 'target[property], ' +
            '"  属性值类型:", typeof target[property]);\n' +
            '        return Reflect.set(...arguments);\n' +
            '    }\n' +
            '}'
        eval('try{\n' + proxy_array[i] + ';\n'
        + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}catch (e) {\n' + proxy_array[i] + '={};\n'
        + proxy_array[i] + '=new Proxy(' + proxy_array[i] + ', ' + handler + ')}')
    }
}
proxy_array = ['window', 'document', 'location', 'navigator', 'history','screen']

window=global
 navigator={
    appCodeName: "Mozilla",
     appName:"Netscape",
appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
language: "zh-CN",
userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",

 }
 document={}
location={}

get_enviroment(proxy_array)

    var _0x44bc = ['WMOVGVc=', 'w5h5wrfCiA==', 'b8OXwoIn', 'GMOjw63DuA==', 'IHxVTg==', 'w5lCwozCgA==', 'GUXDm30=', 'WsKkTMKf', 'DcObFMOo', 'wrXDpEEs', 'B0F6CA==', 'KQ4tw4I=', 'az3CpQk=', 'bsK9wprClg==', 'wq9/w5PCkg==', 'asKqwozCgw==', 'DcOhccKZ', 'HMOHw57DgA==', 'SMKBw6Ar', 'KcOvZ8Kb', 'c8OSOiM=', 'wr/DmsKZwqU=', 'w7rDgcKmEA==', 'UC42Tg==', 'w7MQwqwi', 'w5s4wqw8', 'UyrDoD8=', 'EycpXA==', 'wqzDvWtX', 'XDXDtSg=', 'JcOZEkE=', 'TsKqwp7ClA==', 'wq7DsVok', 'wqDDv3DCtA==', 'VzDDrwk=', 'w5RqwpHCqQ==', 'VUBHDA==', 'PWt8fA==', 'dXl4KQ==', 'IsOdB8Oz', 'WXBqGw==', 'L8KfUgs=', 'fwvDug0=', 'fm54Cg==', 'AB/Co0k=', 'FHZoQQ==', 'KS0kfQ==', 'OxvCm8O8', 'w4bDvMK5w6M=', 'dxfDhC8=', 'w6jDucKRw4g=', 'CMO8N8O0', 'PcKSaiU=', 'w6LDpsKUw5I=', 'CMO2UMKy', 'wphocg==', 'w5MtwqYH', 'RgLDu8OV', 'UcOkTFM=', 'w5A2w6w=', 'w4vDu8OlTQ==', 'EnXCl8Oo', 'w4kYwrY1', 'w6DDmsO9bA==', 'Y8OkOQg=', 'w607wrQc', 'VWAtRQ==', 'w7lIwpPCvw==', 'w5sYwoAD', 'w6pnwojCrQ==', 'JxwUw5A=', 'w57Dh8KPMA==', 'acO/LRk=', 'w5csw6PDqQ==', 'HBdTWA==', 'w4XDgcO+dA==', 'DMKrTzI=', 'MsOJDMK1', 'w497wocL', 'wrDDint4', 'TUVzOQ==', 'wovDtHVK', '6K6T5rOs6aup6K2Y', 'wqPDqloi', 'HMOzP8K0', 'wq3DnsKAZQ==', 'PsKUw5V8', 'w4E8w7g7', 'HCpjUQ==', 'CRbChcOF', 'RgvCsyM=', 'w7bDqsOKQQ==', 'M8OwGUE=', 'EcKIU8Ox', 'NMOsLMK2', 'w7FiwovCiw==', 'aXN9ew==', 'MsKQw7tc', 'wpvCv8OOwpU=', 'CsKcegk=', 'wr/Cm2DDhg==', 'AWdiXA==', 'w73DlsKtw54=', 'SxXCpXo=', 'VsKOw60n', 'aUrCoMK6', 'w7NxwpUE', 'wo5GYgs=', 'wqLDsUY=', 'ccKrw6E=', 'B8OeCcKs', 'F8ObB8Oq', 'VsO3T8O4', 'wokuwp3DiQ==', 'wqzDk8KMwr8=', 'ExYpw58=', 'w4jDiMOpbw==', 'w5ENwpAg', 'FsOBV8KZ', 'IMODJ8Of', 'wqTDjWjCmQ==', 'wpXDucODEQ==', 'W8Kpw6wI', 'wpHDqsOkAA==', 'wqnDq1Es', 'J3p7bA==', 'OMKOFH0=', 'w5dTwqop', 'wrHDksKLZw==', 'w6pLwrc+', 'CsKIcsOH', 'w5PDtcKKOw==', 'RlhKQQ==', 'DsK7ZsOe', 'PcKkSsOo', 'A8KAw4V5', 'LsKGPVo=', 'bVzCq8KY', 'HcOsw43DrQ==', 'w4fDq8KSw4E=', 'Y8OTEHk=', 'wovDmVhP', 'w4lqwrlM', 'RRvCqWU=', 'FEfCt8Ok', 'elTCuD4=', 'w5Ydwqox', 'MHrCk8O0', 'OMKLHXc=', 'wpzDs2vCkw==', 'MmXDv2s=', 'R8KGwrXCgA==', 'LztzdQ==', 'w5Yyw7nDlg==', 'RVrDtHA=', 'PHzCl8K9', 'wonDrV09', 'F8OBN8Ki', 'dMKkwofCvA==', 'LsKOH1g=', 'ZAnDqcOJ', 'wrFvUiU=', 'wonDj8OVKQ==', 'woTDuVnClA==', 'Dgczw58=', 'woLDksKTYQ==', 'w4Vuwp7Cug==', 'WMOCDws=', 'G8KMdMO3', 'cBbClX8=', 'XxXDtws=', 'w7rDhsK6w6E=', 'A8OgbcKX', 'JMO7w4XDhw==', 'WCjDj8Ov', 'FyrCq1o=', 'TmZQw7Q=', 'w7nDmcKVw6g=', 'TQnDm2s=', 'FsOhfcKa', 'w4vDrsKyBg==', 'E8OrLcO+', 'S0dKJw==', 'Jw7Cq2I=', 'RjfDrsOh', 'ScOmecOP', 'wrZKYBI=', 'wrXDlk3Cgg==', 'KcKww6x3', 'wpYbwq7Dog==', 'ccK+wrrCqg==', 'bMKZwpjCoQ==', 'wovDh2TCkw==', 'w4Mrw6/Dng==', 'KMKHw5Vi', 'w6c2w6XDvw==', 'w77Dh8Oe', 'fnRx', 'QTnCgWk=', 'Z392w74=', 'LcOHScK2', 'w4rDjMOxYQ==', 'woXDosO0EQ==', 'LTQXw4U=', 'GsKMZsOs', 'wqRVwrIk', 'B8OPasKv', 'FcOaHsO8', 'TWdjw6A='];
    (function(_0x30a8f6, _0x44bc47) {
        var _0x39cbe9 = function(_0x501174) {
            while (--_0x501174) {
                _0x30a8f6['push'](_0x30a8f6['shift']());
            }
        };
        _0x39cbe9(++_0x44bc47);
    }(_0x44bc, 0x130));
    var _0x39cb = function(_0x30a8f6, _0x44bc47) {
        _0x30a8f6 = _0x30a8f6 - 0x0;
        var _0x39cbe9 = _0x44bc[_0x30a8f6];
        if (_0x39cb['MAKdeh'] === undefined) {
            (function() {
                var _0x1c5bae = function() {
                    var _0x27a0d7;
                    try {
                        _0x27a0d7 = Function('return\x20(function()\x20' + '{}.constructor(\x22return\x20this\x22)(\x20)' + ');')();
                    } catch (_0x351f08) {
                        _0x27a0d7 = window;
                    }
                    return _0x27a0d7;
                };
                var _0x4b8bb0 = _0x1c5bae();
                var _0x3a4562 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
                _0x4b8bb0['atob'] || (_0x4b8bb0['atob'] = function(_0x1dc269) {
                    var _0x27af0f = String(_0x1dc269)['replace'](/=+$/, '');
                    var _0x547589 = '';
                    for (var _0x260b11 = 0x0, _0x4446f0, _0x2ed7c1, _0x42e640 = 0x0; _0x2ed7c1 = _0x27af0f['charAt'](_0x42e640++); ~_0x2ed7c1 && (_0x4446f0 = _0x260b11 % 0x4 ? _0x4446f0 * 0x40 + _0x2ed7c1 : _0x2ed7c1,
                    _0x260b11++ % 0x4) ? _0x547589 += String['fromCharCode'](0xff & _0x4446f0 >> (-0x2 * _0x260b11 & 0x6)) : 0x0) {
                        _0x2ed7c1 = _0x3a4562['indexOf'](_0x2ed7c1);
                    }
                    return _0x547589;
                }
                );
            }());
            var _0x4c921d = function(_0x59a71a, _0x332c2a) {
                var _0xaccd0a = [], _0x13276e = 0x0, _0xe1d744, _0x696231 = '', _0x37bbc3 = '';
                _0x59a71a = atob(_0x59a71a);
                for (var _0x230fd7 = 0x0, _0x102238 = _0x59a71a['length']; _0x230fd7 < _0x102238; _0x230fd7++) {
                    _0x37bbc3 += '%' + ('00' + _0x59a71a['charCodeAt'](_0x230fd7)['toString'](0x10))['slice'](-0x2);
                }
                _0x59a71a = decodeURIComponent(_0x37bbc3);
                var _0x8e14d4;
                for (_0x8e14d4 = 0x0; _0x8e14d4 < 0x100; _0x8e14d4++) {
                    _0xaccd0a[_0x8e14d4] = _0x8e14d4;
                }
                for (_0x8e14d4 = 0x0; _0x8e14d4 < 0x100; _0x8e14d4++) {
                    _0x13276e = (_0x13276e + _0xaccd0a[_0x8e14d4] + _0x332c2a['charCodeAt'](_0x8e14d4 % _0x332c2a['length'])) % 0x100;
                    _0xe1d744 = _0xaccd0a[_0x8e14d4];
                    _0xaccd0a[_0x8e14d4] = _0xaccd0a[_0x13276e];
                    _0xaccd0a[_0x13276e] = _0xe1d744;
                }
                _0x8e14d4 = 0x0;
                _0x13276e = 0x0;
                for (var _0x39ed21 = 0x0; _0x39ed21 < _0x59a71a['length']; _0x39ed21++) {
                    _0x8e14d4 = (_0x8e14d4 + 0x1) % 0x100;
                    _0x13276e = (_0x13276e + _0xaccd0a[_0x8e14d4]) % 0x100;
                    _0xe1d744 = _0xaccd0a[_0x8e14d4];
                    _0xaccd0a[_0x8e14d4] = _0xaccd0a[_0x13276e];
                    _0xaccd0a[_0x13276e] = _0xe1d744;
                    _0x696231 += String['fromCharCode'](_0x59a71a['charCodeAt'](_0x39ed21) ^ _0xaccd0a[(_0xaccd0a[_0x8e14d4] + _0xaccd0a[_0x13276e]) % 0x100]);
                }
                return _0x696231;
            };
            _0x39cb['YzbSKN'] = _0x4c921d;
            _0x39cb['wZYzFk'] = {};
            _0x39cb['MAKdeh'] = !![];
        }
        var _0x501174 = _0x39cb['wZYzFk'][_0x30a8f6];
        if (_0x501174 === undefined) {
            if (_0x39cb['rXkCPM'] === undefined) {
                _0x39cb['rXkCPM'] = !![];
            }
            _0x39cbe9 = _0x39cb['YzbSKN'](_0x39cbe9, _0x44bc47);
            _0x39cb['wZYzFk'][_0x30a8f6] = _0x39cbe9;
        } else {
            _0x39cbe9 = _0x501174;
        }
        return _0x39cbe9;
    };
    function hash(_0x5275b3) {
        var _0x45f980 = {};
        _0x45f980[_0x39cb('0xb4', '!F(m') + 'I'] = function(_0x3f8400, _0x4f7043) {
            return _0x3f8400 ^ _0x4f7043;
        }
        ;
        _0x45f980[_0x39cb('0x96', 'naLL') + 'a'] = _0x39cb('0x3', 'r![p') + _0x39cb('0x74', '1@%v') + _0x39cb('0x53', '6WMO') + _0x39cb('0x1f', '&20#');
        _0x45f980[_0x39cb('0x3e', '@iPt') + 'v'] = function(_0x3f9552, _0x30276c) {
            return _0x3f9552 >= _0x30276c;
        }
        ;
        _0x45f980[_0x39cb('0xd0', '@iPt') + 'i'] = function(_0x2bb04d, _0x5109e2) {
            return _0x2bb04d * _0x5109e2;
        }
        ;
        _0x45f980[_0x39cb('0xf', '@iPt') + 'U'] = _0x39cb('0x89', 'm1O2') + _0x39cb('0x80', 'UO*t') + _0x39cb('0x65', 'AN$h');
        _0x45f980[_0x39cb('0xa8', '*XUD') + 'Y'] = function(_0x48434a, _0x17e967) {
            return _0x48434a << _0x17e967;
        }
        ;
        _0x45f980[_0x39cb('0x44', 'H4@i') + 'K'] = function(_0x38a46c, _0x1107c3) {
            return _0x38a46c - _0x1107c3;
        }
        ;
        _0x45f980[_0x39cb('0x8b', '9WwT') + 'O'] = function(_0x514d23, _0x2d04f6) {
            return _0x514d23 * _0x2d04f6;
        }
        ;
        _0x45f980[_0x39cb('0x85', '*XUD') + 't'] = function(_0x5e5005, _0xd43ccb) {
            return _0x5e5005 & _0xd43ccb;
        }
        ;
        _0x45f980[_0x39cb('0x5c', 'H4@i') + 'E'] = function(_0x2a9f37, _0x16ba52) {
            return _0x2a9f37 * _0x16ba52;
        }
        ;
        _0x45f980[_0x39cb('0x16', 'ep[J') + 'U'] = function(_0x25abee, _0x2075d1) {
            return _0x25abee < _0x2075d1;
        }
        ;
        _0x45f980[_0x39cb('0xb', 'rU8M') + 'Z'] = function(_0xb6eeae, _0x4545ba) {
            return _0xb6eeae >> _0x4545ba;
        }
        ;
        _0x45f980[_0x39cb('0x70', 'RlBI') + 'g'] = function(_0x2cb033, _0x4f53b1) {
            return _0x2cb033 << _0x4f53b1;
        }
        ;
        _0x45f980[_0x39cb('0x62', '870@') + 'B'] = function(_0x4184a9, _0x3d38e2) {
            return _0x4184a9 | _0x3d38e2;
        }
        ;
        _0x45f980[_0x39cb('0x4e', 'O^*8') + 'h'] = function(_0x4d2704, _0x2a3bdf) {
            return _0x4d2704 >>> _0x2a3bdf;
        }
        ;
        _0x45f980[_0x39cb('0xb8', ']bRZ') + 'Y'] = function(_0x1794f7, _0x14ed23) {
            return _0x1794f7 & _0x14ed23;
        }
        ;
        _0x45f980[_0x39cb('0xb9', '*LOk') + 'i'] = function(_0x18f838, _0x28d68b) {
            return _0x18f838 < _0x28d68b;
        }
        ;
        _0x45f980[_0x39cb('0x8f', '6i)$') + 'Z'] = function(_0x509a4a, _0x4e6421) {
            return _0x509a4a & _0x4e6421;
        }
        ;
        _0x45f980[_0x39cb('0x59', 'NNZT') + 'u'] = function(_0x19adca, _0x5e410e) {
            return _0x19adca ^ _0x5e410e;
        }
        ;
        _0x45f980[_0x39cb('0x33', 'ep[J') + 'E'] = function(_0x55b435, _0x1b252a) {
            return _0x55b435 < _0x1b252a;
        }
        ;
        _0x45f980[_0x39cb('0x9', 'q6^v') + 'O'] = function(_0x40e341, _0x3c2fc5, _0x1ae3ee) {
            return _0x40e341(_0x3c2fc5, _0x1ae3ee);
        }
        ;
        _0x45f980[_0x39cb('0x3b', 'v)vS') + 'V'] = function(_0x11a05d, _0x1bb0ff) {
            return _0x11a05d ^ _0x1bb0ff;
        }
        ;
        _0x45f980[_0x39cb('0x29', '&20#') + 'R'] = function(_0x396a30, _0x3b4f7f, _0x3fabdf) {
            return _0x396a30(_0x3b4f7f, _0x3fabdf);
        }
        ;
        _0x45f980[_0x39cb('0x5f', 'MOR!') + 'l'] = function(_0x2a57f6, _0x4a18db, _0x575584) {
            return _0x2a57f6(_0x4a18db, _0x575584);
        }
        ;
        _0x45f980[_0x39cb('0xbf', '@iPt') + 'c'] = function(_0x29a24a, _0x30fcb5, _0x200e51, _0x40a7d2, _0x43e416) {
            return _0x29a24a(_0x30fcb5, _0x200e51, _0x40a7d2, _0x43e416);
        }
        ;
        _0x45f980[_0x39cb('0x28', '1@%v') + 'U'] = function(_0x42f1ec, _0x2a7066) {
            return _0x42f1ec(_0x2a7066);
        }
        ;
        _0x45f980[_0x39cb('0xae', '&@we') + 'h'] = function(_0x5eade1, _0x4cf267, _0x2b0a57) {
            return _0x5eade1(_0x4cf267, _0x2b0a57);
        }
        ;
        _0x45f980[_0x39cb('0x11', 'Xnqx') + 'U'] = function(_0xbed043, _0xcf778f) {
            return _0xbed043 + _0xcf778f;
        }
        ;
        _0x45f980[_0x39cb('0x77', 'UO*t') + 'v'] = function(_0x2063a8, _0x5e3099) {
            return _0x2063a8 + _0x5e3099;
        }
        ;
        _0x45f980[_0x39cb('0xcd', '&@we') + 'X'] = function(_0x16ba38, _0xeeb1c1) {
            return _0x16ba38(_0xeeb1c1);
        }
        ;
        var _0x425f92 = _0x45f980;
        function _0x53821e(_0x296409, _0x5a68e6) {
            return _0x425f92[_0x39cb('0xca', 'm1O2') + 'I']((_0x296409 & 0x7fffffff) + (_0x5a68e6 & 0x7fffffff), _0x296409 & 0x80000000) ^ _0x5a68e6 & 0x80000000;
        }
        function _0x36716a(_0x1b6571) {
            var _0x50cb53 = _0x425f92[_0x39cb('0x5d', '1@%v') + 'a'];
            var _0x5ab5aa = '';
            for (var _0xdde490 = 0x7; _0x425f92[_0x39cb('0x5e', 'Qw&]') + 'v'](_0xdde490, 0x0); _0xdde490--) {
                _0x5ab5aa += _0x50cb53[_0x39cb('0xbd', '&@we') + 'At'](_0x1b6571 >> _0x425f92[_0x39cb('0x75', 'O^*8') + 'i'](_0xdde490, 0x4) & 0xf);
            }
            return _0x5ab5aa;
        }
        function _0x3bb9e9(_0x5eda56) {
            var _0x5bf38c = _0x425f92[_0x39cb('0xbc', 'm1O2') + 'U'][_0x39cb('0x14', ']bRZ') + 't']('|');
            var _0xef19a9 = 0x0;
            while (!![]) {
                switch (_0x5bf38c[_0xef19a9++]) {
                case '0':
                    for (_0xf6328b = 0x0; _0xf6328b < _0x5eda56[_0x39cb('0x2c', 'r![p') + 'th']; _0xf6328b++) {
                        _0x4fc478[_0xf6328b >> 0x2] |= _0x425f92[_0x39cb('0x2', '1@%v') + 'Y'](_0x5eda56[_0x39cb('0x34', 'i@nW') + _0x39cb('0x64', '870@') + 'At'](_0xf6328b), _0x425f92[_0x39cb('0x37', '6WMO') + 'K'](0x18, _0x425f92[_0x39cb('0x24', '*LOk') + 'O'](_0x425f92[_0x39cb('0x61', 'H4@i') + 't'](_0xf6328b, 0x3), 0x8)));
                    }
                    continue;
                case '1':
                    _0x4fc478[_0x425f92[_0x39cb('0x88', '*LOk') + 'K'](_0x425f92[_0x39cb('0x4a', 'X)t)') + 'E'](_0x54dbde, 0x10), 0x1)] = _0x425f92[_0x39cb('0x55', '*LOk') + 'E'](_0x5eda56[_0x39cb('0x98', 'I80D') + 'th'], 0x8);
                    continue;
                case '2':
                    for (var _0xf6328b = 0x0; _0x425f92[_0x39cb('0x2b', 'O^*8') + 'U'](_0xf6328b, _0x54dbde * 0x10); _0xf6328b++) {
                        _0x4fc478[_0xf6328b] = 0x0;
                    }
                    continue;
                case '3':
                    return _0x4fc478;
                case '4':
                    var _0x54dbde = _0x425f92[_0x39cb('0xb', 'rU8M') + 'Z'](_0x5eda56[_0x39cb('0x6a', '&@we') + 'th'] + 0x8, 0x6) + 0x1
                      , _0x4fc478 = new Array(_0x54dbde * 0x10);
                    continue;
                case '5':
                    _0x4fc478[_0x425f92[_0x39cb('0x4f', 'NNZT') + 'Z'](_0xf6328b, 0x2)] |= _0x425f92[_0x39cb('0xc2', 'naLL') + 'g'](0x80, _0x425f92[_0x39cb('0x58', 'I^*m') + 'K'](0x18, _0x425f92[_0x39cb('0x1a', 'q8jq') + 'E'](_0x425f92[_0x39cb('0x20', 'rU8M') + 't'](_0xf6328b, 0x3), 0x8)));
                    continue;
                }
                break;
            }
        }
        function _0x4327a5(_0x468d07, _0x530e98) {
            return _0x425f92[_0x39cb('0x94', 'Yf27') + 'B'](_0x468d07 << _0x530e98, _0x425f92[_0x39cb('0x12', 'Qw&]') + 'h'](_0x468d07, _0x425f92[_0x39cb('0x67', 'X)t)') + 'K'](0x20, _0x530e98)));
        }
        function _0x18a523(_0x130d23, _0x19f8e8, _0x5b9da7, _0x188afd) {
            if (_0x425f92[_0x39cb('0x51', 'tu8V') + 'U'](_0x130d23, 0x14))
                return _0x425f92[_0x39cb('0x7e', '9Nn4') + 'Y'](_0x19f8e8, _0x5b9da7) | _0x425f92[_0x39cb('0x73', 'UO*t') + 'Y'](~_0x19f8e8, _0x188afd);
            if (_0x130d23 < 0x28)
                return _0x425f92[_0x39cb('0xba', '^9MV') + 'I'](_0x19f8e8 ^ _0x5b9da7, _0x188afd);
            if (_0x425f92[_0x39cb('0x93', 'H4@i') + 'i'](_0x130d23, 0x3c))
                return _0x425f92[_0x39cb('0x2a', 'v#5&') + 'B'](_0x425f92[_0x39cb('0x9d', 'I80D') + 'B'](_0x425f92[_0x39cb('0x76', 'eqcG') + 'Y'](_0x19f8e8, _0x5b9da7), _0x425f92[_0x39cb('0x60', 'MOR!') + 'Z'](_0x19f8e8, _0x188afd)), _0x5b9da7 & _0x188afd);
            return _0x425f92[_0x39cb('0x7a', 'RlBI') + 'u'](_0x19f8e8 ^ _0x5b9da7, _0x188afd);
        }
        function _0x26fbbb(_0x19ee7a) {
            return _0x425f92[_0x39cb('0xa7', 'r![p') + 'E'](_0x19ee7a, 0x14) ? 0x5a827999 : _0x425f92[_0x39cb('0x7d', ']bRZ') + 'E'](_0x19ee7a, 0x28) ? 0x6ed9eba1 : _0x425f92[_0x39cb('0x3d', 'aDie') + 'E'](_0x19ee7a, 0x3c) ? -0x70e44324 : -0x359d3e2a;
        }
        var _0x29e735 = _0x3bb9e9(_0x5275b3);
        var _0x584e5d = new Array(0x50);
        var _0x1eb8bc = 0x67452301;
        var _0x43e6ce = -0x10325477;
        var _0x3b0b87 = -0x67452302;
        var _0x5114f4 = 0x10325476;
        var _0x1f1b08 = -0x3c2d1e10;
        for (var _0x27b1ea = 0x0; _0x425f92[_0x39cb('0x9c', '6i)$') + 'E'](_0x27b1ea, _0x29e735[_0x39cb('0x21', 'h#hd') + 'th']); _0x27b1ea += 0x10) {
            var _0x2f0701 = (_0x39cb('0xac', 'ghwH') + _0x39cb('0x9e', '6i)$') + _0x39cb('0x2f', '9WwT') + _0x39cb('0x5', 'H4@i') + _0x39cb('0x32', 'X)t)') + '|1')[_0x39cb('0x9f', 'eqcG') + 't']('|');
            var _0x5f2e1f = 0x0;
            while (!![]) {
                switch (_0x2f0701[_0x5f2e1f++]) {
                case '0':
                    _0x43e6ce = _0x53821e(_0x43e6ce, _0x4a4471);
                    continue;
                case '1':
                    _0x1f1b08 = _0x53821e(_0x1f1b08, _0x25080d);
                    continue;
                case '2':
                    var _0x1b4d9a = _0x1eb8bc;
                    continue;
                case '3':
                    var _0x25080d = _0x1f1b08;
                    continue;
                case '4':
                    var _0x4a4471 = _0x43e6ce;
                    continue;
                case '5':
                    _0x5114f4 = _0x53821e(_0x5114f4, _0x1671e7);
                    continue;
                case '6':
                    var _0x4c0b45 = _0x3b0b87;
                    continue;
                case '7':
                    _0x1eb8bc = _0x53821e(_0x1eb8bc, _0x1b4d9a);
                    continue;
                case '8':
                    _0x3b0b87 = _0x425f92[_0x39cb('0x52', 'r![p') + 'O'](_0x53821e, _0x3b0b87, _0x4c0b45);
                    continue;
                case '9':
                    for (var _0x124a73 = 0x0; _0x425f92[_0x39cb('0xc3', '3cp7') + 'E'](_0x124a73, 0x50); _0x124a73++) {
                        if (_0x124a73 < 0x10) {
                            _0x584e5d[_0x124a73] = _0x29e735[_0x27b1ea + _0x124a73];
                        } else {
                            _0x584e5d[_0x124a73] = _0x4327a5(_0x425f92[_0x39cb('0xc1', '3cp7') + 'u'](_0x425f92[_0x39cb('0x26', 'wrj@') + 'u'](_0x425f92[_0x39cb('0x4', 'mgb(') + 'V'](_0x584e5d[_0x124a73 - 0x3], _0x584e5d[_0x124a73 - 0x8]), _0x584e5d[_0x425f92[_0x39cb('0x31', 'i@nW') + 'K'](_0x124a73, 0xe)]), _0x584e5d[_0x425f92[_0x39cb('0xa3', 'Yf27') + 'K'](_0x124a73, 0x10)]), 0x1);
                        }
                        t = _0x425f92[_0x39cb('0x29', '&20#') + 'R'](_0x53821e, _0x425f92[_0x39cb('0x9b', 'mgb(') + 'R'](_0x53821e, _0x425f92[_0x39cb('0xa5', 'RlBI') + 'l'](_0x4327a5, _0x1eb8bc, 0x5), _0x425f92[_0x39cb('0x6c', ']bRZ') + 'c'](_0x18a523, _0x124a73, _0x43e6ce, _0x3b0b87, _0x5114f4)), _0x425f92[_0x39cb('0x50', 'I^*m') + 'l'](_0x53821e, _0x53821e(_0x1f1b08, _0x584e5d[_0x124a73]), _0x425f92[_0x39cb('0xb3', '9WwT') + 'U'](_0x26fbbb, _0x124a73)));
                        _0x1f1b08 = _0x5114f4;
                        _0x5114f4 = _0x3b0b87;
                        _0x3b0b87 = _0x425f92[_0x39cb('0xcb', '#4Zw') + 'h'](_0x4327a5, _0x43e6ce, 0x1e);
                        _0x43e6ce = _0x1eb8bc;
                        _0x1eb8bc = t;
                    }
                    continue;
                case '10':
                    var _0x1671e7 = _0x5114f4;
                    continue;
                }
                break;
            }
        }
        return _0x425f92[_0x39cb('0xb2', '^9MV') + 'U'](_0x425f92[_0x39cb('0xab', 'NNZT') + 'U'](_0x425f92[_0x39cb('0x90', 'ghwH') + 'v'](_0x425f92[_0x39cb('0xc0', 'rU8M') + 'X'](_0x36716a, _0x1eb8bc) + _0x36716a(_0x43e6ce), _0x36716a(_0x3b0b87)), _0x36716a(_0x5114f4)), _0x36716a(_0x1f1b08));
    }

    cryptojs=require("crypto-js")
    hash1={
        'sha1':function (aa){
            return cryptojs.SHA1(aa).toString()
        },
        'sha256':function (aa){
            return cryptojs.SHA256(aa).toString()
        },
        'md5':function (aa){
            return cryptojs.MD5(aa).toString()
        }
    }
    function go(_0x32de33) {
        if (_0x32de33["ha"]==="sha1"){
             hash=hash1["sha1"]
        }
        if (_0x32de33["ha"]==="sha256"){
             hash=hash1["sha256"]
        }
        if (_0x32de33["ha"]==="md5"){
             hash=hash1["md5"]
        }

        var _0x45ddb2 = {};
        _0x45ddb2[_0x39cb('0x42', 'x1dm') + 'v'] = _0x39cb('0xce', 'ghwH') + _0x39cb('0xad', '870@');
        _0x45ddb2[_0x39cb('0x95', 'UO*t') + 'U'] = function(_0xfaabbe, _0x4c12a1) {
            return _0xfaabbe < _0x4c12a1;
        }
        ;
        _0x45ddb2[_0x39cb('0x7', 'r![p') + 'x'] = function(_0x4436ad, _0x31aabf) {
            return _0x4436ad < _0x31aabf;
        }
        ;
        _0x45ddb2[_0x39cb('0x27', 'wrj@') + 'g'] = function(_0x273fdd, _0x17972b) {
            return _0x273fdd + _0x17972b;
        }
        ;
        _0x45ddb2[_0x39cb('0x6f', '*XUD') + 'V'] = function(_0x50c2b0, _0x3fa3a9) {
            return _0x50c2b0 + _0x3fa3a9;
        }
        ;
        _0x45ddb2[_0x39cb('0x83', 'O^*8') + 'q'] = function(_0x4b54d1, _0x3499a8) {
            return _0x4b54d1 == _0x3499a8;
        }
        ;
        _0x45ddb2[_0x39cb('0x3f', 'MOR!') + 'j'] = function(_0x48af3c, _0x46c8f2) {
            return _0x48af3c(_0x46c8f2);
        }
        ;
        _0x45ddb2[_0x39cb('0x25', 'CiTv') + 'Q'] = function(_0x13dd85, _0x3083e) {
            return _0x13dd85 - _0x3083e;
        }
        ;
        _0x45ddb2[_0x39cb('0x43', 'q8jq') + 'D'] = _0x39cb('0xa0', 'I80D') + _0x39cb('0x8d', 'naLL') + _0x39cb('0x2d', '&20#') + _0x39cb('0xa', 'v#5&');
        _0x45ddb2[_0x39cb('0x97', 'eqcG') + 'F'] = function(_0x120329, _0x51a23b) {
            return _0x120329 >= _0x51a23b;
        }
        ;
        _0x45ddb2[_0x39cb('0x17', '*XUD') + 'j'] = function(_0x8fecc2, _0x39fcf2) {
            return _0x8fecc2 & _0x39fcf2;
        }
        ;
        _0x45ddb2[_0x39cb('0xaa', 'ep[J') + 'k'] = function(_0x21e33d, _0x5ea10b) {
            return _0x21e33d + _0x5ea10b;
        }
        ;
        _0x45ddb2[_0x39cb('0x6b', 'q8jq') + 'E'] = function(_0x3e5dc5, _0x2a2865) {
            return _0x3e5dc5 + _0x2a2865;
        }
        ;
        _0x45ddb2[_0x39cb('0x2e', '3cp7') + 't'] = _0x39cb('0x6e', 'ep[J') + _0x39cb('0x9a', '!F(m') + '\x20/';
        _0x45ddb2[_0x39cb('0x5a', 'Xnqx') + 'u'] = _0x39cb('0xc7', 'h#hd') + 'E';
        _0x45ddb2[_0x39cb('0x57', 'naLL') + 'C'] = _0x39cb('0x86', '^9MV') + 'j';
        _0x45ddb2[_0x39cb('0xb0', 'ep[J') + 'O'] = _0x39cb('0x79', '*XUD') + _0x39cb('0xcf', 'wrj@') + _0x39cb('0xc9', '9WwT') + _0x39cb('0x3c', 'i@nW') + _0x39cb('0x7c', 'naLL') + _0x39cb('0xe', 'q6^v');
        _0x45ddb2[_0x39cb('0x99', 'MCY@') + 'o'] = function(_0x35a44c) {
            return _0x35a44c();
        }
        ;
        _0x45ddb2[_0x39cb('0x30', 'X)t)') + 'W'] = function(_0x1779c6, _0x35f36d, _0xd4939e) {
            return _0x1779c6(_0x35f36d, _0xd4939e);
        }
        ;
        _0x45ddb2[_0x39cb('0x40', '&20#') + 'D'] = function(_0x3b7b98, _0x713a6b) {
            return _0x3b7b98 > _0x713a6b;
        }
        ;
        _0x45ddb2[_0x39cb('0xb6', 'ep[J') + 'S'] = function(_0x4e4e73, _0x3cbda2) {
            return _0x4e4e73(_0x3cbda2);
        }
        ;
        _0x45ddb2[_0x39cb('0x8', 'X)t)') + 'h'] = function(_0x51d701, _0x245eb1) {
            return _0x51d701 - _0x245eb1;
        }
        ;
        var _0x21098b = _0x45ddb2;
        function _0x75e9ef() {
            var _0x1cee05 = window[_0x39cb('0x45', ']bRZ') + _0x39cb('0xa6', 'mgb(') + 'r'][_0x39cb('0x22', 'rU8M') + _0x39cb('0xaf', 'i@nW') + 't']
              , _0x12e8d1 = [_0x21098b[_0x39cb('0x4c', 'r![p') + 'v']];
            for (var _0x5336ed = 0x0; _0x21098b[_0x39cb('0x39', 'm1O2') + 'U'](_0x5336ed, _0x12e8d1[_0x39cb('0x8a', 'ep[J') + 'th']); _0x5336ed++) {
                if (_0x1cee05[_0x39cb('0x1d', 'aDie') + _0x39cb('0xa9', 'x1dm')](_0x12e8d1[_0x5336ed]) != -0x1) {
                    return !![];
                }
            }
            if (window[_0x39cb('0x35', '&20#') + _0x39cb('0x41', 'NNZT') + _0x39cb('0x66', 'CiTv')] || window[_0x39cb('0x1b', 'q6^v') + _0x39cb('0x92', 'aDie')] || window[_0x39cb('0x91', 'MOR!') + _0x39cb('0x81', 'MOR!')] || window[_0x39cb('0xc', 'x1dm') + _0x39cb('0x19', 'H4@i') + 'r'][_0x39cb('0x54', '*XUD') + _0x39cb('0x1c', 'q8jq') + 'r'] || window[_0x39cb('0x15', '&@we') + _0x39cb('0x68', 'tu8V') + 'r'][_0x39cb('0xa1', '#4Zw') + _0x39cb('0x4b', '6i)$') + _0x39cb('0x46', 'h#hd') + _0x39cb('0x78', '6WMO') + 'e'] || window[_0x39cb('0x8e', '3cp7') + _0x39cb('0x49', 'wrj@') + 'r'][_0x39cb('0x36', 'H4@i') + _0x39cb('0x4d', '*XUD') + _0x39cb('0x23', 'wrj@') + _0x39cb('0xc8', '1@%v') + _0x39cb('0x7b', 'aDie')]) {
                return !![];
            }
        }
        ;if (_0x21098b[_0x39cb('0xb1', '&@we') + 'o'](_0x75e9ef)) {
            return;
        }
        var _0x4bfbcd = new Date();
        function _0x112895(_0x151c46, _0x434fbf) {
            var _0x229236 = _0x32de33[_0x39cb('0x8c', 'Yf27') + 's'][_0x39cb('0x82', '*XUD') + 'th'];
            for (var _0x3e0a4e = 0x0; _0x21098b[_0x39cb('0xbe', 'mgb(') + 'x'](_0x3e0a4e, _0x229236); _0x3e0a4e++) {
                for (var _0x144b28 = 0x0; _0x144b28 < _0x229236; _0x144b28++) {
                    var _0x4c9d99 = _0x21098b[_0x39cb('0x38', 'MOR!') + 'g'](_0x21098b[_0x39cb('0xb5', 'UO*t') + 'V'](_0x21098b[_0x39cb('0xb5', 'UO*t') + 'V'](_0x434fbf[0x0], _0x32de33[_0x39cb('0x1', 'CiTv') + 's'][_0x39cb('0x10', 'MCY@') + 'tr'](_0x3e0a4e, 0x1)), _0x32de33[_0x39cb('0x13', 'AN$h') + 's'][_0x39cb('0xbb', '870@') + 'tr'](_0x144b28, 0x1)), _0x434fbf[0x1]);
                    if (_0x21098b[_0x39cb('0x83', 'O^*8') + 'q'](_0x21098b[_0x39cb('0x3a', '870@') + 'j'](hash, _0x4c9d99), _0x151c46)) {
                        return [_0x4c9d99, _0x21098b[_0x39cb('0x69', '*XUD') + 'Q'](new Date(), _0x4bfbcd)];
                    }
                }
            }
        }
        ;var _0x1ff91d = _0x21098b[_0x39cb('0xa4', 'r![p') + 'W'](_0x112895, _0x32de33['ct'], _0x32de33[_0x39cb('0xd', 'aDie')]);
        if (_0x1ff91d) {
            var _0x73c9da;
            if (_0x32de33['wt']) {
                _0x73c9da = _0x21098b[_0x39cb('0xb7', 'UO*t') + 'D'](_0x21098b[_0x39cb('0x18', 'MCY@') + 'S'](parseInt, _0x32de33['wt']), _0x1ff91d[0x1]) ? _0x21098b[_0x39cb('0x71', 'tu8V') + 'h'](parseInt(_0x32de33['wt']), _0x1ff91d[0x1]) : 0x1f4;
            } else {
                _0x73c9da = 0x5dc;
            }
           !function() {
                var _0x364646 = _0x21098b[_0x39cb('0x84', 'q6^v') + 'k'](_0x21098b[_0x39cb('0x6', 'eqcG') + 'E'](_0x32de33['tn'] + '=', _0x1ff91d[0x0]), _0x39cb('0x72', 'ghwH') + _0x39cb('0x1e', 'CiTv') + '=') + _0x32de33['vt'] + _0x21098b[_0x39cb('0x48', '^9MV') + 't'];
                if (_0x32de33['is']) {
                    if (_0x21098b[_0x39cb('0xa2', 'r![p') + 'u'] !== _0x21098b[_0x39cb('0x57', 'naLL') + 'C']) {
                        _0x364646 = _0x364646 + _0x21098b[_0x39cb('0x5b', 'x1dm') + 'O'];
                    } else {
                        var _0x2847a8 = _0x21098b[_0x39cb('0xcc', '9Nn4') + 'D'];
                        var _0xa2dcc8 = '';
                        for (var _0x1fa3a7 = 0x7; _0x21098b[_0x39cb('0x47', 'UO*t') + 'F'](_0x1fa3a7, 0x0); _0x1fa3a7--) {
                            _0xa2dcc8 += _0x2847a8[_0x39cb('0xc6', '@iPt') + 'At'](_0x21098b[_0x39cb('0x56', 'MCY@') + 'j'](num >> _0x1fa3a7 * 0x4, 0xf));
                        }
                        return _0xa2dcc8;
                    }
                }
                document[_0x39cb('0xc5', 'aDie') + 'ie'] = _0x364646;
                location[_0x39cb('0x7f', 'MOR!')] = _0x21098b[_0x39cb('0x6d', 'wrj@') + 'E'](location[_0x39cb('0x87', 'AN$h') + _0x39cb('0x0', 'UO*t')], location[_0x39cb('0x63', '1@%v') + 'ch']);
            }()
        } else {
            alert(_0x39cb('0xc4', 'MCY@') + '失败');
        }
    }
    ;

    get_go=function (aa){
         go(aa)
        return document.cookie

}
console.log(get_go({
    "bts": ["1719636779.605|0|1r1", "bRSL6lbP6Qio7kPJ7vx2wI%3D"],
    "chars": "TsMaHCOXjzQuJtsOJjbuYh",
    "ct": "cd984727802e2bef12911b8b599be74325c5ccd6",
    "ha": "sha1",
    "is": true,
    "tn": "__jsl_clearance_s",
    "vt": "3600",
    "wt": "1500"
}));


