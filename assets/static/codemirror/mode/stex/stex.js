'use strict';(function(g){"object"==typeof exports&&"object"==typeof module?g(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],g):g(CodeMirror)})(function(g){g.defineMode("stex",function(t,q){function r(a){a=a.cmdState;for(var b=a.length-1;0<=b;b--){var c=a[b];if("DEFAULT"!=c.name)return c}return{styleIdentifier:function(){return null}}}function e(a,b,c){return function(){this.name=a;this.bracketNo=0;this.style=b;this.styles=c;this.argument=null;
this.styleIdentifier=function(){return this.styles[this.bracketNo-1]||null};this.openBracket=function(){this.bracketNo++;return"bracket"};this.closeBracket=function(){}}}function n(a,b){a.f=b}function l(a,b){if(a.match(/^\\[a-zA-Z@]+/)){a=a.current().slice(1);var c=d.hasOwnProperty(a)?d[a]:d.DEFAULT;c=new c;b.cmdState.push(c);b.f=p;return c.style}if(a.match(/^\\[$&%#{}_]/)||a.match(/^\\[,;!\/\\]/))return"tag";if(a.match("\\["))return n(b,function(h,k){return m(h,k,"\\]")}),"keyword";if(a.match("\\("))return n(b,
function(h,k){return m(h,k,"\\)")}),"keyword";if(a.match("$$"))return n(b,function(h,k){return m(h,k,"$$")}),"keyword";if(a.match("$"))return n(b,function(h,k){return m(h,k,"$")}),"keyword";var f=a.next();if("%"==f)return a.skipToEnd(),"comment";if("}"==f||"]"==f){if(c=0<b.cmdState.length?b.cmdState[b.cmdState.length-1]:null)c.closeBracket(f),b.f=p;else return"error";return"bracket"}if("{"==f||"["==f)return c=d.DEFAULT,c=new c,b.cmdState.push(c),"bracket";if(/\d/.test(f))return a.eatWhile(/[\w.%]/),
"atom";a.eatWhile(/[\w\-_]/);c=r(b);"begin"==c.name&&(c.argument=a.current());return c.styleIdentifier()}function m(a,b,c){if(a.eatSpace())return null;if(c&&a.match(c))return b.f=l,"keyword";if(a.match(/^\\[a-zA-Z@]+/))return"tag";if(a.match(/^[a-zA-Z]+/))return"variable-2";if(a.match(/^\\[$&%#{}_]/)||a.match(/^\\[,;!\/]/)||a.match(/^[\^_&]/))return"tag";if(a.match(/^[+\-<>|=,\/@!*:;'"`~#?]/))return null;if(a.match(/^(\d+\.\d*|\d*\.\d+|\d+)/))return"number";b=a.next();return"{"==b||"}"==b||"["==b||
"]"==b||"("==b||")"==b?"bracket":"%"==b?(a.skipToEnd(),"comment"):"error"}function p(a,b){var c=a.peek();if("{"==c||"["==c){var f=0<b.cmdState.length?b.cmdState[b.cmdState.length-1]:null;f.openBracket(c);a.eat(c);b.f=l;return"bracket"}if(/[ \t\r]/.test(c))return a.eat(c),null;b.f=l;(c=b.cmdState.pop())&&c.closeBracket();return l(a,b)}var d={};d.importmodule=e("importmodule","tag",["string","builtin"]);d.documentclass=e("documentclass","tag",["","atom"]);d.usepackage=e("usepackage","tag",["atom"]);
d.begin=e("begin","tag",["atom"]);d.end=e("end","tag",["atom"]);d.label=e("label","tag",["atom"]);d.ref=e("ref","tag",["atom"]);d.eqref=e("eqref","tag",["atom"]);d.cite=e("cite","tag",["atom"]);d.bibitem=e("bibitem","tag",["atom"]);d.Bibitem=e("Bibitem","tag",["atom"]);d.RBibitem=e("RBibitem","tag",["atom"]);d.DEFAULT=function(){this.name="DEFAULT";this.style="tag";this.styleIdentifier=this.openBracket=this.closeBracket=function(){}};return{startState:function(){return{cmdState:[],f:q.inMathMode?
function(a,b){return m(a,b)}:l}},copyState:function(a){return{cmdState:a.cmdState.slice(),f:a.f}},token:function(a,b){return b.f(a,b)},blankLine:function(a){a.f=l;a.cmdState.length=0},lineComment:"%"}});g.defineMIME("text/x-stex","stex");g.defineMIME("text/x-latex","stex")});
