<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Minera</title>
    <!-- Bootstrap Core CSS -->
    <link href="/dashboard/internal/bower_components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- MetisMenu CSS -->
    <link href="/dashboard/internal/bower_components/metisMenu/dist/metisMenu.min.css" rel="stylesheet">
    <!-- Timeline CSS -->
    <link href="/dashboard/internal/dist/css/timeline.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link href="/dashboard/internal/dist/css/sb-admin-2.css" rel="stylesheet">
    <!-- Morris Charts CSS -->
    <link href="/dashboard/internal/bower_components/morrisjs/morris.css" rel="stylesheet">
    <!-- Custom Fonts -->
    <link href="/dashboard/internal/bower_components/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
    <style>
    /* Padding - just for asthetics on Bootsnipp.com */
    body { margin-top:20px; }

    /* CSS for Credit Card Payment form */
    .credit-card-box .panel-title {
        display: inline;
        font-weight: bold;
    }
    .credit-card-box .form-control.error {
        border-color: red;
        outline: 0;
        box-shadow: inset 0 1px 1px rgba(0,0,0,0.075),0 0 8px rgba(255,0,0,0.6);
    }
    .credit-card-box label.error {
      font-weight: bold;
      color: red;
      padding: 2px 8px;
      margin-top: 2px;
    }
    .credit-card-box .payment-errors {
      font-weight: bold;
      color: red;
      padding: 2px 8px;
      margin-top: 2px;
    }
    .credit-card-box label {
        display: block;
    }
    /* The old "center div vertically" hack */
    .credit-card-box .display-table {
        display: table;
    }
    .credit-card-box .display-tr {
        display: table-row;
    }
    .credit-card-box .display-td {
        display: table-cell;
        vertical-align: middle;
        width: 50%;
    }
    /* Just looks nicer */
    .credit-card-box .panel-heading img {
        min-width: 180px;
    }

    .this_center{
      padding-top: 90px;
    }
    .panel-login {
    border-color: #ccc;
    -webkit-box-shadow: 0px 2px 3px 0px rgba(0,0,0,0.2);
    -moz-box-shadow: 0px 2px 3px 0px rgba(0,0,0,0.2);
    box-shadow: 0px 2px 3px 0px rgba(0,0,0,0.2);
    }
    .panel-login>.panel-heading {
    color: #00415d;
    background-color: #fff;
    border-color: #fff;
    text-align:center;
    }
    .panel-login>.panel-heading a{
    text-decoration: none;
    color: #666;
    font-weight: bold;
    font-size: 15px;
    -webkit-transition: all 0.1s linear;
    -moz-transition: all 0.1s linear;
    transition: all 0.1s linear;
    }
    .panel-login>.panel-heading a.active{
    color: #029f5b;
    font-size: 18px;
    }
    .panel-login>.panel-heading hr{
    margin-top: 10px;
    margin-bottom: 0px;
    clear: both;
    border: 0;
    height: 1px;
    background-image: -webkit-linear-gradient(left,rgba(0, 0, 0, 0),rgba(0, 0, 0, 0.15),rgba(0, 0, 0, 0));
    background-image: -moz-linear-gradient(left,rgba(0,0,0,0),rgba(0,0,0,0.15),rgba(0,0,0,0));
    background-image: -ms-linear-gradient(left,rgba(0,0,0,0),rgba(0,0,0,0.15),rgba(0,0,0,0));
    background-image: -o-linear-gradient(left,rgba(0,0,0,0),rgba(0,0,0,0.15),rgba(0,0,0,0));
    }
    .panel-login input[type="text"],.panel-login input[type="email"],.panel-login input[type="password"] {
    height: 45px;
    border: 1px solid #ddd;
    font-size: 16px;
    -webkit-transition: all 0.1s linear;
    -moz-transition: all 0.1s linear;
    transition: all 0.1s linear;
    }
    .panel-login input:hover,
    .panel-login input:focus {
    outline:none;
    -webkit-box-shadow: none;
    -moz-box-shadow: none;
    box-shadow: none;
    border-color: #ccc;
    }
    .btn-login {
    background-color: #59B2E0;
    outline: none;
    color: #fff;
    font-size: 14px;
    height: auto;
    font-weight: normal;
    padding: 14px 0;
    text-transform: uppercase;
    border-color: #59B2E6;
    }
    .btn-login:hover,
    .btn-login:focus {
    color: #fff;
    background-color: #53A3CD;
    border-color: #53A3CD;
    }
    .forgot-password {
    text-decoration: underline;
    color: #888;
    }
    .forgot-password:hover,
    .forgot-password:focus {
    text-decoration: underline;
    color: #666;
    }

    .btn-register {
    background-color: #1CB94E;
    outline: none;
    color: #fff;
    font-size: 14px;
    height: auto;
    font-weight: normal;
    padding: 14px 0;
    text-transform: uppercase;
    border-color: #1CB94A;
    }
    .btn-register:hover,
    .btn-register:focus {
    color: #fff;
    background-color: #1CA347;
    border-color: #1CA347;
    }

