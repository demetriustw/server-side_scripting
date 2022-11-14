<?php 
include("includes/includedFiles.php"); 
?>

<h1 class="pageHeadingBig PHbg">You Might Also Like</h1>

<div class="gridViewContainer borderBottom">

	<?php
		$albumQuery = mysqli_query($con, "SELECT * FROM albums ORDER BY RAND() LIMIT 7");

		while($row = mysqli_fetch_array($albumQuery)) {
			



			echo "<div class='gridViewItem'>
					<span role='link' tabindex='0' onclick='openPage(\"album.php?id=" . $row['id'] . "\")'>
						<img src='" . $row['artworkPath'] . "'>

						<div class='gridViewInfo'>"
							. $row['title'] .
						"</div>
					</span>

				</div>";



		}
	?>

</div>


<h1 class="pageHeadingBig PHbg">Your Playlists</h1>

<div class="gridViewContainer borderBottom">

	<?php
			$username = $userLoggedIn->getUsername();

			$playlistsQuery = mysqli_query($con, "SELECT * FROM playlists WHERE owner='$username' LIMIT 7");

			if(mysqli_num_rows($playlistsQuery) == 0) {
				echo "<span class='noResults'>You don't have any playlists yet.</span>";
			}

			while($row = mysqli_fetch_array($playlistsQuery)) {
			
			$playlist = new Playlist($con, $row);

			echo "<div class='gridViewItem'>
					<span role='link' tabindex='0' onclick='openPage(\"playlist.php?id=" . $playlist->getId() . "\")'>
						<img src='assets/images/icons/playlist.png'>

						<div class='gridViewInfo'>"
						. $playlist->getName() .
						"</div>
					</span>

				</div>";



		}
	?>

</div>