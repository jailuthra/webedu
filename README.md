# Web Edu

A very simple MOOC platform in PHP

## Installation

Clone this repo

    $ git clone https://github.com/jailuthra/webedu

`cd` to the cloned directory

    $ cd webedu/

Create the courses directory, and add some video lectures

    $ mkdir -p courses/crypto

    $ mv ~/intro-lec.mp4 courses/crypto/1.mp4

**Note:** The video lecture files should be named *integer*.mp4
(or .webm or any HTML5 compatible video format)  
They will be played in numerical order.

Edit the `maps/courses.php` file to add a full course name corrsponding
to the course's folder name.  
For an example:

```php
<?php
    $course_map = ['crypto' => 'Cryptography'];
?>
```

## Run

You can run it locally using php5

    # php -S 127.0.0.1:80 -t .

The server should be up at the address 127.0.0.1 (or localhost)  
Try it out on a browser

Alternatively you can host it up on any server that can run php code

Report any bugs or feature requests to /dev/null.
Kidding, feel free to send a Pull Request ;)

## Todo

* Add CSS. Make a separate css/ directory
* Improve navigation (Perhaps a navbar at the top would do)
* Student login support (Using OAuth 2.0)

## License

All the work under this project is licensed under MIT LICENSE.
See the file LICENSE.txt for details.
