var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
var client_secret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#100e00',
        fontFamily: '"Montserrat", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
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

    var saveInfo = Boolean($('#save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData={
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': client_secret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';
    $.post(url, postData).done(function(){
        stripe.confirmCardPayment(client_secret,{
        payment_method:{
            card: card,
            billing_details:{
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone.value),
                email: $.trim(form.email.value),
                address:{
                    line1: $.trim(form.address_line1.value),
                    line2: $.trim(form.address_line2.value),
                    city: $.trim(form.city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            }
        },
        shipping:{
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone.value),
            address:{
                line1: $.trim(form.address_line1.value),
                line2: $.trim(form.address_line2.value),
                city: $.trim(form.city.value),
                country: $.trim(form.country.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
            }
        },
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
    });
    }).fail(function(){
        location.reload();
    })  
});