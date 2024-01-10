// should add class to header
const $ = window.$;
$('#red_header').bind('click', function () {
  $('header').addClass('red');
});
