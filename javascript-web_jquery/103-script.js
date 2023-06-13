$(document).ready(function() {
  function fetchTranslation() {
    var languageCode = $('#language_code').val();

    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      data: { lang: languageCode },
      success: function(response) {
        $('#hello').text(response.hello);
      },
      error: function() {
        $('#hello').text('Error occurred while fetching translation.');
      }
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function(e) {
    if (e.which === 13) {
      fetchTranslation();
    }
  });
});

