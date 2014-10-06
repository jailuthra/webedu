from flask import Flask, url_for, render_template
from glob import glob
import os
from courses import course_map, update_lectures

app = Flask(__name__)

course_lectures = dict()

@app.route('/course/<course_id>/<int:lec_no>')
def player(course_id, lec_no):
    return render_template('player.html', course_name = course_map[course_id],
                            lec_no = lec_no, lec_path = course_lectures[course_id][lec_no])

@app.route('/course/<course_id>')
def course(course_id=None):
    global course_lectures
    course_lectures = update_lectures()
    lectures = course_lectures[course_id]
    return render_template('course.html', course_id = course_id,
                            course_name = course_map[course_id],
                            lectures = lectures)

@app.route('/')
def home():
    courses = []
    for course_path in glob('static/courses/*'):
        course_id = os.path.basename(course_path)
        courses.append((course_id, course_map[course_id]))
    return render_template('index.html', courses = courses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
