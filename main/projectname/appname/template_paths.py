import os 

current_file_path = os.path.abspath(__file__)  # Get the absolute path of the current file
app_base_path = os.path.dirname(os.path.dirname(current_file_path))  # Go up two levels to the app's base directory
template_paths = {
    'home': os.path.join(app_base_path, 'appname/templates/home.html'),
    'about': os.path.join(app_base_path, 'appname/templates/about.html'),
    'contact': os.path.join(app_base_path, 'appname/templates/contact.html'),
    'courses': os.path.join(app_base_path, 'appname/templates/courses.html'),
    'playlist': os.path.join(app_base_path, 'appname/templates/playlist.html'),
    'watchvideo': os.path.join(app_base_path, 'appname/templates/watchvideo.html'),
    'profile': os.path.join(app_base_path, 'appname/templates/profile.html'),
    'login': os.path.join(app_base_path, 'appname/templates/login.html'),
    'register': os.path.join(app_base_path, 'appname/templates/register.html'),
    'teacher_profile': os.path.join(app_base_path, 'appname/templates/teacher_profile.html'),
    'teachers': os.path.join(app_base_path, 'appname/templates/teachers.html'),
    'update': os.path.join(app_base_path, 'appname/templates/update.html'),   
}





