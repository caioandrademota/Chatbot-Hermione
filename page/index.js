function getResponse() {
  let userText = $("#textInput").val();
  let userHtml = '<p class="userText"><span>' + userText + "</span></p>";

  $("#textInput").val("");
  $("#chatbox").append(userHtml);

  document
    .getElementById("userInput")
    // .scrollIntoView({ block: "start", behavior: "smooth" });

  $("#chatbox").animate(
    {
      scrollTop: 1000000
    },
    500
  );

  $.get("/get", { msg: userText }).done(function (data) {
    var botHtml = '<p class="botText"><span>' + data + "</span></p>";

    $("#chatbox").append(botHtml);

    document
      .getElementById("userInput")
      // .scrollIntoView({ block: "start", behavior: "smooth" });
  });
}

// tratando botoes e teclas
$("#textInput").keypress(function (e) {
  if (e.which == 13) {
    getResponse();
  }
});

$("#buttonInput").click(function () {
  getResponse();
});
