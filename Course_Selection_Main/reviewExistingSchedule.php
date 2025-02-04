<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="reviewExistingSchedule.css">
    <title>Review Existing Schedule</title>
</head>
<body>
<?php

$filename = "data.txt";

$searchString = $_POST['fName'];

$file = fopen($filename, "r");

while(!feof($file)) {
  $line = fgets($file);

  if(strpos($line, $searchString) !== false) {
    echo $line . "<br>";
    echo "exists";
  }
}

fclose($file);


$message = "";
if(isset($_POST['fName'])){ 
  $message = "Incorrect login";
  
}    
?>
       <schedule>
            Review Existing Schedule<br><br>

            <form action="" method="post">
                <label for="fn">First name:</label>
                <input type="text" id="fn" name="fName"><br>
                <label for="ln">Last name:</label>
                <input type="text" id="ln" name="lName"><br>
                <label for="bd">Birth Date:</label>
                <input type="date" id="bd" name="bDay"><br>
                <label for="id">Student ID: </label>
                <input type="text" id="id" name="id"><br>
                <br>
                <input id="bin" type="submit" class="submitButton">
                <?
                echo "<p id='anger'>".$message."</p>"; 
                ?>
            </form>
        </schedule>
</body>
</html>
