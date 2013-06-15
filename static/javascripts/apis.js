function load_settings(my)
{
  var url = '/load_settings?my='+my;
  $.get(url,function(data) {
    $('#settings_menu').html(data);
  })
}

function load_mainframe(my)
{
  var url = '/load_mainframe?my='+my;
  $.get(url,function(data) {
    $('#mainbody').html(data);
  })
}
