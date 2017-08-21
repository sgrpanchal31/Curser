$(document).ready(function() {
    console.log("hi");

    $.ajax({
        url:"http://localhost:5000/curse/api/v1.0/words/",
        type:"GET",
        // data:"actionfunction=showData",
        cache: false,

        asynch:false,
        contentType: "application/json; charset=utf-8",
        headers: { 'Access-Control-Allow-Origin': '*' },
        crossDomain: true,
        jsonpCallback: 'callback',
        dataType: 'JSONP',
        jsonp: 'callback',
        success: function(response){
            console.log(response.words);
        }

    });

})
