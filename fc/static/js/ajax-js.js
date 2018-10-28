$(document).ready(function() {

    $('[data-role=review_container]').on('click', '[data-action=likes]', function(e){
        var $review_container = $(e.delegateTarget);
        var fcid = $review_container.data("fc_id")
        var $like_button = $(e.currentTarget);
        var $like_count = $review_container.find('[data-role=like_count]')
        var $dislike_count= $review_container.find('[data-role=dislike_count]')

        $.get('/likefact/', {fc_id: fcid}, function(data){

           data = JSON.parse(data);
           $like_count.html(data["likes"]); 
           $dislike_count.html(data["dislikes"]); 
         });
    });

    $('[data-role=review_container]').on('click', '[data-action=dislikes]', function(e){
        var $review_container = $(e.delegateTarget);
        var fcid = $review_container.data("fc_id")
        var $dislike_button = $(e.currentTarget);
        var $like_count = $review_container.find('[data-role=like_count]')
        var $dislike_count= $review_container.find('[data-role=dislike_count]')

        $.get('/dislikefact/', {fc_id: fcid}, function(data){

           data = JSON.parse(data);
           $like_count.html(data["likes"]); 
           $dislike_count.html(data["dislikes"]); 
         });
    });

    $('[data-role=creview_container]').on('click', '[data-action=trueComment]', function(e){
        var $creview_container = $(e.delegateTarget);
        var cid = $creview_container.data("c_id")
        var $true_button = $(e.currentTarget);
        var $true_count = $creview_container.find('[data-role=true_count]')
        var $sortof_count= $creview_container.find('[data-role=sortof_count]')
        var $false_count= $creview_container.find('[data-role=false_count]')

        $.get('/truecomment/', {c_id: cid}, function(data){

           data = JSON.parse(data);
           $true_count.html(data["trues"]); 
           $sortof_count.html(data["sortofs"]); 
           $false_count.html(data["falses"]); 
         });
    });

    $('[data-role=creview_container]').on('click', '[data-action=falseComment]', function(e){
        var $creview_container = $(e.delegateTarget);
        var cid = $creview_container.data("c_id")
        var $false_button = $(e.currentTarget);
        var $true_count = $creview_container.find('[data-role=true_count]')
        var $sortof_count= $creview_container.find('[data-role=sortof_count]')
        var $false_count= $creview_container.find('[data-role=false_count]')

        $.get('/falsecomment/', {c_id: cid}, function(data){

           data = JSON.parse(data);
           $true_count.html(data["trues"]); 
           $sortof_count.html(data["sortofs"]); 
           $false_count.html(data["falses"]); 
         });
    });

    $('[data-role=creview_container]').on('click', '[data-action=sortOfComment]', function(e){
        var $creview_container = $(e.delegateTarget);
        var cid = $creview_container.data("c_id")
        var $sortof_button = $(e.currentTarget);
        var $true_count = $creview_container.find('[data-role=true_count]')
        var $sortof_count= $creview_container.find('[data-role=sortof_count]')
        var $false_count= $creview_container.find('[data-role=false_count]')

        $.get('/sortofcomment/', {c_id: cid}, function(data){

           data = JSON.parse(data);
           $true_count.html(data["trues"]); 
           $sortof_count.html(data["sortofs"]); 
           $false_count.html(data["falses"]); 
         });
    });



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

    $('#trueComment').click(function(){
    console.log("called")
    var comment_id;
    comment_id = $(this).attr("data-cid");
    $.get('/truecomment/', {c_id: comment_id}, function(data){

        data = JSON.parse(data);
        $('#true_count').html(data["trues"]);
        $('#false_count').html(data["falses"]);
        $('#sortof_count').html(data["sortofs"]);
    });

    });


    $('#falseComment').click(function(){
    var comment_id;
    comment_id = $(this).attr("data-cid");
    $.get('/falsecomment/', {c_id: comment_id}, function(data){

        data = JSON.parse(data);
        $('#true_count').html(data["trues"]);
        $('#false_count').html(data["falses"]);
        $('#sortof_count').html(data["sortofs"]);
    });

    });

    $('#sortOfComment').click(function(){
    var comment_id;
    comment_id = $(this).attr("data-cid");
    $.get('/sortofcomment/', {c_id: comment_id}, function(data){

        data = JSON.parse(data);
        $('#true_count').html(data["trues"]);
        $('#false_count').html(data["falses"]);
        $('#sortof_count').html(data["sortofs"]);
    });

    });

});