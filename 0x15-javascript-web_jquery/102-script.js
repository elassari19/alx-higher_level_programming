// should run when the document ready
$('document').ready(function () {
  // api data
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  // should set translate value
  $('INPUT#btn_translate').click(function () {
    // should return lang based on params
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      // should set value lang to html
      $('DIV#hello').html(data.hello);
    });
  });
});
