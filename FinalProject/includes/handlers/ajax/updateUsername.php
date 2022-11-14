<?php
include("../../config.php");

if(!isset($_POST['username'])) {
	echo "ERROR: Could not set username";
	exit();
}

if(isset($_POST['username']) && $_POST['username'] != "") {

	$username = $_POST['username'];
	$newUsername = $_POST['username'];

	$usernameCheck = mysqli_query($con, "SELECT username FROM users WHERE username='$newUsername' AND username != '$username'");
	if(mysqli_num_rows($usernameCheck) > 0) {
		echo "Username is already in use";
		exit();
	}

	$updateQuery = mysqli_query($con, "UPDATE users SET username = '$newUsername' WHERE username='$username'");
	echo "Update successful";

}
else {
	echo "You must provide a username";
}

?>