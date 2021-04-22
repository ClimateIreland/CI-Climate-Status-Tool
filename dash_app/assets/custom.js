// try {
// document.domain = "dash.climateireland.ie";
// console.log('set domain');
// console.log(document.domain);
// }
// catch(err) {
// console.log("Tried to set domain name");
// console.log(err.message);
// }
document.onload(function() {
    var iframe = document.getElementById('dashIFrame');
    var doc = (iframe.contentDocument)? iframe.contentDocument: iframe.contentWindow.document;

    var anchors = doc.getElementsByTagName('a');
    for (var i = 0; i < anchors.length; i++)
        anchors[i].target = '_parent';
    }
    )

// $(function() {
//     var iframeOffset = $("#dashIFrame", window.parent.document).offset();
//     $("a").each(function () {
//         var link = $(this);
//         var href = link.attr("href");
//         if (href && href[0] == "#") {
//             var name = href.substring(1);
//             $(this).click(function () {
//                 var nameElement = $("[name='" + name + "']");
//                 var idElement = $("#" + name);
//                 var element = null;
//                 if (nameElement.length > 0) {
//                     element = nameElement;
//                 } else if (idElement.length > 0) {
//                     element = idElement;
//                 }
  
//                 if (element) {
//                     var offset = element.offset();
//                     window.parent.scrollTo(offset.left, offset.top + iframeOffset.top);
//                 }
  
//                 return false;
//             });
//         }
//     });
//   });
