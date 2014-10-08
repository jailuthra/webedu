# This file is a part of webedu project, available under MIT license
# See LICENSE.txt file for details
#
# Copyright (C) 2014 Jai Luthra <me@jailuthra.in>

from flask import Flask, url_for, render_template
from glob import glob
import os
import courses

app = Flask(__name__)

course_lectures = courses.update_lectures()
course_map = courses.course_map

@app.route('/')
def home():
    courses = []
    for course_path in glob('static/courses/*'):
        course_id = os.path.basename(course_path)
        courses.append((course_id, course_map[course_id]))
    return render_template('index.html', courses = courses)

@app.route('/course/<course_id>')
def course(course_id=None):
    lectures = course_lectures[course_id]
    return render_template('course.html', course_id = course_id,
                            course_name = course_map[course_id],
                            lectures = lectures)

@app.route('/course/<course_id>/<int:lec_no>')
def player(course_id, lec_no):
    args = {
        'course_name': course_map[course_id],
        'course_id': course_id,
        'lec_no': lec_no,
        'lec_path': course_lectures[course_id][lec_no],
        'total_lectures': len(course_lectures[course_id]),
    }
    return render_template('player.html', args = args)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
