<?php
include("includes/includedFiles.php");
?>

<div class="personalDetails">

	<div class="container borderBottom">
		<h2>EMAIL</h2>
		<input type="text" class="email" name="email" placeholder="Email address..." value="<?php echo $userLoggedIn->getEmail(); ?>">
		<span class="message"></span>
		<button class="button" onclick="updateEmail('email')">SAVE</button>
	</div>

	<div class="container">
		<h2>FIRST AND LAST NAME</h2>
		<input type="text" class="firstAndlastName" name="firstAndlastName" placeholder="First and last name" value="<?php echo $userLoggedIn->getFirstAndLastName(); ?>">
		<span class="message"></span>
		<button class="button" onclick="updateFirstAndLastName('firstAndlastName')">SAVE</button>
	</div>

</div>