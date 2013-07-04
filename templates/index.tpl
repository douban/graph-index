%setdefault('matched_metrics', None)
%import config
<h1>Search</h1>
<form action = '' method = 'POST'>
    <input class = 'input-xlarge' type = 'text' name = 'search' placeholder = 'regular expression'></input>
</form>
% if matched_metrics:
% for m in matched_metrics:
<img class = 'graph' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&title=day - {{m}}' />
<img class = 'graph' src = '{{config.graphite_url}}/render/?width=600&height=400&target={{m}}&from=-7d&title=week - {{m}}' />
% end
% end
