import os 
current_file_path = os.path.abspath(__file__)  # Get the absolute path of the current file
app_base_path = os.path.dirname(os.path.dirname(current_file_path))  # Go up two levels to the app's base directory
template_path = {
    'login': os.path.join(app_base_path, 'register/templates/login.html'),
    'register': os.path.join(app_base_path, 'register/templates/register.html'),
    'update': os.path.join(app_base_path, 'register/templates/update.html'),   
}





