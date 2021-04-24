
https://codemirror.net/doc/manual.html#addon_merge
https://github.com/codemirror/CodeMirror/blob/master/demo/merge.html
https://codemirror.net/demo/merge.html


var myCodeMirror = CodeMirror.fromTextArea(myTextArea);



  dv = CodeMirror.MergeView(target, {
    value: value,
    origLeft: panes == 3 ? orig1 : null,
    orig: orig2,
    lineNumbers: true,
    mode: "text/html",
    highlightDifferences: highlight,
    connect: connect,
    collapseIdentical: collapse
  });

