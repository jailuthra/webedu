<!DOCTYPE HTML>

<?php
    include 'map/courses.php';
?>

<html>

<head>
    <title>Web Edu</title>
</head>

<body>
    <h1 id='brand' style="text-align:center;">Web Edu</h1>
    <h3 id='tagline' style="text-align:center;">A simple MOOC platform</h3>

    <p>
        Welcome to <b>Web Edu</b>.
        Watch video lectures from a range of topics.
    </p>

    <h2>Available Courses</h2>

    <ol>
<?php
    $courses = glob('courses/*', GLOB_ONLYDIR);
    foreach ($courses as $course) {
        $course_id = pathinfo($course)['basename'];
        $course_name = $course_map[$course_id];
        echo "<li><a href='course.php?id=$course_id'>$course_name</a></li>\n";
    }
?>
    </ol>

</body>

</html>
