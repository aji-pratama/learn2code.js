'use strict';var $jscomp=$jscomp||{};$jscomp.scope={};$jscomp.findInternal=function(a,c,d){a instanceof String&&(a=String(a));for(var f=a.length,e=0;e<f;e++){var m=a[e];if(c.call(d,m,e,a))return{i:e,v:m}}return{i:-1,v:void 0}};$jscomp.ASSUME_ES5=!1;$jscomp.ASSUME_NO_NATIVE_MAP=!1;$jscomp.ASSUME_NO_NATIVE_SET=!1;$jscomp.SIMPLE_FROUND_POLYFILL=!1;$jscomp.ISOLATE_POLYFILLS=!1;$jscomp.FORCE_POLYFILL_PROMISE=!1;$jscomp.ENABLE_UNHANDLED_REJECTION_POLYFILL=!0;
$jscomp.defineProperty=$jscomp.ASSUME_ES5||"function"==typeof Object.defineProperties?Object.defineProperty:function(a,c,d){if(a==Array.prototype||a==Object.prototype)return a;a[c]=d.value;return a};$jscomp.getGlobal=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var c=0;c<a.length;++c){var d=a[c];if(d&&d.Math==Math)return d}throw Error("Cannot find global object");};$jscomp.global=$jscomp.getGlobal(this);
$jscomp.IS_SYMBOL_NATIVE="function"===typeof Symbol&&"symbol"===typeof Symbol("x");$jscomp.TRUST_ES6_POLYFILLS=!$jscomp.ISOLATE_POLYFILLS||$jscomp.IS_SYMBOL_NATIVE;$jscomp.polyfills={};$jscomp.propertyToPolyfillSymbol={};$jscomp.POLYFILL_PREFIX="$jscp$";var $jscomp$lookupPolyfilledValue=function(a,c){var d=$jscomp.propertyToPolyfillSymbol[c];if(null==d)return a[c];d=a[d];return void 0!==d?d:a[c]};
$jscomp.polyfill=function(a,c,d,f){c&&($jscomp.ISOLATE_POLYFILLS?$jscomp.polyfillIsolated(a,c,d,f):$jscomp.polyfillUnisolated(a,c,d,f))};$jscomp.polyfillUnisolated=function(a,c,d,f){d=$jscomp.global;a=a.split(".");for(f=0;f<a.length-1;f++){var e=a[f];if(!(e in d))return;d=d[e]}a=a[a.length-1];f=d[a];c=c(f);c!=f&&null!=c&&$jscomp.defineProperty(d,a,{configurable:!0,writable:!0,value:c})};
$jscomp.polyfillIsolated=function(a,c,d,f){var e=a.split(".");a=1===e.length;f=e[0];f=!a&&f in $jscomp.polyfills?$jscomp.polyfills:$jscomp.global;for(var m=0;m<e.length-1;m++){var r=e[m];if(!(r in f))return;f=f[r]}e=e[e.length-1];d=$jscomp.IS_SYMBOL_NATIVE&&"es6"===d?f[e]:null;c=c(d);null!=c&&(a?$jscomp.defineProperty($jscomp.polyfills,e,{configurable:!0,writable:!0,value:c}):c!==d&&($jscomp.propertyToPolyfillSymbol[e]=$jscomp.IS_SYMBOL_NATIVE?$jscomp.global.Symbol(e):$jscomp.POLYFILL_PREFIX+e,e=
$jscomp.propertyToPolyfillSymbol[e],$jscomp.defineProperty(f,e,{configurable:!0,writable:!0,value:c})))};$jscomp.polyfill("Array.prototype.find",function(a){return a?a:function(c,d){return $jscomp.findInternal(this,c,d).v}},"es6","es3");
(function(a){"object"==typeof exports&&"object"==typeof module?a(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],a):a(CodeMirror)})(function(a){function c(b){b.state.markedSelection&&b.operation(function(){r(b)})}function d(b){b.state.markedSelection&&b.state.markedSelection.length&&b.operation(function(){e(b)})}function f(b,g,h,k){if(0!=p(g,h))for(var l=b.state.markedSelection,n=b.state.markedSelectionStyle,q=g.line;;){var t=q==g.line?g:v(q,
0);q+=u;var w=q>=h.line,x=w?h:v(q,0);t=b.markText(t,x,{className:n});null==k?l.push(t):l.splice(k++,0,t);if(w)break}}function e(b){b=b.state.markedSelection;for(var g=0;g<b.length;++g)b[g].clear();b.length=0}function m(b){e(b);for(var g=b.listSelections(),h=0;h<g.length;h++)f(b,g[h].from(),g[h].to())}function r(b){if(!b.somethingSelected())return e(b);if(1<b.listSelections().length)return m(b);var g=b.getCursor("start"),h=b.getCursor("end"),k=b.state.markedSelection;if(!k.length)return f(b,g,h);var l=
k[0].find(),n=k[k.length-1].find();if(!l||!n||h.line-g.line<=u||0<=p(g,n.to)||0>=p(h,l.from))return m(b);for(;0<p(g,l.from);)k.shift().clear(),l=k[0].find();0>p(g,l.from)&&(l.to.line-g.line<u?(k.shift().clear(),f(b,g,l.to,0)):f(b,g,l.from,0));for(;0>p(h,n.to);)k.pop().clear(),n=k[k.length-1].find();0<p(h,n.to)&&(h.line-n.from.line<u?(k.pop().clear(),f(b,n.from,h)):f(b,n.to,h))}a.defineOption("styleSelectedText",!1,function(b,g,h){h=h&&h!=a.Init;g&&!h?(b.state.markedSelection=[],b.state.markedSelectionStyle=
"string"==typeof g?g:"CodeMirror-selectedtext",m(b),b.on("cursorActivity",c),b.on("change",d)):!g&&h&&(b.off("cursorActivity",c),b.off("change",d),e(b),b.state.markedSelection=b.state.markedSelectionStyle=null)});var u=8,v=a.Pos,p=a.cmpPos});
