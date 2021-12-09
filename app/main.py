import glob

import japanize_kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import  NoTransition, ScreenManager, Screen
from kivy.utils import get_color_from_hex

import download
import question
# import update


class MainScreen(Screen):
    pass


# class UpdateScreen(Screen):
#     status = StringProperty('ファイルを選んでください')

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)


#     def load_english_word_file(self, file_path):
#         """
#         for register button


#         param
#         --------------------
#         file_path: str

#         return
#         --------------------
#         None
#         """
#         if file_path:
#             self.status = update.move_to_data(file_path)
#         else:
#             ErrorPopup().open_popup()

class TemplateScreen(Screen):
    check = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = 'csv'

    def on_checkbox_press(self, type):
        """
        check what did you choose from csv or xlsx.

        param
        --------------------
        type: str

        return
        --------------------
        None
        """
        self.type = type

    def download_file(self):
        """
        for Download button.
        move file chosen from csv or xlsx to downloads directory.

        param
        --------------------
        None

        return
        --------------------
        None
        """
        download.move_to_template(self.type)


class TestScreen(Screen):
    english = StringProperty('')
    japanese = StringProperty('')
    button_text = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = 0
        self.english, self.japanese = 'Startボタンを押して', 'スタート'
        self.button_text = 'Start'
        self.status = 1
        self.japanese_tmp = ''

    def on_press_button(self):
        """
        for next button.

        param
        --------------------
        None

        return
        --------------------
        None
        """
        csv_file = glob.glob('data/*.csv')
        excel_file = glob.glob('data/*.xlsx')
        if csv_file:
            self.file_path = csv_file[0]
        elif excel_file:
            self.file_path = excel_file[0]

        if self.file_path:
            if self.status:
                self.status = 0
                self.japanese = ''
                self.english, self.japanese_tmp = question.select_english_word(self.file_path)
                self.button_text = 'Answer'
            else:
                self.japanese = self.japanese_tmp
                self.status = 1
                self.button_text = 'Next'

        else:
            ErrorPopup().open_popup()


class MemorizeScreen(Screen):
    english = StringProperty('')
    japanese = StringProperty('')
    button_text = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = 0
        self.english, self.japanese = 'Startボタンを押して', 'スタート'
        self.button_text = 'Start'
        self.status = 1

    def on_press_button(self):
        """
        for next button.

        param
        --------------------
        None

        return
        --------------------
        None
        """
        csv_file = glob.glob('data/*.csv')
        excel_file = glob.glob('data/*.xlsx')
        if csv_file:
            self.file_path = csv_file[0]
        elif excel_file:
            self.file_path = excel_file[0]

        if self.file_path:
            self.english, self.japanese, self.index = question.select_english_word_for_memorize(self.file_path, self.index)
        else:
            ErrorPopup().open_popup()

        if self.status:
            self.button_text = 'Next'
            self.status = 0


class ErrorPopupScreen(Screen):
    close_popup = ObjectProperty(None)
    msg = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.msg = 'ファイルを選択し直してください。'


class ErrorPopup:
    def open_popup(self):
        """
        Open popup for error.
        param
        --------------------
        None

        return
        --------------------
        None
        """
        content = ErrorPopupScreen(close_popup=self.close_popup)
        self.popup = Popup(title='Error', content=content)
        self.popup.open()

    def close_popup(self):
        """
        Close popup for error.

        param
        --------------------
        None

        return
        --------------------
        None
        """
        self.popup.dismiss()



class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'EnglishWordsApp'

    def build(self):
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(TemplateScreen(name='template'))
        # self.sm.add_widget(UpdateScreen(name='update'))
        self.sm.add_widget(TestScreen(name='test'))
        self.sm.add_widget(MemorizeScreen(name='memorize'))
        self.sm.add_widget(ErrorPopupScreen(name='errorpopup'))
        return self.sm


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#696969')
    MainApp().run()