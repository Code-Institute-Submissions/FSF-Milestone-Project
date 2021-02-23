var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
var client_secret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

//style var goes here

var card = elements.create('card');
card.mount('#card-element');


card.addEventListener('change', function(event){
    if (event.error){
            $('#card-errors').html(`
                <span class="icon" role="alert">
                    <i class="fas fas-times"></i>
                </span>
                <span>${event.error.message}</span>`)}
    else{
        $('#card-errors').html('');
    }
});

var form = document.getElementById('payment-form')

form.addEventListener('submit', function(ev){
    ev.preventDefault(); //stops default action, so script can do it's thing.
    card.update({ 'disabled': true}); // disables card and submit button when clicked, to prevent multiple submissions.
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#checkout-items').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(client_secret,{
        payment_method:{
            card: card,
        }
    }).then(function(result){
        if(result.error){
            $('#card-errors').html(`
                <span class="icon" role="alert">
                    <i class="fas fas-times"></i>
                </span>
                <span>${result.error.message}</span>`)
            $('#payment-form').fadeToggle(100);
            $('#checkout-items').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({'disabled':false});
            $('#submit-button').attr('disabled', false);
        }
        else{
            if (result.paymentIntent.status === 'succeeded'){
                form.submit();
            }
        };
    })
})