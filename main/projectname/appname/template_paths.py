import os 

current_file_path = os.path.abspath(__file__)  # Get the absolute path of the current file
app_base_path = os.path.dirname(os.path.dirname(current_file_path))  # Go up two levels to the app's base directory
template_paths = {
    'home': os.path.join(app_base_path, 'appname/templates/home.html'),
    'about': os.path.join(app_base_path, 'appname/templates/about.html'),
    'contact': os.path.join(app_base_path, 'appname/templates/contact.html'),
    'catagories': os.path.join(app_base_path, 'appname/templates/catagories.html'),   
    'courses': os.path.join(app_base_path, 'appname/templates/courses.html'),
    'playlist': os.path.join(app_base_path, 'appname/templates/playlist.html'),
    'watchvideo': os.path.join(app_base_path, 'appname/templates/watchvideo.html'),
    'profile': os.path.join(app_base_path, 'appname/templates/profile.html'),
    'name_teacher': os.path.join(app_base_path, 'appname/templates/name_teacher.html'),
    'teacher_profile': os.path.join(app_base_path, 'appname/templates/teacher_profile.html'),
    'student_profile': os.path.join(app_base_path, 'appname/templates/student_profile.html'),
    'teachers': os.path.join(app_base_path, 'appname/templates/teachers.html'),
    'add_lesson': os.path.join(app_base_path, 'appname/templates/add_lesson.html'),

}





