'use strict';(function(){CodeMirror.defineMode("markdown_with_stex",function(){var a=CodeMirror.getMode({},"stex"),b=CodeMirror.getMode({},"markdown");return CodeMirror.multiplexingMode(b,{open:"$",close:"$",mode:a,delimStyle:"delim",innerStyle:"inner"})});var c=CodeMirror.getMode({},"markdown_with_stex");(function(a){test.mode(a,c,Array.prototype.slice.call(arguments,1),"multiplexing")})("stexInsideMarkdown","[strong **Equation:**] [delim&delim-open $][inner&tag \\pi][delim&delim-close $]")})();