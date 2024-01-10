// should replace text of header
const $ = window.$;
$('#update_header').bind('click', function () {
  $('header').replaceWith('New Header!!!');
});
