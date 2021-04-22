// try {
// document.domain = "dash.climateireland.ie";
// console.log('set domain');
// console.log(document.domain);
// }
// catch(err) {
// console.log("Tried to set domain name");
// console.log(err.message);
// }
var iframe = document.getElementById('dashIFrame');
var doc = (iframe.contentDocument)? iframe.contentDocument: iframe.contentWindow.document;

var anchors = doc.getElementsByTagName('a');
for (var i = 0; i < anchors.length; i++)
    anchors[i].target = '_parent';
