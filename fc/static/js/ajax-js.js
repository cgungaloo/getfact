$(document).ready(function() {

    $('#likes').click(function(){
    var fcid;
    console.log("Like called")
    fcid = $(this).attr("data-fcid");
    $.get('/likefact/', {fc_id: fcid}, function(data){

    	data = JSON.parse(data);
    	$('#like_count').html(data["likes"]);
    	$('#dislike_count').html(data["dislikes"]);
    });
	});

	$('#dislikes').click(function(){
    var fcid;
    console.log("Dislike called")
    fcid = $(this).attr("data-fcid");
    $.get('/dislikefact/', {fc_id: fcid}, function(data){

    	data = JSON.parse(data);
    	$('#dislike_count').html(data["dislikes"]);
    	$('#like_count').html(data["likes"]);
    });

	});

});