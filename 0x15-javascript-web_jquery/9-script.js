// should fetch api and return list
const $ = window.$;
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
  console.log(data.hello);
  $('#hello').html(data.hello);
});
