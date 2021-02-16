// This code taken from Django tutorials
$('.update-link').click(function(e){
    var form = $(this).prev('.update-form');
    form.submit();
})

$('.remove-item').click(function(e){
    var csrfToken = "{{ csrf_token }}"; //is this going to work as an imported script?
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/bag/remove/${itemId}`;
    var data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url,data)
    .done(function(){
        location.reload();
    })
})