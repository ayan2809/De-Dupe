// Parallax Code
var scene = document.getElementById('scene');
var parallax = new Parallax(scene);

var $loader = $(".text");
var $btnDare = $loader.find(".dare");

$(document).ready(function () {
    $btnDare.click(function () {
      window.location = '/';
      // $('.success').fadeOut(500);
    });
  });