$(document).ready(function() {
    console.log("hid");

    $.ajax({
        url:"http://127.0.0.1:5000/curse/api/v1.0/words/",
        type:"GET",
        cache: false,
        asynch:false,
        success: function(response){
            console.log(response);
        }

    });

    // var root = 'https://jsonplaceholder.typicode.com';

    // $.ajax({
    //   url: root + '/posts/1',
    //   method: 'GET'
    // }).then(function(data) {
    //   console.log(data);
    // });
})
