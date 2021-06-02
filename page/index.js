function getResponse() {
  let userText = $('#textInput').val();
  let userHtml = '<p class="userText"><span>' + userText + '</span></p>';

  $('#textInput').val('');
  $('#chatbox').append(userHtml);

  document.getElementById('userInput');

  $('#chatbox').animate(
    {
      scrollTop: 1000000,
    },
    500,
  );

  $.get('/get', { msg: userText }).done(function (dados) {
    var botHtml = '<p class="botText"><span>' + dados.resp + '</span></p>';
    $('#chatbox').append(botHtml);

    if (dados.extra) {
      var botHtml2 = '<p class="botText"><span>' + dados.extra + '</span></p>';
      $('#chatbox').append(botHtml2);
    }

    document.getElementById('userInput');
  });
}

// tratando botoes e teclas
$('#textInput').keypress(function (e) {
  if (e.which == 13) {
    getResponse();
  }
});

$('#buttonInput').click(function () {
  getResponse();
});
