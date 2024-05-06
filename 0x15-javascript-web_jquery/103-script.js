$(() => {
  const fetchTranslation = () => {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, (data) => {
      $('#hello').text(data.hello);
    });
  };

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress((event) => {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});

