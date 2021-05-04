<?php
//error_reporting(0);
//require 'vendor/autoload.php';
//include_once('credentials.php');

if ( isset( $_POST['submit'] ) ) {
    try {
        $time_0 = $_POST['0'];
        $time_11 = $_POST['11'];
        $time_12 = $_POST['12'];
        $time_13 = $_POST['13'];
        $time_21 = $_POST['21'];
        $time_22 = $_POST['22'];
        $time_23 = $_POST['23'];
        $time_31 = $_POST['31'];
        $time_32 = $_POST['32'];
        $time_33 = $_POST['33'];
        $time_41 = $_POST['41'];
        $time_42 = $_POST['42'];
        $time_43 = $_POST['43'];
        $count_0 = $_POST['c0'];
        $count_11 = $_POST['c11'];
        $count_12 = $_POST['c12'];
        $count_13 = $_POST['c13'];
        $count_21 = $_POST['c21'];
        $count_22 = $_POST['c22'];
        $count_23 = $_POST['c23'];
        $count_31 = $_POST['c31'];
        $count_32 = $_POST['c32'];
        $count_33 = $_POST['c33'];
        $count_41 = $_POST['c41'];
        $count_42 = $_POST['c42'];
        $count_43 = $_POST['c43'];
        $pro0 = filter_var($_POST['pro0'], FILTER_SANITIZE_STRING);
        $pro1_1 = filter_var($_POST['pro1_1'], FILTER_SANITIZE_STRING);
        $pro1_2 = filter_var($_POST['pro1_2'], FILTER_SANITIZE_STRING);
        $pro1_3 = filter_var($_POST['pro1_3'], FILTER_SANITIZE_STRING);
        $pro2_1 = filter_var($_POST['pro2_1'], FILTER_SANITIZE_STRING);
        $pro2_2 = filter_var($_POST['pro2_2'], FILTER_SANITIZE_STRING);
        $pro2_3 = filter_var($_POST['pro2_3'], FILTER_SANITIZE_STRING);
        $pro3_1 = filter_var($_POST['pro3_1'], FILTER_SANITIZE_STRING);
        $pro3_2 = filter_var($_POST['pro3_2'], FILTER_SANITIZE_STRING);
        $pro3_3 = filter_var($_POST['pro3_3'], FILTER_SANITIZE_STRING);
        $pro4_1 = filter_var($_POST['pro4_1'], FILTER_SANITIZE_STRING);
        $pro4_2 = filter_var($_POST['pro4_2'], FILTER_SANITIZE_STRING);
        $pro4_3 = filter_var($_POST['pro4_3'], FILTER_SANITIZE_STRING);
        $fname = filter_var($_POST['fname'], FILTER_SANITIZE_STRING);
        $lname = filter_var($_POST['lname'], FILTER_SANITIZE_STRING);
        $age = filter_var($_POST['age'], FILTER_SANITIZE_STRING);
        $gender = filter_var($_POST['gender'], FILTER_SANITIZE_STRING);
        $email = filter_var($_POST['email'], FILTER_SANITIZE_STRING);
        $flag = 1;

        $response = array();
        $userdetails = array($fname, $lname, $age, $gender, $email);
        $prototype0 = array($pro0, $time_0, $count_0);
        $prototype1 = array($pro1_1, $pro1_2, $pro1_3, $time_11, $time_12, $time_13, $count_11, $count_12, $count_13);
        $feedback1 = array($_POST['likert_fb1_1'], $_POST['likert_fb1_2'], $_POST['likert_fb1_3'], $_POST['text_fb1_1'], $_POST['text_fb1_2']);
        $prototype2 = array($pro2_1, $pro2_2, $pro2_3, $time_21, $time_22, $time_23, $count_21, $count_22, $count_23);
        $feedback2 = array($_POST['likert_fb2_1'], $_POST['likert_fb2_2'], $_POST['likert_fb2_3'], $_POST['text_fb2_1'], $_POST['text_fb2_2']);
        $prototype3 = array($pro3_1, $pro3_2, $pro3_3, $time_31, $time_32, $time_33, $count_31, $count_32, $count_33);
        $feedback3 = array($_POST['likert_fb3_1'], $_POST['likert_fb3_2'], $_POST['likert_fb3_3'], $_POST['text_fb3_1'], $_POST['text_fb3_2']);
        $prototype4 = array($pro4_1, $pro4_2, $pro4_3, $time_41, $time_42, $time_43, $count_41, $count_42, $count_43);
        $feedback4 = array($_POST['likert_fb4_1'], $_POST['likert_fb4_2'], $_POST['likert_fb4_3'], $_POST['text_fb4_1'], $_POST['text_fb4_2']);

        $response['userdetails'] = $userdetails;
        $response['prototype0'] = $prototype0;
        $response['prototype1'] = $prototype1;
        $response['feedback1'] = $feedback1;
        $response['prototype2'] = $prototype2;
        $response['feedback2'] = $feedback2;
        $response['prototype3'] = $prototype3;
        $response['feedback3'] = $feedback3;
        $response['prototype4'] = $prototype4;
        $response['feedback4'] = $feedback4;

// to send email
/*
        $FROM_EMAIL = 'bharath.subramanian@gatech.edu';
        $TO_EMAIL = 'bharath.subramanian@gatech.edu';

        $htmlContent = json_encode($response);;

        $from = new SendGrid\Email(null, $FROM_EMAIL);
        $subject = "Survey response from " . $fname . " " . $lname;
        $to = new SendGrid\Email(null, $TO_EMAIL);
        $content = new SendGrid\Content("text/plain", $htmlContent);
        $mail = new SendGrid\Mail($from, $subject, $to, $content);

        $email2 = new SendGrid\Email(null, "aditi.shah@gatech.edu");
        $mail->personalization[0]->addTo($email2);
        $email3 = new SendGrid\Email(null, "svkarimi15@gmail.com");
        $mail->personalization[0]->addTo($email3);
        $email4 = new SendGrid\Email(null, "vfanelle@gmail.com");
        $mail->personalization[0]->addTo($email4);

        $sg = new \SendGrid($apiKey);

        $res = $sg->client->mail()->send()->post($mail);

        if ($res->statusCode() == 202) {
            echo "<h2>Your responses are recorded successfully! Thank you for your time.</h2>";
        }
        else{
            echo '<h2>Your responses are not recorded!!!</h2>';
        } */


// connect to postgresql

        $host        = "host = ec2-54-221-215-228.compute-1.amazonaws.com";
        $port        = "port = 5432";
        $dbname      = "dbname = d1r97om49rojm2";
        $credentials = "user = nqusdlggfpwxmf password = 89d5750729154a2dd9ab923a762fdc5cfcef96fccd97f774a11867f4c6dcf48e";

        $db = pg_connect( "$host $port $dbname $credentials"  ) or die ("Could not connect to server\n");

        //check for duplicate values
        $sql = "SELECT flag FROM survey1 WHERE email = '$email'";
        $result = pg_exec($db, $sql);
        $numrows = pg_numrows($result);
        if($numrows != 0) {
            echo "You have already participated in the survey!";
            pg_close($db);
        }
        //insert value
        $sql = "INSERT INTO survey1 VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19,$20,$21,$22,$23,$24,$25,$26,$27,$28,$29,$30,$31,$32,$33,$34,$35,$36,$37,$38,$39,$40,$41,$42,$43,$44,$45,$46,$47,$48,$49,$50,$51,$52,$53,$54,$55,$56,$57,$58,$59,$60,$61,$62,$63,$64,$65)";
        $result = pg_prepare($db, 'my_insert', $sql);
        $result = pg_execute($db, 'my_insert', array($email, $fname, $lname, $age, $gender, $flag, $pro0, $time_0, $count_0, $pro1_1, $pro1_2, $pro1_3, $time_11, $time_12, $time_13, $count_11, $count_12, $count_13, $_POST['likert_fb1_1'], $_POST['likert_fb1_2'], $_POST['likert_fb1_3'], $_POST['text_fb1_1'], $_POST['text_fb1_2'], $pro2_1, $pro2_2, $pro2_3, $time_21, $time_22, $time_23, $count_21, $count_22, $count_23,$_POST['likert_fb2_1'], $_POST['likert_fb2_2'], $_POST['likert_fb2_3'], $_POST['text_fb2_1'], $_POST['text_fb2_2'], $pro3_1, $pro3_2, $pro3_3, $time_31, $time_32, $time_33, $count_31, $count_32, $count_33, $_POST['likert_fb3_1'], $_POST['likert_fb3_2'], $_POST['likert_fb3_3'], $_POST['text_fb3_1'], $_POST['text_fb3_2'], $pro4_1, $pro4_2, $pro4_3, $time_41, $time_42, $time_43, $count_41, $count_42, $count_43, $_POST['likert_fb4_1'], $_POST['likert_fb4_2'], $_POST['likert_fb4_3'], $_POST['text_fb4_1'], $_POST['text_fb4_2'])) or die("\nError while inserting.");
        if($result){
            echo "Your responses are recorded successfully. Thank you!!!";
        }
        pg_close($db);
    }


    catch (Exception $e){
        echo 'Caught exception: ',  $e->getMessage(), "\n";
        echo '<h2>Your responses are not recorded!!!</h2>';
    }
}

