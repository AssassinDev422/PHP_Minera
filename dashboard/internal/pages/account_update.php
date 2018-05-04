<?php
  $sid = $_GET['sid'];
  $password = $_POST['password'];
  $username = $_POST['username'];
  $email = $_POST['email'];
  $phone = $_POST['phone'].str_replace(" ","").str_replace("-","");
  $wallet = $_POST['btcaddress'];
  $wallet2 = $_POST['ltcaddress'];
  $wallet3 = $_POST['dashaddress'];
  $command = 'python accountupdate.py' . ' ' . $sid . ' ' . $email . ' ' . $username . ' ' . $password . ' ' . $phone . ' ' . $wallet . ' ' . $wallet2 . ' ' . $wallet3;
  exec($command, $output, $status);
  $sid = $output[0];
  echo $sid;
  header('Location: /dashboard/internal/pages/UserProfile.php?sid=' . $sid);
?>
