<?php
  $username = $_POST['username'];
  $command = 'python forgot.py' . ' ' . $username ;
  exec($command, $output, $status);
  header('Location: index.php');
?>
