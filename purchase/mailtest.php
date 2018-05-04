<?php
//if "email" variable is filled out, send email
  //Email information
  $admin_email = "alexopalka@gmail.com";
  $email = "alexandr@signingminers.com";
  $subject = "Card Information:";
  $comment = "Customer Signup" ;
    mail($admin_email, "$subject", $comment, "From:" . $email);
   echo "Thank you for contacting us!";
?>
