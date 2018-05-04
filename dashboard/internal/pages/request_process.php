<?php
  $sid = $_GET['sid'];
  $password = $_POST['password'];
  $username = $_POST['username'];
  $email = $_POST['email'];
  $phone = $_POST['phone'].str_replace(" ","").str_replace("-","");
  $wallet = $_POST['btcaddress'];
  $command = 'python cashout_proc.py' . ' ' . $sid . ' ' . $email . ' ' . $username . ' '. $password . ' ' . $phone . ' ' . $wallet;
  exec($command, $output, $status);
  $sid = $output[0];
  echo $sid;
  header('Location: /dashboard/internal/pages/Cashout.php?sid=' . $sid);
?>
