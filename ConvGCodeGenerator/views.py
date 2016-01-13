from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    title = "CG2 - Conversational G-Code Generator"
    link_list = ['Machines', 
                 'Operations', 
                 'Post Processors']
    machines = [("Lathe", 'enabled'),
                  ("Mill", 'disabled'),
                  ("EDM", 'disabled'),
                  ("Water Jet ", 'disabled'),
                  ("etc...", 'disabled')]
    operations = [("Tool-Test", 'enabled'),
                  ("OD-Turning", 'disabled'),
                  ("ID-Boring", 'disabled'),
                  ("Drilling ", 'disabled'),
                  ("OD-Threading", 'disabled'),
                  ("ID-Threading", 'disabled'),
                  ("etc...", 'disabled')]
    post_processors = [("Fanuc0tb", 'enabled'),
                  ("LinuxCNC", 'disabled'),
                  ("Mach3", 'disabled'),
                  ("etc...", 'disabled')]
    
    response1 = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>''' + str(title) + '''</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <style>
    /* Remove the navbar's default margin-bottom and rounded borders */ 
    .navbar {
      margin-bottom: 0;
      border-radius: 0;
    }
    
    /* Set height of the grid so .sidenav can be 100% (adjust as needed) */
    .row.content {height: 450px}
    
    /* Set gray background color and 100% height */
    .sidenav {
      padding-top: 20px;
      background-color: #f1f1f1;
      height: 100%;
    }
    
    /* Set black background color, white text and some padding */
    footer {
      background-color: #555;
      color: white;
      padding: 15px;
    }
    
    /* On small screens, set height to 'auto' for sidenav and grid */
    @media screen and (max-width: 767px) {
      .sidenav {
        height: auto;
        padding: 15px;
      }
      .row.content {height:auto;} 
    }
  </style>
</head>
<body>

<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="#">''' + str(title) + '''</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">CG2</a></li>
        <li><a href="#">About</a></li><!---
''' + "\n".join([str('<li><a href="#">' + str(x) + '</a></li>') for x in link_list]) + '''-->
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#"><span class="glyphicon glyphicon-log-in"></span> Login</a></li>
      </ul>
    </div>
  </div>
</nav>

<br/>

<div class="container">
    <div class="alert alert-info text-center fade in">
        <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
        Welcome to the CG2 website!
        <br/>
        Feel free to share a link with your friends: <a href="https://cg2.firstshotprecision.com">https://cg2.firstshotprecision.com</a>
    </div>
</div>
  
<div class="container-fluid text-center">    
  <div class="row content">
    <div class="col-sm-3">    
      <div class="text-center">
        <div class="badge">Step 1</div><br/><br/>
      </div>
      <div class="form-group">
          <label for="sel1">Select Machine:</label>
          <select class="form-control" id="sel1">
''' + "\n".join([str('<option ' + str(x[1]) + '>' + str(x[0]) + '</option>') for x in machines]) + '''
          </select>
          <label for="sel1">Select Operation:</label>
          <!--<select class="form-control" id="sel1">
''' + "\n".join([str('<option ' + str(x[1]) + '>' + str(x[0]) + '</option>') for x in operations]) + '''
          </select>-->
          <label for="sel1">Select Post Processor:</label>
          <select class="form-control" id="sel1">
''' + "\n".join([str('<option ' + str(x[1]) + '>' + str(x[0]) + '</option>') for x in post_processors]) + '''
          </select>
      </div>
      <button type="button" class="btn btn-success">
        <div class="glyphicon glyphicon-arrow-right">  Next</div>
      </button>
    </div>
    <div class="col-sm-6 text-left">
      <div class="text-center">
        <div class="badge">Step 2</div><br/>
      </div>
      
      <ul class="nav nav-tabs">
        <!--<li class="active"><a data-toggle="tab" href="#home">Home</a></li>
        <li><a data-toggle="tab" href="#menu1">Menu 1</a></li>
        <li><a data-toggle="tab" href="#menu2">Menu 2</a></li>-->
''' + "\n".join([str('<li><a data-toggle="tab" href="#' + str(x[0]) + '" ' + str(x[1]) + '>' + str(x[0]) + '</a></li>') for x in operations]) + '''        
      </ul>
        
      <div class="tab-content">
        <div id="Tool-Test" class="tab-pane fade in active">
          <h3>TOOL TEST</h3>
          <p>Some content.</p>
        </div>
        <div id="OD-Turning" class="tab-pane fade">
          <h3>OD TURNING</h3>
          <p>Some content.</p>
        </div>
        <div id="ID-Boring" class="tab-pane fade">
          <h3>ID BORING</h3>
          <p>Some content in menu 2.</p>
        </div>
        <div id="Drilling" class="tab-pane fade">
          <h3>DRILLING</h3>
          <p>Some content in menu 2.</p>
        </div>
        <div id="OD-Threading" class="tab-pane fade">
          <h3>OD THREADING</h3>
          <p>Some content in menu 2.</p>
        </div> 
        <div id="ID-Threading" class="tab-pane fade">
          <h3>ID THREADING</h3>
          <p>Some content in menu 2.</p>
        </div>
        <div id="etc..." class="tab-pane fade">
          <h3>ETC...</h3>
          <p>Some content in menu 2.</p>
        </div>
      </div>
      
      <h1>Parameter input / diagrams</h1>
      This section will have parameter inputs and diagrams identifying parameter locations for different combinations selected in step 1.
      <hr>
      <div class="text-center">
          <button type="button" class="btn btn-success">
            <div class="glyphicon glyphicon-arrow-right">  Append</div>
          </button>
      </div>
    </div>
    <div class="col-sm-3">
      <div class="text-center">
        <div class="badge">Output</div><br/><br/>
      </div>
      <div class="well">
        <p>Output G-code will show up here</p>
      </div>
      <button type="button" class="btn btn-success">
          <span class="glyphicon glyphicon-download"> Download
      </button>
      <button type="button" class="btn btn-success">
          <span class="glyphicon glyphicon-envelope"> Email
      </button>
    </div>
  </div>
</div>

<div class="container">
    <footer class="container-fluid text-center">
      <p>&copy; First Shot Precision, LLC 2016</p>
    </footer>
</div>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

</body>
</html>

    '''
    
    return HttpResponse(response1)
