import getpass
import platform
import shutil


def move_to_template(file_type):
    """
    move template file to downloads directory.

    param
    --------------------
    file_type: str
        csv or xlsx

    return
    --------------------
    None
    """
    os_type = platform.system()
    user = getpass.getuser()
    # user = pwd.getpwuid(os.getuid())[0]
    if os_type == 'Darwin':
        path = f'/Users/{user}/Downloads'
        template_path = 'templates/template'
    elif os_type == 'Windows':
        path = fr'C:\Users\{user}\Downloads'
        template_path = r'.\templates\template'

    if file_type == 'csv':
        shutil.copy(f'{template_path}.csv', path)
    elif file_type == 'excel':
        shutil.copy(f'{template_path}.xlsx', path)


if __name__ == '__main__':
    pass
