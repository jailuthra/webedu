# This file is a part of webedu project, available under MIT license
# See LICENSE.txt file for details
#
# Copyright (C) 2014 Jai Luthra <me@jailuthra.in>

from glob import glob
import os

course_map = {'course_folder_name' : 'Full Course Name'}

def lectures():
    '''
    Returns a dict of all available lectures under all courses
    Example:
        lecs = courses.lectures()
        lecs = {
            'crypto': {
                    1: 'static/courses/crypto/1.mp4',
                    2: 'static/courses/crypto/2.mp4',
            },
            'ml': {
                    1: 'static/courses/ml/1-1-Intro.mp4',
            },
        }
    '''
    lectures = dict()
    for course_id in course_map:
        # For every course_id, search the folder for video files
        exts = ['mp4', 'webm', 'ogg']
        vid_files = []
        for ext in exts:
            search_exp = 'static/courses/%s/*.%s' % (course_id, ext)
            vid_files.extend(glob(search_exp))
        vid_files = sorted(vid_files)
        # Add lectures in a dict with lec_no and lec_path
        course_lecs = dict((n+1, str(x)) for n,x in enumerate(vid_files))
        # Add course_lecs dict inside another superset lectures dict
        lectures[course_id] = course_lecs
    return lectures

def list_courses():
    '''
    Returns a list of all available courses
    Example:
        courses = courses.list_courses()
        courses = [('ml', 'Machine Learning'), ('crypto', 'Cryptography')]
    '''
    courses = []
    for course_path in glob('static/courses/*'):
        course_id = os.path.basename(course_path)
        courses.append((course_id, course_map[course_id]))
    return courses
