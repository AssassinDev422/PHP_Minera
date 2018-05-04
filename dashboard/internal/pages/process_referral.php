<?php
  $password = $_POST['password'];
  $username = $_POST['username'];
  $email = $_POST['email'];
  $referralid = $_GET['referralid'];
  $phone = $_POST['phone'].str_replace(" ","").str_replace("-","");
  $hashpower = $_POST['hashpower'];
  $command = 'python referral.py' . ' ' . $email . ' ' . $username . ' ' . $password . ' ' . $phone . ' '. $referralid . ' ' . $hashpower;
  echo $command;
  exec($command, $output, $status);
  $sid = $output[0];
  echo $sid;
  header('Location: UserProfile.php?sid=' . $sid);
?>
