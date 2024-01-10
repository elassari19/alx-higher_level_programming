// should run when the document ready
$('document').ready(function () {
  // should add new li to ul list
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  // should remove li from ul list
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last').remove();
  });
  // should remove all li from ul list
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
