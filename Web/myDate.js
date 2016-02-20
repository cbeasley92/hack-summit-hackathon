  console.log("hello");
$.getJSON( "test.js", function( json ) {
  var a = JSON.parse(json);
  console.log(json);
  console.log("hello");
 });