/*
SQL queries
to create table
create table survey1 (email VARCHAR(50) PRIMARY KEY, fname VARCHAR(50), lname VARCHAR(50), age INTEGER, gender VARCHAR(10), flag INTEGER DEFAULT 0, pro0 text, time_0 NUMERIC, count_0 INTEGER, pro1_1 TEXT, pro1_2 TEXT, pro1_3 TEXT, time_11 NUMERIC, time_12 NUMERIC, time_13 NUMERIC, count_11 INTEGER, count_12 INTEGER, count_13 INTEGER, likert_fb1_1 TEXT, likert_fb1_2 TEXT, likert_fb1_3 TEXT, text_fb1_1 TEXT, text_fb1_2 TEXT, pro2_1 TEXT, pro2_2 TEXT, pro2_3 TEXT, time_21 NUMERIC, time_22 NUMERIC, time_23 NUMERIC, count_21 INTEGER, count_22 INTEGER, count_23 INTEGER, likert_fb2_1 TEXT, likert_fb2_2 TEXT, likert_fb2_3 TEXT, text_fb2_1 TEXT, text_fb2_2 TEXT, pro3_1 TEXT, pro3_2 TEXT, pro3_3 TEXT, time_31 NUMERIC, time_32 NUMERIC, time_33 NUMERIC, count_31 INTEGER, count_32 INTEGER, count_33 INTEGER, likert_fb3_1 TEXT, likert_fb3_2 TEXT, likert_fb3_3 TEXT, text_fb3_1 TEXT, text_fb3_2 TEXT, pro4_1 TEXT, pro4_2 TEXT, pro4_3 TEXT, time_41 NUMERIC, time_42 NUMERIC, time_43 NUMERIC, count_41 INTEGER, count_42 INTEGER, count_43 INTEGER, likert_fb4_1 TEXT, likert_fb4_2 TEXT, likert_fb4_3 TEXT, text_fb4_1 TEXT, text_fb4_2 TEXT);

To copy db to csv
\copy survey1 to survey1.csv delimiter ',';

*/
?>