<?php
     $user_name = $_POST['username'];
     $user_pass = $_POST['pass'];
     // Get cURL resource
    $url = 'http://api.msunicloud.com:2404/users/login';
    $data = array('username' => $user_name, 'password' => $user_pass);
    // use key 'http' even if you send the request to https://...
    $options = array(
        'http' => array(
            'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
            'method'  => 'POST',
            'content' => http_build_query($data)) );
    $context  = stream_context_create($options);
    $result = file_get_contents($url, false, $context);
    if ($result === FALSE) {
      var_dump($result);
      header('Refresh=1;url=index.php');
    }
    $data = json_decode($result);
    $sid = $data->id;
    #echo $sid;
    echo 'Location: /dashboard/internal/pages/index.php?sid=' . $sid;
    header('Location: /dashboard/internal/pages/index.php?sid=' . $sid);
?>
