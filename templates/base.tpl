% setdefault('page', 'index')
% setdefault('search', '')
% setdefault('errors', [])
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Graph Index</title>
    <link href="/static/css/bootstrap.css" rel="stylesheet">
    <link href="/static/css/style.css" rel="stylesheet">
    <script src="/static/js/jquery.min.js"></script>
    <script src="/static/js/graph-index.js"></script>
  </head>

  <body>
    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container-fluid">
          <a class="brand" href="/">Graph Index</a>
          <div class="nav-collapse">
            <ul class="nav">
	% for (key, title) in [('index', 'Home'), ('dashboard', 'Dashboard'), ('debug', 'Debug'), ('docs', 'Docs'), ]:
		% if page == key:
              <li class="active"><a href="/{{key}}">{{title}}</a></li>
		% else:
              <li><a href="/{{key}}">{{title}}</a></li>
		% end
	% end
            </ul>
            <form class = 'navbar-search pull-right' action = '/regex/' method = 'POST'>
              <input id = 'search-box' type = 'text' class = 'search-query input-xlarge' name = 'search' placeholder = 'regular expression' value = "{{search}}"></input>
            </form>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
    <div id = 'container'>
    {{!body}}
    </div>
  </body>
</html>