</style>
</head>

<body>

  <div id="wrapper">
          <div class="container-fluid">
              <!-- /.row -->
              <br>
              <div class="row">
              <div class="col-lg-12">
              <div class="this_center">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-6 col-md-offset-3">
                      <div class="panel panel-login">
                        <div class="panel-body">
                          <div class="row">
                            <div class="col-lg-12">
                               <!-- CREDIT CARD FORM STARTS HERE -->
                               <div class="panel panel-default credit-card-box">
                                  <img class="img-responsive pull-right" src="http://i76.imgup.net/accepted_c22e0.png">
                                   <div class="panel-body">
                                       <form role="form" id="payment-form" method="POST" action="process.php">
                                           <div class="row">
                                               <div class="col-xs-12">
                                                   <div class="form-group">
                                                       <label for="cardNumber">CARD NUMBER</label>
                                                       <div class="input-group">
                                                           <input
                                                               type="tel"
                                                               class="form-control"
                                                               name="cardNumber"
                                                               placeholder="Valid Card Number"
                                                               autocomplete="cc-number"
                                                               required autofocus
                                                           />
                                                           <span class="input-group-addon"><i class="fa fa-credit-card"></i></span>
                                                       </div>
                                                   </div>
                                               </div>
                                           </div>
                                           <div class="row">
                                               <div class="col-xs-7 col-md-7">
                                                   <div class="form-group">
                                                       <label for="cardExpiry"><span class="hidden-xs">EXPIRATION</span><span class="visible-xs-inline">EXP</span> MONTH </label>
                                                       <input
                                                           type="tel"
                                                           class="form-control"
                                                           name="cardExpMonth"
                                                           placeholder="MM"
                                                           autocomplete="cc-exp"
                                                           maxlength="2"
                                                           required
                                                       />
                                                   </div>
                                               </div>
                                               <div class="col-xs-5 col-md-5 pull-right">
                                                 <div class="form-group">
                                                     <label for="cardExpiry"><span class="hidden-xs">EXPIRATION</span><span class="visible-xs-inline">EXP</span> YEAR </label>
                                                     <input
                                                         type="tel"
                                                         class="form-control"
                                                         name="cardExpYear"
                                                         placeholder="MM"
                                                         autocomplete="cc-exp"
                                                         maxlength="2"
                                                         required
                                                     />
                                                 </div>
                                               </div>
                                           </div>
                                           <div class="row">
                                               <div class="col-xs-12">
                                                 <div class="form-group">
                                                     <label for="cardCVC">CV CODE</label>
                                                     <input
                                                         type="tel"
                                                         class="form-control"
                                                         name="cardCVC"
                                                         placeholder="CVC"
                                                         autocomplete="cc-csc"
                                                         required
                                                     />
                                                 </div>
                                               </div>
                                           </div>
                                           <div class="row">
                                               <div class="col-xs-12">
                                                   <div class="form-group">
                                                       <label for="hashpower">HASHPOWER</label>
                                                       <input type="text" class="form-control" name="hashpower" />
                                                   </div>
                                               </div>
                                           </div>
                                           <div class="row">
                                               <div class="col-xs-12">
                                                  <input type="submit" name="register-submit" id="register-submit" tabindex="4" class="form-control btn btn-register" value="Purchase">
                                               </div>
                                           </div>
                                           <div class="row" style="display:none;">
                                               <div class="col-xs-12">
                                                   <p class="payment-errors"></p>
                                               </div>
                                           </div>
                                       </form>
                                   </div>
                               </div>
                               <!-- CREDIT CARD FORM ENDS HERE -->
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
          </div>
          <!-- /.container-fluid -->
      </div>
  <!-- /.container-fluid -->
  </div>
  </div>
  <!-- /#wrapper -->
  </div>
  <!-- /#wrapper -->
    <!-- jQuery -->
    <script src="/dashboard/internal/bower_components/jquery/dist/jquery.min.js"></script>
    <!-- Bootstrap Core JavaScript -->
    <script src="/dashboard/internal/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>
    <!-- Metis Menu Plugin JavaScript -->
    <script src="/dashboard/internal/bower_components/metisMenu/dist/metisMenu.min.js"></script>
    <!-- DataTables JavaScript -->
    <script src="/dashboard/internal/bower_components/datatables/media/js/jquery.dataTables.min.js"></script>
    <script src="/dashboard/internal/bower_components/datatables-plugins/integration/bootstrap/3/dataTables.bootstrap.min.js"></script>
    <!-- Custom Theme JavaScript -->
    <script src="/dashboard/internal/dist/js/sb-admin-2.js"></script>
    <!-- Page-Level Demo Scripts - Tables - Use for reference -->
    <script>
    $(document).ready(function() {
        $('#dataTables-example').DataTable({
                responsive: true
        });
        $('#dataTables-example2').DataTable({
                responsive: true
        });
    });
    </script>
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
