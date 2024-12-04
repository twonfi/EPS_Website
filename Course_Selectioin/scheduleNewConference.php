<html>
    <title>Schedule New Conference</title>
    <link rel="stylesheet" href="scheduleNewConference.css">
    <header>Schedule New Conference</header>
    <script>
        function checkUsername() {                        // Declare function
  var username = el.value;                        // Store username in variable
  if (username.length < 5) {                      // If username < 5 characters
    elMsg.className = 'warning';                  // Change class on message
    elMsg.textContent = 'Not long enough, yet...';// Update message
  } else {                                        // Otherwise
    elMsg.textContent = '';                       // Clear the message
  }
}

function tipUsername() {                          // Declare function
  elMsg.className = 'tip';                        // Change class for message
  elMsg.innerHTML = 'Username must be at least 5 characters'; // Add message
}

var el = document.getElementById('fn');     // Username input
var elMsg = document.getElementById('feedback');  // Element to hold message

// When the username input gains / loses focus call functions above:
el.addEventListener('focus', tipUsername, false); // focus call tipUsername()
el.addEventListener('blur', checkUsername, false);// blur call checkUsername()
        
    </script>
    
<?
$servername = "localhost";
$username = "Ec2car3G31xCHLd";
$password = "WIy{Bxp-ZTnl";
$dbname = "ParentTeacherConferences";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}


?>
    <body>

        <div style="text-align: right;"><img src="kid.png" alt="My Image" /></div>
        <schedule>
            Schedule New Conference<br><br>

            <form  action="reviewExistingSchedule.php" method="post">
                <label for="fn">First name:</label>
                <input type="text" id="fn" name="fName" minlength="1" required><br>
                <div id="feedback"></div>
                <label for="ln">Last name:</label>
                <input type="text" id="ln" name="lName" minlength="1" required><br>
                <label for="bd">Birth Date:</label>
                <input type="date" id="bd" name="bDay" minlength="1" required><br>
                <label for="id">Student ID: </label>
                <input type="text" id="id" name="id" minlength="1" required><br>
                <br>
                <input type="submit"  id="sub" class="submitButton" minlength="1" required></input>
            </form>
        </schedule>
    </body>
</html>
