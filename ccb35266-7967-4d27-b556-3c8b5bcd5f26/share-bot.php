<!DOCTYPE html>
<html>
  <head>
	<meta name="robots" content="all">
    <title>DISCORD.de</title>
  </head>
  <body style="background:linear-gradient(#1234,#4567)">
	<div style="text-align:center"><h1 style="color:red"><i><font style="background-color:green" face="Comic Sans MS">DISCORD SHARE YOUR BOT</h1>
	<form action="share-bot.php" method="post">
	<input name="url" style="color:black;background-color:red;text-align:center;width:400px" placeholder="YOUR BOT INVITE URL"><br>
	<input name="name" style="color:black;background-color:red;text-align:center;width:400px" placeholder="NAME OF YOUR BOT"><br>
	<input name="desc" style="color:black;background-color:red;text-align:center;width:400px" placeholder="WHAT IS YOUR BOT MADE FOR"><br>
	<input type="submit" style="color:white;background-color:red;width:400px" value="SHARE BOT">
	</form>
	<?php
		$url=$_POST["url"];
		$name=$_POST["name"];
		$desc=$_POST["desc"];
		if ($url=="" || $name=="" || $desc==""){

		}
		else{
			$bots=@fopen("bots.php","a+");
			fwrite($bots,'<a href="'.$url.'"><input style="color:white; background-color:blue" type="button" value="'.$name.'"><br>'.$desc."<br><br>");
			echo "<meta http-equiv='refresh' content='5; URL=bots.php'>";
		}
	?>
  </body>
</html>