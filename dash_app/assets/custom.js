try {
document.domain = "dash.climateireland.ie";
console.log('set domain');
console.log(document.domain);
}
catch(err) {
console.log("Tried to set domain name");
console.log(err.message);
}
