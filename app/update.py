import glob
import os
import platform
import shutil

import pandas as pd

from main import ErrorPopup


def check_file(file_path):
    """
    check file extension.
    if extension is xlsx, it is changed xlsx to csv.
    if extension is neither xlsx or csv, raise error.

    param
    --------------------
    file_path: str

    return
    --------------------
    None
    """
    is_file = os.path.isfile(file_path)
    if is_file:
        file_type = file_path.split('.')[-1]
        if file_type == 'xlsx':
            unify_extension(file_path)
        elif not (file_type == 'csv' or file_type == 'xlsx'):
            raise ValueError('not supported extension')
    else:
        raise ValueError('This is not file')


def unify_extension(file_path):
    """
    extension is changed xlsx to csv.

    param
    --------------------
    file_path: str

    return
    --------------------
    None
    """
    os_type = platform.system()
    if os_type == 'Darwin':
        name = file_path.split('/')[-1].split('.')[0]
    elif os_type == 'Windows':
        name = file_path.split('\\')[-1].split('.')[0]
    df = pd.read_excel(file_path)
    df.to_csv(f'data/{name}.csv')


def remove_files(extension):
    """
    remove files selected extension.

    param
    --------------------
    extension: str

    return
    --------------------
    None
    """
    excel_files = glob.glob(f'data/*.{extension}')
    if excel_files:
        for file in excel_files:
            os.remove(file)


def move_to_data(file_path):
    """
    if extension is xlsx or csv, its file is moved data directory.

    param
    --------------------
    file_path: str

    return
    --------------------
    status message: str
    """
    os_type = platform.system()
    try:
        remove_files('csv')
        check_file(file_path[0])
        if os_type == 'Darwin':
            move_path = 'data'
            shutil.copy(file_path[0], move_path)
        elif os_type == 'Windows':
            move_path = r'.\data'
            shutil.copy(file_path[0], move_path)
        remove_files('xlsx')
        return '登録できました'
    except ValueError:
        ErrorPopup().open_popup()
        return 'ファイルを選んでください'



