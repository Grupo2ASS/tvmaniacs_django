var QueryString = function () {
  var query_string = {};
  var query = window.location.search.substring(1);
  var vars = query.split("&");
  for (var i=0;i<vars.length;i++) {
    var pair = vars[i].split("=");
    	// If first entry with this name
    if (typeof query_string[pair[0]] === "undefined") {
      query_string[pair[0]] = pair[1];
    	// If second entry with this name
    } else if (typeof query_string[pair[0]] === "string") {
      var arr = [ query_string[pair[0]], pair[1] ];
      query_string[pair[0]] = arr;
    	// If third or later entry with this name
    } else {
      query_string[pair[0]].push(pair[1]);
    }
  }
    return query_string;
} ();

$(function() {
    var check_all_exist = $('#order-by-name').length>0 && $('#order-by-user-rating').length>0;
    check_all_exist = check_all_exist && $('#form-sort-hidden').length>0;
    check_all_exist = check_all_exist && $('#series-search-form').length>0;

    if(check_all_exist) {
        $('#series-search-form').submit(function() {
            var sort = (QueryString["sort"] == undefined) ? 'name' : QueryString["sort"];
            $('#form-sort-hidden')[0].value = sort;
            return true;
        });

        var query = QueryString["search_query"];
        if(query != undefined) {
            $('#order-by-name')[0].href += "&search_query="+query;
            $('#order-by-user-rating')[0].href += "&search_query="+query;
            $('#series_search_input')[0].value = query.split('+').join(' ');
        }
    }
});