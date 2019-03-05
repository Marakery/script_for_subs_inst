'''
Created on 25 февр. 2019 г.

@author: mrk
'''

from tkinter import *
import requests
import time
import random



def start_getsubs(username, id):
    device_id = id
    username = username
    
    url = 'https://followmania.vip/Send?postTag=c2VsYW1rYW5rYWJ1YmlyYmFzZTY0&device_id=' + device_id
    url_get = 'https://followmania.vip/GetUserInfo?postTag=c2VsYW1rYW5rYWJ1YmlyYmFzZTY0&device_id=' + device_id

    followers = 'followers'
    #followers_count = '1'
    credi_count = '2'

    random_subs_value = random.randint(1,15)
    user_info = requests.get(url_get)
    
    
    resp = requests.post(
        url,
        json=dict(
                  device_id=device_id, 
                  username=username, 
                  type=followers, 
                  followers_count=random_subs_value, 
                  credi_count=credi_count
                  ),
        #verify=False,
    )
    data = resp.text
    # or if you expect json response
    data = resp.json()
    print(username,' ', user_info.text,' : ', data) 
 
 
def start():
    global secs

    if id_account.get() == 'id' or username.get() == 'username':
        enter_data('ENTER DATA', 'red')
    else:
        enter_data('WORKING', 'green')
            
    
    #new_winF()
        secs = 2
        beeper()  # start repeated checking

def beeper():
    global after_id
    global secs
    global username
    global id_account
    global counter
    
    id_input = id_account.get()
    ur_nickName = id_account.get() 
    secs += 1
    
    if secs % 2 == 0:  # every other second
        start_getsubs(ur_nickName, id_input)
        counter += 1
#         time.sleep(10)
    
    after_id = root.after(5000, beeper)  # check again in 1 second
    

def stop():
    global after_id
    if after_id:
        root.after_cancel(after_id)
        after_id = None



class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


if __name__ == '__main__':


    FREQ = 2500
    DUR = 300
    
    after_id = None
    secs = 0
    counter = 0


    root = Tk()
    id_account = EntryWithPlaceholder(root, "id")
    username = EntryWithPlaceholder(root, "username")
    
    
    root.title('InstFol')
    root.geometry('200x150')
    
    def enter_data(string, color):
        newwin = Toplevel(root)
        #newwin.geometry('100x100')
        display = Label(newwin, text=string,foreground=color)
        display.pack()   
        newwin.after(2000, lambda: newwin.destroy())
    
#     def new_winF(): # new window definition
#         newwin = Toplevel(root)
#         display = Label(newwin, text="Working !")
#         display.pack()   
#         newwin.after(1000, lambda: newwin.destroy()) 

   # button1=Button(root, text ="open new window", command =new_winF) #command linked
 




    startButton = Button(root, height=2, width=20, text="Start",
                                 command=start)
    stopButton = Button(root, height=2, width=20, text="Stop",
                                command=stop)
    
    id_account.pack()
    username.pack() 
    startButton.pack()
    stopButton.pack()
    
    
    
 
    root.mainloop()

