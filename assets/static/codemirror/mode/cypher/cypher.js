'use strict';(function(d){"object"==typeof exports&&"object"==typeof module?d(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],d):d(CodeMirror)})(function(d){var k=function(c){return new RegExp("^(?:"+c.join("|")+")$","i")};d.defineMode("cypher",function(c){var f=function(a){var b=a.next();if('"'===b)return a.match(/.*?"/),"string";if("'"===b)return a.match(/.*?'/),"string";if(/[{}\(\),\.;\[\]]/.test(b))return e=b,"node";if("/"===b&&a.eat("/"))return a.skipToEnd(),
"comment";if(m.test(b))return a.eatWhile(m),null;a.eatWhile(/[_\w\d]/);if(a.eat(":"))return a.eatWhile(/[\w\d_\-]/),"atom";a=a.current();return n.test(a)?"builtin":p.test(a)?"def":q.test(a)||r.test(a)?"keyword":"variable"},g=function(a,b,h){return a.context={prev:a.context,indent:a.indent,col:h,type:b}},l=function(a){a.indent=a.context.indent;return a.context=a.context.prev},t=c.indentUnit,e,n=k("abs acos allShortestPaths asin atan atan2 avg ceil coalesce collect cos cot count degrees e endnode exp extract filter floor haversin head id keys labels last left length log log10 lower ltrim max min node nodes percentileCont percentileDisc pi radians rand range reduce rel relationship relationships replace reverse right round rtrim shortestPath sign sin size split sqrt startnode stdev stdevp str substring sum tail tan timestamp toFloat toInt toString trim type upper".split(" ")),
p=k("all and any contains exists has in none not or single xor".split(" ")),q=k("as asc ascending assert by case commit constraint create csv cypher delete desc descending detach distinct drop else end ends explain false fieldterminator foreach from headers in index is join limit load match merge null on optional order periodic profile remove return scan set skip start starts then true union unique unwind using when where with call yield".split(" ")),r=k("access active assign all alter as catalog change copy create constraint constraints current database databases dbms default deny drop element elements exists from grant graph graphs if index indexes label labels management match name names new node nodes not of on or password populated privileges property read relationship relationships remove replace required revoke role roles set show start status stop suspended to traverse type types user users with write".split(" ")),
m=/[*+\-<>=&|~%^]/;return{startState:function(){return{tokenize:f,context:null,indent:0,col:0}},token:function(a,b){a.sol()&&(b.context&&null==b.context.align&&(b.context.align=!1),b.indent=a.indentation());if(a.eatSpace())return null;var h=b.tokenize(a,b);"comment"!==h&&b.context&&null==b.context.align&&"pattern"!==b.context.type&&(b.context.align=!0);if("("===e)g(b,")",a.column());else if("["===e)g(b,"]",a.column());else if("{"===e)g(b,"}",a.column());else if(/[\]\}\)]/.test(e)){for(;b.context&&
"pattern"===b.context.type;)l(b);b.context&&e===b.context.type&&l(b)}else"."===e&&b.context&&"pattern"===b.context.type?l(b):/atom|string|variable/.test(h)&&b.context&&(/[\}\]]/.test(b.context.type)?g(b,"pattern",a.column()):"pattern"!==b.context.type||b.context.align||(b.context.align=!0,b.context.col=a.column()));return h},indent:function(a,b){b=b&&b.charAt(0);a=a.context;if(/[\]\}]/.test(b))for(;a&&"pattern"===a.type;)a=a.prev;b=a&&b===a.type;return a?"keywords"===a.type?d.commands.newlineAndIndent:
a.align?a.col+(b?0:1):a.indent+(b?0:t):0}}});d.modeExtensions.cypher={autoFormatLineBreaks:function(c){var f=c.split("\n");var g=/\s+\b(return|where|order by|match|with|skip|limit|create|delete|set)\b\s/g;for(c=0;c<f.length;c++)f[c]=f[c].replace(g," \n$1 ").trim();return f.join("\n")}};d.defineMIME("application/x-cypher-query","cypher")});
