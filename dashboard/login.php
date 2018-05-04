<html>
<head lang="en">
    <meta charset="UTF-8">
    <link type="text/css" rel="stylesheet" href="/dashboard/internal/bower_components/bootstrap/dist/css/bootstrap.css">
    <title>Login</title>
</head>
<style>
    .login-panel {
        margin-top: 150px;
      }
      .forgot{
        margin-top: 5px;
      }
</style>
<body>
<div class="container">
    <div class="row">
        <div class="col-md-4 col-md-offset-4">
            <div class="login-panel panel panel-success">
                <div class="panel-heading">
                    <h3 class="panel-title">Sign In</h3>
                </div>
                <div class="panel-body">
                  <form action="login_check.php" method="post" >
                        <fieldset>
                            <div class="form-group"  >
                                <input class="form-control" placeholder="Username" name="username"  id="username" type="text" autofocus>
                            </div>
                            <div class="form-group">
                                <input class="form-control" placeholder="Password" name="pass" id="password" type="password" value="">
                            </div>
                            <button class="btn btn-lg btn-success btn-block" type="submit" value="login" name="login" >LOGIN</button>
                            <p><br><a class="forgot" href="/dashboard/internal/pages/forgot.php">Forgot Password<a></p>
                        </fieldset>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-80189658-1', 'auto');
  ga('send', 'pageview');
</script>
</body>
</html>
