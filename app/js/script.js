$(document).ready(function() {
    console.log("hi");

    // $.ajax({
    //     // url:"http://localhost:5000/curse/api/v1.0/words/",
    //     url:"https://jsonplaceholder.typicode.com/posts/1",
    //     type:"GET",
    //     // dataType :"jsonp",
    //     // "Content-type": "application/json",
    //     cache: false,
    //     asynch:false,
    //     // jsonp: false,
    //     // jsonpCallback: "myJsonMethod",
    //     success: function(response){
    //         console.log(response);
    //     }

    // });
    var root = 'https://jsonplaceholder.typicode.com';

    $.ajax({
      url: root + '/posts/1',
      method: 'GET'
    }).then(function(data) {
      console.log(data);
    });
})
