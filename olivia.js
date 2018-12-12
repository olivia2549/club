function secret() {
  alert("the code is: 123456!")
}

function myFunction() {
  var x = document.getElementById("myQuotes");
  if (x.innerHTML == "'If your ship doesn't come in, swim out to meet it'") {
    x.innerHTML = "'Another cool quote!'";
  } else {
    x.innerHTML = "'If your ship doesn't come in, swim out to meet it'";
  }
}
