'use strict';(function(g){"object"==typeof exports&&"object"==typeof module?g(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],g):g(CodeMirror)})(function(g){g.defineMode("tiddlywiki",function(){function f(a,c,d){c.tokenize=d;return d(a,c)}function e(a,c){var d=a.sol(),b=a.peek();c.block=!1;if(d&&/[<\/\*{}\-]/.test(b)){if(a.match(k))return c.block=!0,f(a,c,h);if(a.match(l))return"quote";if(a.match(m)||a.match(n)||a.match(p)||a.match(q)||a.match(r)||
a.match(t))return"comment";if(a.match(u))return"hr"}a.next();if(d&&/[\/\*!#;:>|]/.test(b)){if("!"==b)return a.skipToEnd(),"header";if("*"==b)return a.eatWhile("*"),"comment";if("#"==b)return a.eatWhile("#"),"comment";if(";"==b)return a.eatWhile(";"),"comment";if(":"==b)return a.eatWhile(":"),"comment";if(">"==b)return a.eatWhile(">"),"quote";if("|"==b)return"header"}if("{"==b&&a.match(/\{\{/))return f(a,c,h);if(/[hf]/i.test(b)&&/[ti]/i.test(a.peek())&&a.match(/\b(ttps?|tp|ile):\/\/[\-A-Z0-9+&@#\/%?=~_|$!:,.;]*[A-Z0-9+&@#\/%=~_|$]/i))return"link";
if('"'==b)return"string";if("~"==b||/[\[\]]/.test(b)&&a.match(b))return"brace";if("@"==b)return a.eatWhile(v),"link";if(/\d/.test(b))return a.eatWhile(/\d/),"number";if("/"==b){if(a.eat("%"))return f(a,c,w);if(a.eat("/"))return f(a,c,x)}if("_"==b&&a.eat("_"))return f(a,c,y);if("-"==b&&a.eat("-")){if(" "!=a.peek())return f(a,c,z);if(" "==a.peek())return"brace"}if("'"==b&&a.eat("'"))return f(a,c,A);if("<"==b&&a.eat("<"))return f(a,c,B);a.eatWhile(/[\w\$_]/);return C.propertyIsEnumerable(a.current())?
"keyword":null}function w(a,c){for(var d=!1,b;b=a.next();){if("/"==b&&d){c.tokenize=e;break}d="%"==b}return"comment"}function A(a,c){for(var d=!1,b;b=a.next();){if("'"==b&&d){c.tokenize=e;break}d="'"==b}return"strong"}function h(a,c){var d=c.block;if(d&&a.current())return"comment";if(!d&&a.match(D)||d&&a.sol()&&a.match(E))return c.tokenize=e,"comment";a.next();return"comment"}function x(a,c){for(var d=!1,b;b=a.next();){if("/"==b&&d){c.tokenize=e;break}d="/"==b}return"em"}function y(a,c){for(var d=
!1,b;b=a.next();){if("_"==b&&d){c.tokenize=e;break}d="_"==b}return"underlined"}function z(a,c){for(var d=!1,b;b=a.next();){if("-"==b&&d){c.tokenize=e;break}d="-"==b}return"strikethrough"}function B(a,c){if("<<"==a.current())return"macro";var d=a.next();if(!d)return c.tokenize=e,null;if(">"==d&&">"==a.peek())return a.next(),c.tokenize=e,"macro";a.eatWhile(/[\w\$_]/);return F.propertyIsEnumerable(a.current())?"keyword":null}var C={},F={allTags:!0,closeAll:!0,list:!0,newJournal:!0,newTiddler:!0,permaview:!0,
saveChanges:!0,search:!0,slider:!0,tabs:!0,tag:!0,tagging:!0,tags:!0,tiddler:!0,timeline:!0,today:!0,version:!0,option:!0,"with":!0,filter:!0},v=/[\w_\-]/i,u=/^\-\-\-\-+$/,m=/^\/\*\*\*$/,n=/^\*\*\*\/$/,l=/^<<<$/,p=/^\/\/\{\{\{$/,q=/^\/\/\}\}\}$/,r=/^\x3c!--\{\{\{--\x3e$/,t=/^\x3c!--\}\}\}--\x3e$/,k=/^\{\{\{$/,E=/^\}\}\}$/,D=/.*?\}\}\}/;return{startState:function(){return{tokenize:e}},token:function(a,c){return a.eatSpace()?null:c.tokenize(a,c)}}});g.defineMIME("text/x-tiddlywiki","tiddlywiki")});