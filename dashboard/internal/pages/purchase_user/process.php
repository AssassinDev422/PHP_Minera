<?php

    $hashpower = intval($_POST['hashpower']);
    $hp = $hashpower;
    echo $hashpower  . ' ';
    $hashpower = $hashpower * 200;
    echo $hashpower  . ' ';
    $name = $_POST['name'];
    echo $name  . ' ';
    $cardNumber = $_POST['cardNumber'];
    echo $cardNumber  . ' ';
    $month = intval($_POST['cardExpMonth']);
    echo $month  . ' ';
    $year = intval($_POST['cardExpYear']);
    echo $year  . ' ';
    $cardCVC = $_POST['cardCVC'];
    echo $cardCVC  . ' ';
    $amount = $hashpower * 100;
    echo $amount  . ' ';
    $email = $_POST['email'];
    echo $email  . ' ';
    $phone = $_POST['phone'];
    $phone = str_replace(' ','', $phone);
    echo $phone  . ' ';
    $password = $_POST['password'];
    $command1 = 'python process.py' . ' ' . $cardNumber . ' ' . $month . ' ' . $year. ' ' . $cardCVC. ' ' . $email. ' ' . $hp . ' ' . $phone . ' ' . $password . ' ' . $name ;
    echo $command1 . ' ' ;
    exec($command1, $output1, $status1);
    echo 'Location: http://signingminers.com/dashboard/internal/pages/index.php?sid=' . $output1[0];
    header('Location: http://signingminers.com/dashboard/internal/pages/index.php?sid=' . $output1[0] );
 ?>
