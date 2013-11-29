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
    var order_by_name = $('#order-by-name');
    var order_by_user_rating = $('#order-by-user-rating');
    var series_search_form = $('#series-search-form');

    var form_sort_hidden = $('#form-sort-hidden');

    var check_all_exist_series = order_by_name.length>0 && order_by_user_rating.length>0;
    check_all_exist_series = check_all_exist_series && form_sort_hidden.length>0;
    check_all_exist_series = check_all_exist_series && series_search_form.length>0;

    var search_query = QueryString["search_query"];

    if(check_all_exist_series) {
        series_search_form.submit(function() {
            var sort_param = (QueryString["sort"] == undefined) ? 'name' : QueryString["sort"];
            form_sort_hidden[0].value = sort_param;
            return true;
        });

        if(search_query != undefined) {
            order_by_name[0].href += "&search_query="+search_query;
            order_by_user_rating[0].href += "&search_query="+search_query;

            var series_search_input = $('#series_search_input');
            if(series_search_input.length>0){
                series_search_input[0].value = search_query.split('+').join(' ');
            }
        }
    }

    var actor_search_form = $('#actor-search-form');

    var check_all_exist_actor = form_sort_hidden.length>0;
    check_all_exist_actor = check_all_exist_actor && actor_search_form.length>0;

    if(check_all_exist_actor){
        actor_search_form.submit(function() {
            var sort_param = (QueryString["sort"] == undefined) ? 'name' : QueryString["sort"];
            form_sort_hidden[0].value = sort_param;
            return true;
        });

        if(search_query != undefined) {
            var actor_search_input = $('#actor_search_input');
            if(actor_search_input.length>0){
                actor_search_input[0].value = search_query.split('+').join(' ');
            }
        }
    }
});