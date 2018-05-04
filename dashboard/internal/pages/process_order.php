<?php
  $sid = $_GET['sid'];
  $username = $_POST['username'];
  $purchasetype = $_POST['purchasetype'];
  $hashpower = $_POST['hashpower'];
  $command = 'python order.py' . ' ' . $sid  . ' ' . $username . ' ' . $purchasetype . ' ' . $hashpower;
  echo $command;
  exec($command, $output, $status);
  header('Location: viewOrders.php?sid=' . $sid);
?>
