<!DOCTYPE HTML>

<?php
    $course_id = $_GET['id'];
    $course_map = ['ml' => 'Machine Learning'];
    $course_name = $course_map[$course_id];
?>

<html>

<head>
    <title>Web Edu - <?= $course_name ?></title>
</head>

<body>
    <h1><?= $course_name ?></h1>
    <h3>Lectures</h3>
    <ul>

<?php 
    $files = glob('courses/'. $course_id . '/*.{mp4,avi,webm}', GLOB_BRACE);
    foreach($files as $file) {
        $lec_no = pathinfo($file)['filename'];
            echo "<li><a href='$file'>Lecture $lec_no</a></li>\n";
    }
?>

    </ul>
</body>

</html>
