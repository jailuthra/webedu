# This file is a part of webedu project, available under MIT license
# See LICENSE.txt file for details
#
# Copyright (C) 2014 Jai Luthra <me@jailuthra.in>

from flask import Flask, url_for, render_template
import courses

app = Flask(__name__)

lectures = courses.lectures()
course_map = courses.course_map

@app.route('/')
def home():
    courses_list = courses.list_courses()
    return render_template('index.html', courses_list = courses_list)

@app.route('/course/<course_id>')
def course(course_id=None):
    course_lecs = lectures[course_id]
    args = {
        'course_id': course_id,
        'course_name': course_map[course_id],
        'lectures': course_lecs,
    }
    return render_template('course.html', args = args);

@app.route('/course/<course_id>/<int:lec_no>')
def player(course_id, lec_no):
    args = {
        'course_name': course_map[course_id],
        'course_id': course_id,
        'lec_no': lec_no,
        'lec_path': lectures[course_id][lec_no],
        'total_lectures': len(lectures[course_id]),
    }
    return render_template('player.html', args = args)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
