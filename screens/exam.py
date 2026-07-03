from kivy.uix.screenmanager import Screen


class ExamScreen(Screen):
    def finish_exam(self):
        self.manager.current = "dashboard"
