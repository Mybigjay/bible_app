from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import sqlite3
Window.clearcolor = (0,0,0.2, 0.7)
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGrey"



class JanuaryCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)
    #Window.clearcolor = (0, 0, 0, 1)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""



    def JanuaryWeek1Btn(self):

        sm.current = "Januaryweek1"

    def JanuaryWeek2Btn(self):

        sm.current = "Januaryweek2"

    def JanuaryWeek3Btn(self):

        sm.current = "Januaryweek3"

    def JanuaryWeek4Btn(self):

        sm.current = "Januaryweek4"

"""  January week1"""
class Januaryweek1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Januarycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Januarycreate(self):
        self.reset()
        sm.current = "Januarycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showJanuaryweek1(self):
        with open("Januaryweek1.txt", "r") as f:
            return (f.read())


    def January1Btn(self):

        sm.current = "January1"

    def January2Btn(self):

        sm.current = "January2"
    def January3Btn(self):

        sm.current = "January3"
    def January4Btn(self):

        sm.current = "January4"
    def January5Btn(self):

        sm.current = "January5"
    def January6Btn(self):

        sm.current = "January6"
    def January7Btn(self):

        sm.current = "January7"


"""  January 1"""
class January1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    #Window.size = (1120, 630)
    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Januarycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary1(self):
        with open("January1.txt", "r") as f:
            return (f.read())
    def showJanuary1b(self):
        with open("January1b.txt", "r") as f:
            return (f.read())



"""  January 2"""
class January2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Januarycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary2(self):
        with open("January2.txt", "r") as f:
            return (f.read())

"""  January 3"""
class January3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Januarycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary3(self):
        with open("January3.txt", "r") as f:
            return (f.read())

"""  January 4"""
class January4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Januarycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary4(self):
        with open("January4.txt", "r") as f:
            return (f.read())
"""  January 5"""
class January5Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Januarycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary5(self):
        with open("January5.txt", "r") as f:
            return (f.read())


"""  January 6"""
class January6Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Januarycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary6(self):
        with open("January6.txt", "r") as f:
            return (f.read())

"""  January 7"""
class January7Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Januarycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Januaryweek1(self):

        sm.current = "Januaryweek1"



    def login(self):

        sm.current = "login"

    def showJanuary7(self):
        with open("January7.txt", "r") as f:
            return (f.read())



"""  January week2"""
class Januaryweek2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Januarycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Januarycreate(self):
        self.reset()
        sm.current = "Januarycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showJanuaryweek2(self):
        with open("Januaryweek2.txt", "r") as f:
            return (f.read())






class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)


    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def JanuaryBtn(self):

        sm.current = "Januarycreate"

    def FebBtn(self):

        sm.current = "Febcreate"

    def MarchBtn(self):

        sm.current = "Marchcreate"

    def AprilBtn(self):

        sm.current = "Aprilcreate"

    def MayBtn(self):

        sm.current = "Maycreate"
    def JuneBtn(self):

        sm.current = "Junecreate"

    def JulyBtn(self):

        sm.current = "Julycreate"

    def AugustBtn(self):

        sm.current = "Augustcreate"

    def SeptemberBtn(self):

        sm.current = "Septembercreate"

    def OctoberBtn(self):

        sm.current = "Octobercreate"

    def NovemberBtn(self):

        sm.current = "Novembercreate"

    def DecemberBtn(self):

        sm.current = "Decembercreate"







    def JanBtn(self):
        if dbjan.january1(self.JANUARY, self.WEEK1):
            MainWindow.current = self.JANUARY
            self.reset()
            """smjan.current = "main" """
        else:
            invalidLogin()
    def JanBtn(self):
        if dbjan.january2(self.JANUARY, self.WEEK1):
            MainWindow.current = self.JANUARY
            self.reset()
            """smjan.current = "main" """
        else:
            invalidLogin()




    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()



    """ def FebBtn(self):
        if db.validate(self.email.text, self.password.text):
            FebWindow.current = self.email.text
            self.reset()
            smFeb.current = "Febcreate"
        else:
            invalidLogin() """




class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    JANUARY = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created


class FebWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    JANUARY = ObjectProperty(None)
    current = ""

    def logOut(self):
        smFeb.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created

    def showFeb(self):
        with open("abcd.txt", "r") as f:
            return (f.read())

class WindowManager(ScreenManager):
    pass
