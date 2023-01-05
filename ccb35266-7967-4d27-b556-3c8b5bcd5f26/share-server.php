<!DOCTYPE html>
<html>
  <head>
	<meta name="robots" content="all">
    <title>DISCORD.de</title>
  </head>
  <body style="background:linear-gradient(#1234,#4567)">
	<div style="text-align:center"><h1 style="color:red"><i><font style="background-color:green" face="Comic Sans MS">DISCORD SHARE YOUR SERVER</h1>
	<form action="share-server.php" method="post">
	<input name="url" style="color:black;background-color:red;text-align:center;width:400px" placeholder="YOUR SERVER INVITE URL"><br>
	<input name="name" style="color:black;background-color:red;text-align:center;width:400px" placeholder="NAME OF YOUR SERVER"><br>
	<input name="desc" style="color:black;background-color:red;text-align:center;width:400px" placeholder="WHAT IS YOUR SERVER MADE FOR"><br>
	<input type="submit" style="color:white;background-color:red;width:400px" value="SHARE SERVER">
	</form>
	<?php
		$url=$_POST["url"];
		$name=$_POST["name"];
		$desc=$_POST["desc"];
		if ($url=="" || $name=="" || $desc==""){

		}
		else{
			$bots=@fopen("servers.php","a+");
			fwrite($bots,'<a href="'.$url.'"><input style="color:white; background-color:blue" type="button" value="'.$name.'"><br>'.$desc."<br><br>");
			echo "<meta http-equiv='refresh' content='5; URL=servers.php'>";
		}
	?>
  </body>
</html>