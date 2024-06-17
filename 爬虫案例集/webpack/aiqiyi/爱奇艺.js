passwd="zac123456"
  var ye, xe, be, _e = {}, ke = {}, we = 16, Ce = 65536, Se = 65535, Pe = function(e) {
            this.digits = "boolean" === typeof e && !0 === e ? null : ye.slice(0),
            this.isNeg = !1
        };
        function Ie(e) {
            var t = ke
              , n = t.biDivideByRadixPower(e, this.k - 1)
              , i = t.biMultiply(n, this.mu)
              , o = t.biDivideByRadixPower(i, this.k + 1)
              , r = t.biModuloByRadixPower(e, this.k + 1)
              , a = t.biMultiply(o, this.modulus)
              , s = t.biModuloByRadixPower(a, this.k + 1)
              , l = t.biSubtract(r, s);
            l.isNeg && (l = t.biAdd(l, this.bkplus1));
            for (var c = t.biCompare(l, this.modulus) >= 0; c; )
                l = t.biSubtract(l, this.modulus),
                c = t.biCompare(l, this.modulus) >= 0;
            return l
        }
        function Ae(e, t) {
            var n = ke.biMultiply(e, t);
            return this.modulo(n)
        }
        function Te(e, t) {
            var n = new Pe;
            n.digits[0] = 1;
            for (var i = e, o = t; 0 != (1 & o.digits[0]) && (n = this.multiplyMod(n, i)),
            0 != (o = ke.biShiftRight(o, 1)).digits[0] || 0 != ke.biHighIndex(o); )
                i = this.multiplyMod(i, i);
            return n
        }
        _e.BarrettMu = function(e) {
            this.modulus = ke.biCopy(e),
            this.k = ke.biHighIndex(this.modulus) + 1;
            var t = new Pe;
            t.digits[2 * this.k] = 1,
            this.mu = ke.biDivide(t, this.modulus),
            this.bkplus1 = new Pe,
            this.bkplus1.digits[this.k + 1] = 1,
            this.modulo = Ie,
            this.multiplyMod = Ae,
            this.powMod = Te
        }
        ,
        ke.biModuloByRadixPower = function(e, t) {
            var n = new Pe;
            return ke.arrayCopy(e.digits, 0, n.digits, 0, t),
            n
        }
        ,
        ke.biMultiply = function(e, t) {
            for (var n, i, o, r = new Pe, a = ke.biHighIndex(e), s = ke.biHighIndex(t), l = 0; l <= s; ++l) {
                n = 0,
                o = l;
                for (var c = 0; c <= a; ++c,
                ++o)
                    i = r.digits[o] + e.digits[c] * t.digits[l] + n,
                    r.digits[o] = i & Se,
                    n = i >>> 16;
                r.digits[l + a + 1] = n
            }
            return r.isNeg = e.isNeg != t.isNeg,
            r
        }
        ,
        ke.biDivideByRadixPower = function(e, t) {
            var n = new Pe;
            return ke.arrayCopy(e.digits, t, n.digits, 0, n.digits.length - t),
            n
        }
        ,
        ke.biDivide = function(e, t) {
            return ke.biDivideModulo(e, t)[0]
        }
        ,
        ke.setMaxDigits = function(e) {
            ye = new Array(e);
            for (var t = 0; t < ye.length; t++)
                ye[t] = 0;
            xe = new Pe,
            (be = new Pe).digits[0] = 1
        }
        ,
        ke.setMaxDigits(20),
        ke.biCopy = function(e) {
            var t = new Pe(!0);
            return t.digits = e.digits.slice(0),
            t.isNeg = e.isNeg,
            t
        }
        ,
        ke.reverseStr = function(e) {
            for (var t = "", n = e.length - 1; n > -1; --n)
                t += e.charAt(n);
            return t
        }
        ;
        var De = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
        ke.biToString = function(e, t) {
            var n = new Pe;
            n.digits[0] = t;
            for (var i = ke.biDivideModulo(e, n), o = De[i[1].digits[0]]; 1 == ke.biCompare(i[0], xe); )
                i = ke.biDivideModulo(i[0], n),
                o += De[i[1].digits[0]];
            return (e.isNeg ? "-" : "") + ke.reverseStr(o)
        }
        ;
        var Ee = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];
        ke.digitToHex = function(e) {
            for (var t = "", n = 0; n < 4; ++n)
                t += Ee[15 & e],
                e >>>= 4;
            return ke.reverseStr(t)
        }
        ,
        ke.biToHex = function(e) {
            for (var t = "", n = (ke.biHighIndex(e),
            ke.biHighIndex(e)); n > -1; --n)
                t += ke.digitToHex(e.digits[n]);
            return t
        }
        ,
        ke.charToHex = function(e) {
            return e >= 48 && e <= 57 ? e - 48 : e >= 65 && e <= 90 ? 10 + e - 65 : e >= 97 && e <= 122 ? 10 + e - 97 : 0
        }
        ,
        ke.hexToDigit = function(e) {
            for (var t = 0, n = Math.min(e.length, 4), i = 0; i < n; ++i)
                t <<= 4,
                t |= ke.charToHex(e.charCodeAt(i));
            return t
        }
        ,
        ke.biFromHex = function(e) {
            for (var t = new Pe, n = e.length, i = 0; n > 0; n -= 4,
            ++i)
                t.digits[i] = ke.hexToDigit(e.substr(Math.max(n - 4, 0), Math.min(n, 4)));
            return t
        }
        ,
        ke.biAdd = function(e, t) {
            var n;
            if (e.isNeg != t.isNeg)
                t.isNeg = !t.isNeg,
                n = ke.biSubtract(e, t),
                t.isNeg = !t.isNeg;
            else {
                n = new Pe;
                for (var i, o = 0, r = 0; r < e.digits.length; ++r)
                    i = e.digits[r] + t.digits[r] + o,
                    n.digits[r] = i % Ce,
                    o = Number(i >= Ce);
                n.isNeg = e.isNeg
            }
            return n
        }
        ,
        ke.biSubtract = function(e, t) {
            var n;
            if (e.isNeg != t.isNeg)
                t.isNeg = !t.isNeg,
                n = ke.biAdd(e, t),
                t.isNeg = !t.isNeg;
            else {
                var i, o;
                n = new Pe,
                o = 0;
                for (var r = 0; r < e.digits.length; ++r)
                    i = e.digits[r] - t.digits[r] + o,
                    n.digits[r] = i % Ce,
                    n.digits[r] < 0 && (n.digits[r] += Ce),
                    o = 0 - Number(i < 0);
                if (-1 == o) {
                    o = 0;
                    for (r = 0; r < e.digits.length; ++r)
                        i = 0 - n.digits[r] + o,
                        n.digits[r] = i % Ce,
                        n.digits[r] < 0 && (n.digits[r] += Ce),
                        o = 0 - Number(i < 0);
                    n.isNeg = !e.isNeg
                } else
                    n.isNeg = e.isNeg
            }
            return n
        }
        ,
        ke.biHighIndex = function(e) {
            for (var t = e.digits.length - 1; t > 0 && 0 == e.digits[t]; )
                --t;
            return t
        }
        ,
        ke.biNumBits = function(e) {
            var t, n = ke.biHighIndex(e), i = e.digits[n], o = (n + 1) * we;
            for (t = o; t > o - we && 0 == (32768 & i); --t)
                i <<= 1;
            return t
        }
        ,
        ke.biMultiplyDigit = function(e, t) {
            var n, i, o, r = new Pe;
            n = ke.biHighIndex(e),
            i = 0;
            for (var a = 0; a <= n; ++a)
                o = r.digits[a] + e.digits[a] * t + i,
                r.digits[a] = o & Se,
                i = o >>> 16;
            return r.digits[1 + n] = i,
            r
        }
        ,
        ke.arrayCopy = function(e, t, n, i, o) {
            for (var r = Math.min(t + o, e.length), a = t, s = i; a < r; ++a,
            ++s)
                n[s] = e[a]
        }
        ;
        var Me = [0, 32768, 49152, 57344, 61440, 63488, 64512, 65024, 65280, 65408, 65472, 65504, 65520, 65528, 65532, 65534, 65535];
        ke.biShiftLeft = function(e, t) {
            var n = Math.floor(t / we)
              , i = new Pe;
            ke.arrayCopy(e.digits, 0, i.digits, n, i.digits.length - n);
            for (var o = t % we, r = we - o, a = i.digits.length - 1, s = a - 1; a > 0; --a,
            --s)
                i.digits[a] = i.digits[a] << o & Se | (i.digits[s] & Me[o]) >>> r;
            return i.digits[0] = i.digits[a] << o & Se,
            i.isNeg = e.isNeg,
            i
        }
        ;
        var Ne = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535];
        ke.biShiftRight = function(e, t) {
            var n = Math.floor(t / we)
              , i = new Pe;
            ke.arrayCopy(e.digits, n, i.digits, 0, e.digits.length - n);
            for (var o = t % we, r = we - o, a = 0, s = a + 1; a < i.digits.length - 1; ++a,
            ++s)
                i.digits[a] = i.digits[a] >>> o | (i.digits[s] & Ne[o]) << r;
            return i.digits[i.digits.length - 1] >>>= o,
            i.isNeg = e.isNeg,
            i
        }
        ,
        ke.biMultiplyByRadixPower = function(e, t) {
            var n = new Pe;
            return ke.arrayCopy(e.digits, 0, n.digits, t, n.digits.length - t),
            n
        }
        ,
        ke.biCompare = function(e, t) {
            if (e.isNeg != t.isNeg)
                return 1 - 2 * Number(e.isNeg);
            for (var n = e.digits.length - 1; n >= 0; --n)
                if (e.digits[n] != t.digits[n])
                    return e.isNeg ? 1 - 2 * Number(e.digits[n] > t.digits[n]) : 1 - 2 * Number(e.digits[n] < t.digits[n]);
            return 0
        }
        ,
        ke.biDivideModulo = function(e, t) {
            var n, i, o = ke.biNumBits(e), r = ke.biNumBits(t), a = t.isNeg;
            if (o < r)
                return e.isNeg ? ((n = ke.biCopy(be)).isNeg = !t.isNeg,
                e.isNeg = !1,
                t.isNeg = !1,
                i = ke.biSubtract(t, e),
                e.isNeg = !0,
                t.isNeg = a) : (n = new Pe,
                i = ke.biCopy(e)),
                [n, i];
            n = new Pe,
            i = e;
            for (var s = Math.ceil(r / we) - 1, l = 0; t.digits[s] < 32768; )
                t = ke.biShiftLeft(t, 1),
                ++l,
                ++r,
                s = Math.ceil(r / we) - 1;
            i = ke.biShiftLeft(i, l),
            o += l;
            for (var c = Math.ceil(o / we) - 1, d = ke.biMultiplyByRadixPower(t, c - s); -1 != ke.biCompare(i, d); )
                ++n.digits[c - s],
                i = ke.biSubtract(i, d);
            for (var u = c; u > s; --u) {
                var p = u >= i.digits.length ? 0 : i.digits[u]
                  , h = u - 1 >= i.digits.length ? 0 : i.digits[u - 1]
                  , f = u - 2 >= i.digits.length ? 0 : i.digits[u - 2]
                  , v = s >= t.digits.length ? 0 : t.digits[s]
                  , g = s - 1 >= t.digits.length ? 0 : t.digits[s - 1];
                n.digits[u - s - 1] = p == v ? Se : Math.floor((p * Ce + h) / v);
                for (var m = n.digits[u - s - 1] * (v * Ce + g), y = 4294967296 * p + (h * Ce + f); m > y; )
                    --n.digits[u - s - 1],
                    m = n.digits[u - s - 1] * (v * Ce | g),
                    y = p * Ce * Ce + (h * Ce + f);
                d = ke.biMultiplyByRadixPower(t, u - s - 1),
                (i = ke.biSubtract(i, ke.biMultiplyDigit(d, n.digits[u - s - 1]))).isNeg && (i = ke.biAdd(i, d),
                --n.digits[u - s - 1])
            }
            return i = ke.biShiftRight(i, l),
            n.isNeg = e.isNeg != a,
            e.isNeg && (n = a ? ke.biAdd(n, be) : ke.biSubtract(n, be),
            t = ke.biShiftRight(t, l),
            i = ke.biSubtract(t, i)),
            0 == i.digits[0] && 0 == ke.biHighIndex(i) && (i.isNeg = !1),
            [n, i]
        }
        ;
        var Le = function(e, t, n) {
            var i = ke;
            this.e = i.biFromHex(e),
            this.d = i.biFromHex(t),
            this.m = i.biFromHex(n),
            this.chunkSize = 2 * i.biHighIndex(this.m),
            this.radix = 16,
            this.barrett = new _e.BarrettMu(this.m)
        };
        ke.getKeyPair = function(e, t, n) {
            return new Le(e,t,n)
        }
        ,
        ke.encryptedString = function(e, t) {
            for (var n = [], i = t.length, o = 0; o < i; )
                n[o] = t.charCodeAt(o),
                o++;
            for (; n.length % e.chunkSize != 0; )
                n[o++] = 0;
            var r, a, s, l = n.length, c = "";
            for (o = 0; o < l; o += e.chunkSize) {
                for (s = new Pe,
                r = 0,
                a = o; a < o + e.chunkSize; ++r)
                    s.digits[r] = n[a++],
                    s.digits[r] += n[a++] << 8;
                var d = e.barrett.powMod(s, e.e);
                c += (16 == e.radix ? ke.biToHex(d) : ke.biToString(d, e.radix)) + " "
            }
            return c.substring(0, c.length - 1)
        }
        ,
        ke.setMaxDigits(130);

        let je = {
            createSign(e, t, n, i) {
                let o = Object.keys(e).sort().map((t=>{
                    var n;
                    return "".concat(t, "=").concat(null !== (n = e[t]) && void 0 !== n ? n : "")
                }
                )).join("&");
                t = t || "key",
                n = n || "2cCq2fgeDNG-Eb8B%d]S.Ch<c]@uVN95",
                o = "".concat(o, "&").concat(t, "=").concat(n);
                let r = _()(o);
                return i ? r.toUpperCase() : r.toLowerCase()
            },
            createSignLike(e) {
                let t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "X2HZpj6R04Lz7srW"
                  , n = Object.keys(e).sort().map((t=>{
                    var n;
                    return "".concat(t, "=").concat(null !== (n = e[t]) && void 0 !== n ? n : "")
                }
                )).join("&");
                return n = "".concat(n).concat(t),
                console.log("createSignLike str:", n),
                je.getQdsf(n)
            },
            createSignPca: e=>je.createSign(e, "secret_key", "howcuteitis", !0),
            rsaEnc(e) {
                var t = ke.getKeyPair("10001", "", "ab86b6371b5318aaa1d3c9e612a9f1264f372323c8c0f19875b5fc3b3fd3afcc1e5bec527aa94bfa85bffc157e4245aebda05389a5357b75115ac94f074aefcd");
                return ke.encryptedString(t, encodeURIComponent(e)).replace(/\s/g, "-")
            },
            qdsfInfo(e) {
                let t = Z.httpParamsStr(e)
                  , n = "";
                try {
                    var i;
                    n = null === Re || void 0 === Re || null === (i = Re.qdsf) || void 0 === i ? void 0 : i.call(Re, 0, t, Math.floor(Date.now() / 1e3))
                } catch (o) {}
                return n ? {
                    "pass-sign": n
                } : {}
            },
            qdsfStr(e) {
                let t = "";
                try {
                    var n;
                    t = null === Re || void 0 === Re || null === (n = Re.qdsf) || void 0 === n ? void 0 : n.call(Re, 0, e, Math.floor(Date.now() / 1e3))
                } catch (i) {}
                return t ? "&qd_sf=".concat(t) : ""
            },
            getQdsf(e) {
                let t = "";
                try {
                    var n;
                    t = null === Re || void 0 === Re || null === (n = Re.qdsf) || void 0 === n ? void 0 : n.call(Re, 0, e, Math.floor(Date.now() / 1e3))
                } catch (i) {}
                return t
            }
        }
          , Be = "//mesh.if.iqiyi.com/"
          , Oe = {
            recommendAd: Be + "portal${platform}v5/channel/recoms",
            channelsData: Be + "portal${platform}v5/channel/navigateBar",
            channelPageV5: Be + "portal${platform}v5/channel/",
            channelPageV7: Be + "portal${platform}v7/channel/",
            shortVideoMenu: Be + "portal${platform}shortVideoChannel/tag?channelId=",
            shortVideoDatas: Be + "portal${platform}shortVideoChannel/entity?tagId=",
            shortVideoRecmdDatas: Be + "portal${platform}v2/short/video/data?tagId=",
            markImages: Be + "player{0}/video/mark_type/info",
            switchSettings: Be + "player{0}/setting/switches",
            activityApi: "//act.vip.iqiyi.com/interact/api/v2/show",
            interactApi: Be + "portal${platform}interact",
            activityApi_test: "http://act.vip.qiyi.domain/interact/api/v2/show",
            afterPay: Be + "tvg{0}/after_buy",
            discoverPage: Be + "tvg/find_page",
            addCollectUrl: Be + "tvg/my{0}/subscribe?",
            rmvCollectUrl: Be + "tvg/my{0}/unsubscribe?",
            isCollectUrl: Be + "tvg/my{0}/is_subscribed?",
            toFollow: Be + "tvg/my{0}/to_follow",
            cancelFollow: Be + "tvg/my{0}/cancel_follow",
            isFollow: Be + "tvg/my{0}/follow_status",
            appointVideo: "//subscription.iqiyi.com/services/subscribe/add.htm",
            cancelVideoAppointment: "//subscription.iqiyi.com/services/subscribe/cancel.htm",
            getVideoAppointState: "//subscription.iqiyi.com/services/subscribe/countAndState.htm",
            libTags: Be + "portal${platform}videolib/tag",
            libDatas: Be + "portal${platform}videolib/data",
            loginNote: Be + "tvg{0}/mixer_v2/login_note",
            preview: Be + "portal${platform}v5/channel/preview",
            getSimpleBaseinfo: Be + "tvg/v2{0}/base_info",
            baseVideoinfoV2: Be + "tvg/v2{0}/base_info",
            albumPosterBg: "https://pic7.iqiyipic.com/image/20221226/47/f4/pv_10008940535_em_601.jpg",
            popMarketing: Be + "tvg{0}/pop_marketing",
            vipActivity: Be + "player{0}/display/control/v2",
            qiquanInteract: Be + "interact",
            queryOrderStat: "https://i.vip.iqiyi.com/payresult/pc/queryOrderStat.action",
            newVideos: Be + "portal${platform}upcoming/movies",
            hangingOut: Be + "tvg/video_stream/hanging_out",
            like: "https://sns-like.iqiyi.com/gateway/v1/like",
            unlike: "https://sns-like.iqiyi.com/gateway/v1/dislike",
            removelikes: "https://sns-like.iqiyi.com/gateway/v1/record/removeLikes",
            adMix: "//mesh.if.iqiyi.com/portal{0}/ad/mixer",
            footerData: Be + "portal/lw/base/info/footer/resource"
        }
          , Fe = {
            clearSubscribe: Be + "tvg/my{0}/clear_subscribe",
            deleteHistory: Be + "tvg/my{0}/del_play_history",
            myHistory: Be + "tvg/my{0}/v2/play_history",
            mySubscribe: Be + "tvg/my{0}/my_subscribe",
            myLike: Be + "tvg/my{0}/liked_list",
            myReservation: Be + "tvg{0}/my_reservation",
            myFollow: Be + "tvg/my{0}/my_follow",
            myCourse: Be + "tv/purchased/list",
            vipInfoCover: "https://serv.vip.iqiyi.com/pay/result/multi-identity.action",
            vipRights: Be + "tvg${platform}v_user_rights",
            vipUserInfo: Be + "proxy{0}/userInfo",
            usercenterEntry: Be + "user{0}/userCenter",
            userLoginRewardView: Be + "user{0}/loginRewardView",
            userLoginReward: Be + "user{0}/loginReward",
            userVipReward: Be + "user{0}/vipReward",
            userBenifitReward: Be + "user{0}/benefitReward",
            usercenterEntry2: Be + "user{0}/userCenterLayer",
            batchAuth: "https://api.vip.iqiyi.com/services/batchAuth.action",
            downloadInfo: Be + "tvg{0}/mixer_v2/download_info",
            downloadInfoJson: Be + "tvg{0}/mixer/download_json",
            videoDash: "//cache.video.iqiyi.com/dash",
            playListDetail: Be + "tvg{0}/play_list_detail"
        }
          , Ve = "https://www.iqiyi.com/safety/findPassword.html?"
          , qe = "https://www.iqiyi.com/user/register/protocol.html"
          , He = "https://privacy.iqiyi.com/policies"
          , Ue = "https://www.iqiyi.com/weatherPCA?"
          , ze = {
            weatherInfo: Be + "portal/pcw/weather/data",
            gameInfo: Be + "tvg{0}/layer_game",
            gameCenterInfo: Be + "user{0}/infoCenter",
            playComplete: Be + "user{0}/game/playComplete",
            getGameVip: Be + "user{0}/game/getVip",
            getVipFloat: Be + "user{0}/activity/vipFloat",
            uploadRegister: "https://mp.iqiyi.com/wemedia/publish/video?refer=iqiyipcw_homepage_upload_register"
        }
          , We = "//passport.iqiyi.com/"
          , Ge = {
            logout: We + "apis/user/logout.action",
            login: We + "apis/reglogin/login.action",
            optLogin: We + "apis/sso/device_otp_login.action",
            delOptKey: We + "apis/user/del_device_otp.action",
            thirdLogin: "https://passport.iqiyi.com/apis/thirdparty/nlogin.action",
            ssoTokenIQIYI: We + "apis/user/sso/cd/token.action",
            ssoCookieIQIYI: We + "apis/user/sso/cd/cookie.action",
            delcookieIQIYI: We + "apis/user/delcookie.action",
            genLoginToken: We + "apis/qrcode/gen_login_token.action",
            isTokenLogin: We + "apis/qrcode/is_token_login.action",
            getAreacode: We + "apis/phone/get_support_areacode.action",
            getAuthCode: We + "apis/phone/secure_send_cellphone_authcode.action",
            authcodeLogin: We + "apis/reglogin/authcode_login.action",
            upBizInfo: We + "apis/phone/up_biz_info.action",
            upBizStatus: We + "apis/phone/up_biz_status.action",
            verifyAuthCode: We + "apis/phone/verify_cellphone_authcode.action",
            directBindPhone: We + "apis/phone/direct_bind_phone.action",
            verifyAccount: We + "apis/phone/verify_account.action",
            checkAccount: We + "apis/user/check_account.action",
            userRegConfirm: We + "apis/reglogin/user_reg_confirm.action",
            bindLogin: We + "apis/reglogin/bind_login.action",
            getUserStatus: We + "apis/phone/account_status.action",
            checkAuth: We + "apis/user/uid.action",
            renewAuthCookie: We + "apis/reglogin/renew_authcookie.action",
            userInfoDetail: "https://pcw-api.iqiyi.com/passport/user/userinfodetail"
        };
        const Ke = e=>{
            let t = decodeURIComponent(window.location.search || window.location.href);
            e && (t = decodeURIComponent(e));
            let n = {}
              , i = t.split("?");
            if (i.length <= 1)
                return n;
            i = i[1].split("&");
            for (let o = 0, r = i.length; o < r; o++) {
                let e = i[o].split("=");
                n[e[0]] = e[1]
            }
            return n
        }
          , Ye = (e,t,n)=>{
            let i = Object.keys(e);
            i.sort();
            let o = "";
            for (let r = 0; r < i.length; r++) {
                let t = i[r];
                o += (r > 0 ? "&" : "") + t + "=" + (n ? e[t] : encodeURIComponent(e[t]))
            }
            if (t)
                if ("string" === typeof t)
                    o += t;
                else {
                    o += "&";
                    for (let e of Object.keys(t))
                        o += "".concat(e, "=").concat(t[e])
                }
            return o
        }
        ;
        let Qe = {
            count: 0
        };

 var Le = function(e, t, n) {
            var i = ke;
            this.e = i.biFromHex(e),
            this.d = i.biFromHex(t),
            this.m = i.biFromHex(n),
            this.chunkSize = 2 * i.biHighIndex(this.m),
            this.radix = 16,
            this.barrett = new _e.BarrettMu(this.m)
        };
        ke.getKeyPair = function(e, t, n) {
            return new Le(e,t,n)
        }
        ,
        ke.encryptedString = function(e, t) {
            for (var n = [], i = t.length, o = 0; o < i; )
                n[o] = t.charCodeAt(o),
                o++;
            for (; n.length % e.chunkSize != 0; )
                n[o++] = 0;
            var r, a, s, l = n.length, c = "";
            for (o = 0; o < l; o += e.chunkSize) {
                for (s = new Pe,
                r = 0,
                a = o; a < o + e.chunkSize; ++r)
                    s.digits[r] = n[a++],
                    s.digits[r] += n[a++] << 8;
                var d = e.barrett.powMod(s, e.e);
                c += (16 == e.radix ? ke.biToHex(d) : ke.biToString(d, e.radix)) + " "
            }
            return c.substring(0, c.length - 1)
        }
 ke.biFromHex = function(e) {
            for (var t = new Pe, n = e.length, i = 0; n > 0; n -= 4,
            ++i)
                t.digits[i] = ke.hexToDigit(e.substr(Math.max(n - 4, 0), Math.min(n, 4)));
            return t
        }
rsaEnc=function (e) {
    var t = ke.getKeyPair("10001", "", "ab86b6371b5318aaa1d3c9e612a9f1264f372323c8c0f19875b5fc3b3fd3afcc1e5bec527aa94bfa85bffc157e4245aebda05389a5357b75115ac94f074aefcd");
    return ke.encryptedString(t, encodeURIComponent(e)).replace(/\s/g, "-")
}
passwd=rsaEnc(passwd)

console.log(passwd)