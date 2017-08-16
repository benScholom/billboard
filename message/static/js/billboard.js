$(document).ready(function() {
	//ensure placeholders are set in the add new post form
	$("#id_post_text").attr('placeholder', "Enter some text:");
	$("#id_post_title").attr('placeholder', "Title");
	$("#id_post_author").attr('placeholder', 'author');
	//remove bound submit event from x button and add return to homepage capbility
	//$(".close").unbind();
	//$(".close").on('click', function() {
		//window.location = "{% url '/'%}";
	//});
});

