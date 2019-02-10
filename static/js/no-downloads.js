$( document ).ready(function() {
    
    var firsth2 = $("h2").text();
    
    if (firsth2=="") {
        $("#download-message").text("You don't have any downloads yet.");
    }
    
});