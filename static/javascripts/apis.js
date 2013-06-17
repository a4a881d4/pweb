function load_settings(my)
{
  var url = '/load_settings?my='+my;
  $.get(url,function(data) {
    $('#settings_menu').html(data);
  });
}

function load_mainframe(my)
{
  var url = '/load_mainframe?my='+my;
  $.get(url,function(data) {
    $('#mainbody').html(data);
  });
}

function plugin_turn(ID,name)
{
  var url = '/plugin_turn?my='+ID;
  $.get(url,function(data) {
  });
}

function load_html_byID(url,item) 
{
  $.get(url,function(data) {
    $(item).html(data);
  });
}

function show_float_box( title , url )
{
	$('#float_box').off('show');
	$('#float_box').on('show', function () 
	{
  		$('#float_box_title').text(title);
  		$('#float_box .modal-body').load(url);
	})

	$('#float_box .modal-body').html('<div class="muted"><center>Loading</center>');
	$('#float_box').modal({ 'show':true });

}

