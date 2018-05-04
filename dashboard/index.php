<!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="0;url=login.php">
<title>Minera CLOUD</title>
</head>
<body>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-80189658-1', 'auto');
  ga('send', 'pageview');
</script>
<script type="text/javascript" src="/dashboard/js/lib/jquery.js"></script>
<script type="text/javascript" src="/dashboard/dpd/dpd.js"></script>
<script type="text/javascript">
  dpd.users.me(function(user){
    if (user) {
      location.href = "/dashboard/internal/pages/index.php";
    } else {
      location.href = "/dashboard/login.php";
    }
  });
</script>
</body>
</html>
