$(document).ready(function() {
  $("#welcome").click(function(e) {
    console.log("fading welcome picture");
    var time = 850;
    $("#welcome-picture").fadeToggle(time);

    e.preventDefault();

    setTimeout(function() {
      window.location.href = "home";
    }, time);
  });

  $('[data-toggle="tooltip"]').tooltip();
});
