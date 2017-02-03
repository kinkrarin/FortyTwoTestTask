var old_number = 0;
var large = "";
var new_number = 0;
var title = 0;

function get_requests(){
  $.ajax({
    type: "GET",
    url: "/request_list/",
    dataType: "json",
    success: function(data){

      $("#MyTable > tbody").html("");


      for (var i = 0; i < data.length; i++) {
          var data_rewrite = data[i].fields.req_time;
          data_rewrite = data_rewrite.slice(0,10) + ' ' +  data_rewrite.slice(11,19);
          large += '<tr><td>' + data[i].fields.path + '</td>' + '<td>' + data_rewrite + '</td>' +  '<td>' + data[i].fields.method + '</td>' + '<td>' + data[i].fields.status + '</td>' + '</tr>';
      }
      $('#MyBody').append(large);
      large = '';
    },
    error: function (data) {
      alert("fail");
    }
  });
}

setInterval(function get_numbers() {
    $.ajax({
            type: 'GET',
            url: '/request_list_ajax/',
            dataType: 'json',
            success: function(data) {

                new_number = data.records;
                if (new_number > old_number) {
                    title = new_number - old_number;
                    show_title(title);
                    old_number = new_number;
                    get_requests();
                } else {

                }
            }
          });}
        , 3000);


function show_title(title) {
  if (title == 1){
    document.title = title + ' new request';
  } else if (title > 1){
    document.title = title + 'new requests';
  } else {
    document.title = ' Requests';
  }
  setTimeout(function(){
    document.title = 'Requests';
  }, 6000);
}


$(document).ready(function(){
  get_requests();
  get_numbers();
});
