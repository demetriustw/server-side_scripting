<?php
include("includes/includedFiles.php");
?>

<div class="userDetails">

	<div class="container borderBottom">
		<h2>USERNAME</h2>
		<input type="text" class="username" name="username" placeholder="Username..."  value="<?php /** echo $userLoggedIn->getUsername(); */?> NOT WORKING CAN'T GET TO WORK AND TO FRUSTRATED BY">
		<span class="message"></span>
		<button class="button" onclick="updateUsername('username')">SAVE</button>
	</div>

	<div class="container">
		<h2>PASSWORD</h2>
		<input type="password" class="oldPassword" name="oldPassword" placeholder="Current password">
		<input type="password" class="newPassword1" name="newPassword1" placeholder="New password">
		<input type="password" class="newPassword2" name="newPassword2" placeholder="Confirm password">
		<span class="message"></span>
		<button class="button" onclick="updatePassword('oldPassword', 'newPassword1', 'newPassword2')">SAVE</button>
	</div>

</div>