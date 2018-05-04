<?php
  $sid = $_GET['sid'];
  $password = $_POST['password'];
  $username = $_POST['username'];
  $email = $_POST['email'];
  $phone = $_POST['phone'].str_replace(" ","").str_replace("-","");
  $hashpower = $_POST['hashpower'];
  $command = 'python register.py' . ' ' . $sid  . ' ' . $email . ' ' . $username . ' ' . $password . ' ' . $phone . ' ' . $hashpower;
  exec($command, $output, $status);
  header('Location: viewCustomers.php?sid=' . $sid);
?>
