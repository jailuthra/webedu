from glob import glob

course_map = {'course_folder_name' : 'Full Course Name'}

def update_lectures():
    course_lectures = dict()
    for course_id in course_map:
        vid_files = sorted(glob('static/courses/%s/*.mp4' % course_id))
        lectures = dict((n+1, str(x)) for n,x in enumerate(vid_files))
        course_lectures[course_id] = lectures
    return course_lectures
