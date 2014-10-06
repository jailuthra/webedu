# Web Edu

A very simple MOOC platform in Python (Flask)

## Installation

Clone this repo

    $ git clone https://github.com/jailuthra/webedu

`cd` to the cloned directory

    $ cd webedu/

Create the courses directory, and add some video lectures

    $ mkdir -p static/courses/crypto

    $ mv ~/intro-lec.mp4 static/courses/crypto/1.mp4

**Note:** The video lecture files should be named *integer*.mp4
(or .webm or any HTML5 compatible video format)  
They will be played in numerical order.

Edit the `courses.py` file to add a full course name corrsponding
to the course's folder name.  
For an example:

```python
    course_map = ['crypto' : 'Cryptography'];
```

## Run

You can run it locally using flask

    # pip2 install flask
    # python2 app.py

The server should be up at the address 127.0.0.1:5000
Try it out on a browser

Alternatively you can host it up on any web server that can run flask

Report any bugs or feature requests to /dev/null.
Kidding, feel free to send a Pull Request ;)

## Todo

* Add CSS. Make a separate css/ directory
* Improve navigation (Perhaps a navbar at the top would do)
* Student login support (Using OAuth 2.0)

## License

All the work under this project is licensed under MIT LICENSE.
See the file LICENSE.txt for details.
