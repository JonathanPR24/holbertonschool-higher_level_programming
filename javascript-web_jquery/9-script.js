$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (fetch) {
  $('#hello').text(fetch.hello);
});
