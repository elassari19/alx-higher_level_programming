// should fetch data and add it to character
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('#character').append(data.name);
});
