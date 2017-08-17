$(document).ready(function() {
    console.log("hi");

    $.ajax({
        url:"http://localhost:5000/curse/api/v1.0/words/2",
        type:"GET",
        // data:"actionfunction=showData",
        cache: false,
        success: function(response){
            console.log(response);
        }

    });

})
