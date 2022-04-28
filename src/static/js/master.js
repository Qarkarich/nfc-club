$(".card").click(function(event) {
    var elem = event.currentTarget;
    var card_id = elem.getAttribute("data-card");
    xhr = $.ajax(
        '/card/' + card_id.trim()).done(
        function(data) {
            xhr = null
            $(".main-layout").append(data);
            $("#fadeout").show(200);
            $("#card-popup").fadeTo(200, 1);

            $(".edit-card").click(function(event) {
                xhr = $.ajax(
                    '/card/' + card_id.trim() + '/view').done(function(data) {
                        $("#card-popup").html(data);
                    });
            });
        });
});
    


$("#fadeout").click(function() {
    $("#fadeout").hide(200);
    $("#card-popup").remove();
});
