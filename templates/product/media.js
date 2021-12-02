function update_cart(product_id, quantity, sendButton, failcallback = null) {
    return $.ajax({
        url: "{{ url('cart_update') }}",
        type: 'post',
        data: {
            id: product_id,
            csrfmiddlewaretoken: '{{ csrf_token }}',
            quantity: quantity,
        },
        beforeSend: function() {
            sendButton.button('loading');
        },
        complete: function() {
            sendButton.button('reset');
        },
        error: failcallback,
    });
};