class WindowManagerFeb(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()







def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


""" FEBRUAY"""


class FebCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                smFeb.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def showfeb(self):
        with open("abcd.txt", "r") as f:
            return (f.read())


""" MARCH"""
class MarchCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def showmarch(self):
        with open("march.txt", "r") as f:
            return (f.read())



""" APRIL"""

class AprilCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def showApril(self):
        with open("April.txt", "r") as f:
            return (f.read())

""" MAY"""
class MayCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""



    def MayWeek1Btn(self):

        sm.current = "Mayweek1"

    def MayWeek2Btn(self):

        sm.current = "Mayweek2"

    def MayWeek3Btn(self):

        sm.current = "Mayweek3"

    def MayWeek4Btn(self):

        sm.current = "Mayweek4"

""" may week1"""

class Mayweek1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Maycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showMayweek1(self):
        with open("mayweek1.txt", "r") as f:
            return (f.read())

""" may week2"""

class Mayweek2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Maycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def showMayweek2(self):
        with open("mayweek2.txt", "r") as f:
            return (f.read())


""" MAYWEEK 3"""

class Mayweek3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Maycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def showMayweek3(self):
        with open("mayweek3.txt", "r") as f:
            return (f.read())

""" MAYWEEK 4"""

class Mayweek4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Maycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Maycreate(self):
        self.reset()
        sm.current = "Maycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def showMayweek4(self):
        with open("mayweek4.txt", "r") as f:
            return (f.read())


""" JUNE """
class JuneCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""



    def JuneWeek1Btn(self):

        sm.current = "Juneweek1"

    def JuneWeek2Btn(self):

        sm.current = "Juneweek2"

    def JuneWeek3Btn(self):

        sm.current = "Juneweek3"

    def JuneWeek4Btn(self):

        sm.current = "Juneweek4"

""" June week1"""

class Juneweek1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Junecreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Junecreate(self):
        self.reset()
        sm.current = "Junecreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showJuneweek1(self):
        with open("juneweek1.txt", "r") as f:
            return (f.read())

""" JUNE WEEK2 """

class Juneweek2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Junecreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Junecreate(self):
        self.reset()
        sm.current = "Junecreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showJuneweek2(self):
        with open("juneweek2.txt", "r") as f:
            return (f.read())

""" JUNE WEEK3 """

class Juneweek3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Junecreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Junecreate(self):
        self.reset()
        sm.current = "Junecreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showJuneweek3(self):
        with open("juneweek3.txt", "r") as f:
            return (f.read())

""" JUNE WEEK4 """

class Juneweek4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Junecreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Junecreate(self):
        self.reset()
        sm.current = "Junecreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showJuneweek4(self):
        with open("juneweek4.txt", "r") as f:
            return (f.read())

""" JULY """
class JulyCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""



    def JulyWeek1Btn(self):

        sm.current = "Julyweek1"

    def JulyWeek2Btn(self):

        sm.current = "Julyweek2"

    def JulyWeek3Btn(self):

        sm.current = "Julyweek3"

    def JulyWeek4Btn(self):

        sm.current = "Julyweek4"


"""  JULY week1"""
class Julyweek1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Julycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Julycreate(self):
        self.reset()
        sm.current = "Julycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showJulyweek1(self):
        with open("julyweek1.txt", "r") as f:
            return (f.read())

"""  JULY week2 """
class Julyweek2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Julycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Julycreate(self):
        self.reset()
        sm.current = "Julycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showJulyweek2(self):
        with open("julyweek2.txt", "r") as f:
            return (f.read())


"""  JULY week3 """
class Julyweek3Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Julycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Julycreate(self):
        self.reset()
        sm.current = "Julycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showJulyweek3(self):
        with open("julyweek3.txt", "r") as f:
            return (f.read())



"""  JULY week4 """
class Julyweek4Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Julycreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Julycreate(self):
        self.reset()
        sm.current = "Julycreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showJulyweek4(self):
        with open("julyweek4.txt", "r") as f:
            return (f.read())


""" AUGUST """
class AugustCreateWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""



    def AugustWeek1Btn(self):

        sm.current = "Augustweek1"

    def AugustWeek2Btn(self):

        sm.current = "Augustweek2"

    def AugustWeek3Btn(self):

        sm.current = "Augustweek3"

    def AugustWeek4Btn(self):

        sm.current = "Augustweek4"

"""  AUGUST week1"""
class Augustweek1Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Augustcreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Augustcreate(self):
        self.reset()
        sm.current = "Augustcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showAugustweek1(self):
        with open("augustweek1.txt", "r") as f:
            return (f.read())

"""  AUGUST week2"""
class Augustweek2Window(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    namejan = ObjectProperty(None)
    nameFeb = ObjectProperty(None)


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "Augustcreate"
            else:
                invalidForm()
        else:
            invalidForm()

    def Augustcreate(self):
        self.reset()
        sm.current = "Augustcreate"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def login(self):
        self.reset()
        sm.current = "login"

    def showAugustweek2(self):
        with open("augustweek2.txt", "r") as f:
            return (f.read())









kv = Builder.load_file("my.kv")

sm = WindowManager()
smFeb = WindowManagerFeb()

db = DataBase("users.txt")
dbjan = DataBase("JAN.txt")

screens = [LoginWindow(name="login"),JanuaryCreateWindow(name="Januarycreate"),Januaryweek1Window(name="Januaryweek1"),January1Window(name="January1"),January2Window(name="January2"),January3Window(name="January3"),January4Window(name="January4"),January5Window(name="January5"),January6Window(name="January6"),January7Window(name="January7"),Januaryweek2Window(name="Januaryweek2"),FebCreateWindow(name="Febcreate"),MarchCreateWindow(name="Marchcreate"),AprilCreateWindow(name="Aprilcreate"),MayCreateWindow(name="Maycreate"),Mayweek1Window(name="Mayweek1"),Mayweek2Window(name="Mayweek2"),Mayweek3Window(name="Mayweek3"),Mayweek4Window(name="Mayweek4"),JuneCreateWindow(name="Junecreate"),Juneweek1Window(name="Juneweek1"),Juneweek2Window(name="Juneweek2"),Juneweek3Window(name="Juneweek3"),Juneweek4Window(name="Juneweek4"),MainWindow(name="main"),JulyCreateWindow(name="Julycreate"),Julyweek1Window(name="Julyweek1"),Julyweek2Window(name="Julyweek2"),Julyweek3Window(name="Julyweek3"),Julyweek4Window(name="Julyweek4"),AugustCreateWindow(name="Augustcreate"),Augustweek1Window(name="Augustweek1"),Augustweek2Window(name="Augustweek2"),FebWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)


sm.current = "login"


screen1 = [LoginWindow(name="login"),JanuaryCreateWindow(name="create"),FebCreateWindow(name="Febcreate"),MainWindow(name="main"),FebWindow(name="main")]
for screen in screen1:

    smFeb.add_widget(screen)

smFeb.current = "login"


class MyMainApp(App):
    def build(self):
        return sm
        return sma



if __name__ == "__main__":
    MyMainApp().run()
