$(".card").click(function(event) {
    var elem = event.currentTarget;
    var card_id = elem.getAttribute("data-card");
    xhr = $.ajax(
        '/card/' + card_id.trim() + '/view').done(
        function(data) {
            xhr = null
            $("#card-popup").html(data);
        });
});
