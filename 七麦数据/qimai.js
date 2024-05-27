window=global


 function v2(t) {
                t = window["encodeURIComponent"](t)["replace"](/%([0-9A-F]{2})/g, function(n, t) {
                    return o("0x" + t)
                });

                    return window["btoa"](t)

            }

function o(n) {
                t = "",
                [
    "66",
    "72",
    "6f",
    "6d",
    "43",
    "68",
    "61",
    "72",
    "43",
    "6f",
    "64",
    "65"]["forEach"](function(n) {
                    t += window["unescape"]("%u00" + n)
                });
                var t, e = t;
                return window["String"][e](n)
            }
            function h(n, t) {
                t = t ||"a12c0fa6ab9119bc90e4ac7700796a53";
                for (var e = (n = n["split"](""))["length"], r = t["length"], a = "charCodeAt", i = 0; i < e; i++)
                    n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
                return n["join"]("")
            }
 function y(n, t, e) {
                for (var r = void 0 === e ? 2166136261 : e, a = 0, i = n["length"]; a < i; a++)
                    r = (r ^= n["charCodeAt"](a)) + ((r << 1) + (r << 4) + (r << 7) + (r << 8) + (r << 24));
                return t ? ("xyz" + (r >>> 0)["toString"](16) + "efgh")["substr"](-16) : r >>> 0
            }

get_analysis = function (params) {
    r = +new Date() - (1640 || 0) - 1661224081041
    console.log(r)
    console.log(params)
    a = params
    a = a["sort"]()["join"]("")
    console.log(a)
    a = v2(a);
    v = "@#";
    a = (a += v + "/indexV2/getIndexRank") + (v + r) + (v + 3);
    console.log(a)
    d = y("qimai@2022&Technology", 1)
    console.log(d)
    // d = "xyz517cda96efgh"

    e = v2(h(a, d))
    console.log(e)
    return e
}

get_analysis([0,'5000'])