<!DOCTYPE HTML>

<?php
    include 'map/courses.php';
    $course_id = $_GET['id'];
    $course_name = $course_map[$course_id];
?>

<html>

<head>
    <title>Web Edu - <?= $course_name ?></title>
</head>

<body>
    <h1 id='course_name'><?= $course_name ?></h1>
    <h3>Lectures</h3>
    <ul id='lectures'>

<?php 
    $files = glob('courses/'. $course_id . '/*.{mp4,avi,webm}', GLOB_BRACE);
    foreach ($files as $file) {
        // Extract lecture number from the filename
        $lec_no = pathinfo($file)['filename'];
            echo "<li><a href='player.php?course=$course_id&lec=$lec_no'>".
            "Lecture $lec_no</a></li>\n";
    }
?>

    </ul>
</body>

</html>
