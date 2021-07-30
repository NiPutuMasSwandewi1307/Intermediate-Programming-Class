import sqlloginuas
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

mydb = sqlloginuas.mydb

### User Login App Interface Command ###
class rootMyLayout(Widget):
    def ClickLogin(self):
        #Input Text
        username = self.ids.uname.text
        password = self.ids.pword.text
        
        #Fetch from the table on database namely "User"
        mycursor = mydb.cursor(dictionary = True)
        mycursor.execute("SELECT * FROM users WHERE username = %s \ and password = SHA1(%s)", (username, password))
        myresult = mycursor.fetchone()
        
        try:
            if (myresult is not None): # match between username and password
               self.ids.resultlogin.text = "Welcome %s" %myresult['name'] + " from %s" %myresult['department']
            else:
               self.ids.resultlogin.text = "Invalid Login!" # unmatch between username and password
        except:
            return

#Class of User Login App
class loginuas(App):
    def build(self):
        return rootMyLayout()

#Run User Login
if (__name__ == "__main__"):
    loginuas().run()
