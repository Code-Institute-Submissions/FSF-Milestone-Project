// This code taken from Django tutorials
$('.update-link').click(function(e){
    var form = $(this).prev('.update-form');
    form.submit();
})

$('.remove-item').click(function(e){
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/cart/remove/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrftoken}; //changed this, django provides a csrftoken variable to js.

    $.post(url,data)
    .done(function(){
        location.reload();
    })
})