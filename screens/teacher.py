from kivy.uix.screenmanager import Screen


class TeacherScreen(Screen):
    def open_exam(self):
        self.manager.current = "exam"
