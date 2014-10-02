<!DOCTYPE HTML>

<html>

<head>
  <title>Lecture</title>
</head>

<body>

<?php
  $course = $_GET["course"];
  $lec = $_GET["lec"];
  $src = "courses/$course/$lec.mp4";

  echo "<video src='$src' controls autoplay>";
  echo "</video>"
?>

</body>

</html>
