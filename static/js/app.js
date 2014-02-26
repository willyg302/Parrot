$('#omnibar').submit(function(event) {
	event.preventDefault();
	var url = $(this).attr('action');
	var post = $.post(url, {
		data: $('#search').val()
	});
	post.done(function(data) {
		$('#prompt').text(data);
		$('#search').val('');
	});
});