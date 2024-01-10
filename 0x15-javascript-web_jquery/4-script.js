// should toggle class on header
const $ = window.$;
$('#toggle_header').bind('click', function () {
  $('header').toggleClass('green red');
});
