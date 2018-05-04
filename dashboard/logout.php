<?php
  $cmd = 'python logout.py ' . $_GET['sid'];
  echo $cmd;
  exec($cmd , $output, $status);
  header('Location: /dashboard/index.php');
?>
