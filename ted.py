##http://bit.do/list-of-url-shorteners.php
##http://www.hongkiat.com/blog/url-shortening-services-the-ultimate-list/
import random,webbrowser,os
from tkinter import *
from tkinter import messagebox
FILE_HISTORY = 'history.dat'
vchars = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
history = []
#settings in order Warn_Skiplink , History_Track , Session_History
settings = []
##settings do double check when adding new settings that every setting is added in all the procs properly
#Menu_settings_window_DATA = []##global datastore for settings window maynot need as objectified
root = Tk()
linktype_Radio = IntVar()
linktype_Random = IntVar()
gennedlink = StringVar()
def openrng():##button funct
    global gennedlink
    global settings
    print('link = ',gennedlink.get())
    #0 = prompt
    print(settings[0])
    if int(settings[0]) == 1:##functionise instead?
        print('no prompt')
        webbrowser.open(gennedlink.get())
        
    else:
        if messagebox.askokcancel(title = 'confirm open',message = 'are you sure\nthere is NO guaruntee the link will be safe!'):
            webbrowser.open(gennedlink.get())
        
    
def googlehome():##button funct
    webbrowser.open('google.co.uk')

    
def save_file(name,data,overwrite = False,array = False):#saving funct
    if overwrite:
        f = open(name,'r+')
    else:
        f = open(name,'w')
    if array:
        for x in data:
            f.write(x+'\n')
    else:
        for x in data:
            f.write(x)
    f.close()


def loadfile(name):##loading funct
    contents = []
    f = open(name,'r')
    for x in f.readlines():
        contents.append(x.strip('\n'))
    f.close()
    return contents

def array2csv(array):##from beelib
        temp = ''
        for fl in array:
            print(fl)
            temp += str(fl)+','
        temp+=','
        return temp
    
def csv2array(csvstr):##may need os.isfile() or whatever it is to check file is in dir before declaring eofsame for array2csv      ##from beelib
    arrayreturn = []
    temp = ''
    flag = False
    for x in csvstr:#range(len(csvnames)):
        if flag and (x==','):## ,, delimiter
            break
        if x ==',':
            arrayreturn.append(temp)
            temp = ''
            flag = True
        else:
            temp+=x
            flag = False
    return arrayreturn

def load_history_ext():##unused
    global history
    if askokcancel():
        history = loadfile(FILE_HISTORY)
        
##temp here till beelib sorted out should'nt be here
def csv2dot(strng):##replaces , with . char for  sub 'csvising them'
    temp = ''
    for x in range(len(strng)):
        if strng[x] == ',':
            temp += '.'
        else:
            temp += strng[x]
    return temp

def dot2csv(strng):##replaces . with , char for  sub 'uncsvising them'
    temp = ''
    for x in range(len(strng)):
        if strng[x] == '.':
            temp += ','
        else:
            temp += strng[x]
    return temp
##END

def load_history():
    global history
    if FILE_HISTORY in os.listdir():
        history = loadfile(FILE_HISTORY)
    else:
        save_file(FILE_HISTORY,['the history file'])

    
def save_history():
    global history
    global settings
    print(settings[2])
    if int(settings[2]) == 1:
        print('not saving to disk')
    else:
        save_file(FILE_HISTORY,history,array = True)

def refresh_Hbox():##refreshes listbox to update it
    history_Listbox.delete(0,history_Listbox.size())
    for x in history:
        history_Listbox.insert(END,x)

        
def clearhistory():##temp clears urlbox
    if messagebox.askokcancel(title = 'confirm clear',message = 'delete your history?'):
        save_file(FILE_HISTORY,['the history file'],overwrite = False)
        history_Listbox.delete(0,history_Listbox.size())
        refresh_Hbox()
        print('cleared')
    else:
        print('no')
    
def loadsettings():
    global settings
    global custom_radio
    print('loading settings...')
    if 'SETTINGS.CFF' in os.listdir():##my add as a function instead(exists checker)
        f = open('SETTINGS.CFF','r+')
        data = csv2array(f.readline())
        f.close()
        #print(data)
        settings = data
        print ('loaded: ',data)
    if 'CUSTOM.CLF' in os.listdir():
        f = open('CUSTOM.CLF','r')
        dat = f.readline()
        f.close()
        data = csv2array(dat)##to solve type prob
        print('enabled custom: '+data[4])
        if data[4] == 1 or '1':
            custom_radio.configure(state = 'normal')
            
        

def genlink():##button funct
    global settings
    if linktype_Random.get() == 1:
        linktype_Radio.set(random.randint(1,4))##randomises the link(change values to allow for all radios(UPDATE)
        ##genlink()
        
    if linktype_Radio.get() == 0:
        pass

    else:
        ##if linktype_Radio.get() == -1:
            ##linktype_Radio.set(random.randint(1,3))##randomises the link(change values to allow for all radios(UPDATE)
            ##genlink()
        if linktype_Radio.get()   ==  1:
            gennedlink.set(get_tinyurl())##eg http://tinyurl.com/DlJzJ
        elif linktype_Radio.get() ==  2:
            gennedlink.set(get_BitLy())
        elif linktype_Radio.get() ==  3:
            gennedlink.set(get_googl())
        elif linktype_Radio.get() ==  4:
            gennedlink.set(get_imgur())
        elif linktype_Radio.get() ==  5:
            gennedlink.set(get_custom())
        if int(settings[1]) == 1:##skips saving link to array and disk
            print('skipped saving history')
        else:
            history.append(gennedlink.get())
            save_history()
        linkbox_Label.config(text = str(gennedlink.get()))
        refresh_Hbox()

        
def setlink():
    global history_listbox
    if history_Listbox.curselection() == None:##checks if valid
        pass
    else:
        gennedlink.set(history_Listbox.get(history_Listbox.curselection()))
        linkbox_Label.config(text = str(gennedlink.get()))


def get_tinyurl():   
    link = ''
    leng = random.randint(4,6)#4-6 chars
    for x in range(0,leng):
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://tinyurl.com/'+link


def get_BitLy():
    link = ''
    leng = random.randint(4,6)#4-6 chars
    for x in range(0,leng):##can be longer as https://bit.ly/zzzzzzzzzzzzzzzzz is valid
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://bit.ly/'+link


def get_googl():
    link = ''
    leng = 7##7 imgur has fixed 7charsrandom.randint(4,6)#4-6 chars
    for x in range(0,leng):
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://goo.gl/'+link

##image sites
def get_imgur():
    link = ''
    leng = random.randint(4,7)#4-6 chars
    for x in range(0,leng):##can be longer as https://bit.ly/zzzzzzzzzzzzzzzzz is valid
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://i.imgur.com/'+link##+'.jpg'##check format may need detecting from file

##custom
def get_custom():##youtube thing bndPy1MHm8E
    f = open('CUSTOM.CLF','r')
    dat = f.readline()
    f.close()
    data = csv2array(dat)##to solve type prob
    print('//##//\n',data,'\n\\##\\')
    #data = csv2array(dat)
    print(data[3])
    print(dot2csv(data[3]))
    data[3] = csv2array(dot2csv(data[3]))
    print('\n\n//##//\n',data,'\n\\##\\')
    enabled = data[4]
    if enabled  == 1 or '1':
        link = ''
        leng = random.randint(int(data[2]),int(data[1]))#chars
        for x in range(0,leng):##can be longer as https://bit.ly/zzzzzzzzzzzzzzzzz is valid
            link+=data[3][random.randint(0,len(vchars))]
        return data[0]+link##+'.jpg'##check format may need detecting from file
    
def on_run():##bootup setup
    load_history()
    refresh_Hbox()
    loadsettings()

    
def on_close():##cleanup on close
    #save_history()##better to save direct
    print('cleanup')
    
    
def asciidump_ext():
	chrs = []
	for x in range(0,255):
		chrs.append(str(chr(x)))
	return chrs


#def genrandom():#save_file(name,data,overwrite = False,array = False)
#    pass ##implemented in class

##def Menu_settings_window():
##    global root
##    #global Menu_settings_window_DATA
##    Warn_Skiplink = IntVar()
##    
##    optionsmenu = Toplevel()
##    OCL = LabelFrame(optionsmenu,text = 'toggle options')##options_Checkboxes_labelframe
##    OBL = LabelFrame(optionsmenu,text = 'buttons')##options_buttons_labelframe
##    
##    SKIPWARN_check = Checkbutton(OCL,text = 'skip openbox on link open',variable = Warn_Skiplink,onvalue = 1,offvalue =0)
##    KEEPHISTORY_checks = Checkbutton(OCL,text = 'keep history',variable = Warn_Skiplink,onvalue = 1,offvalue =0)
##
##    OCL.pack()
##    OBL.pack()
##
##    SKIPWARN_check.pack()
##    KEEPHISTORY_checks.pack()
##
##    #root.config()
##    optionsmenu.title('options')
##    optionsmenu.mainloop()
##
##def Menu_settings_savesettings():
##    #global Menu_settings_window_DATA


## file objects##
class file_prog:
    filelist = os.listdir()##dont really need mainly for debug (line)
    data = []##line = one entry
    name =''
    linelen = 0
    def __init__(self):
        pass
        #self.linelen = len(self.data)
        #self.name = fname
        #self.executor()
        
    def readfile(self,fname):##internal method for filereading
        f = open(fname,'r')
        self.data = f.readlines()
        f.close()
        self.name = fname
        
    def writefile(self,fname):##internal method for filewriting
        f = open(fname,'w')
        f.write(array2csv(self.data))
        #self.data = f.readlines()
        f.close()
        #self.name = fname
    def update_fobj(self):##internal update class
        self.linelen = len(self.data)
        
    def readup(self,filename):
        self.readfile(filename)
        self.update_fobj()
        
    def get_name(self):
        return self.name
    
    def get_linelen(self):
        return self.linelen
    
    def get_data(self):
        return self.data
    
    def get_dataline(self,lineno):
        '''first line is zero '''
        return self.data[lineno]
    ##temp here till beelib sorted out should'nt be here
    def csv2dot(self,strng):##replaces , with . char for  sub 'csvising them'
        temp = ''
        for x in range(len(strng)):
            if strng[x] == ',':
                temp += '.'
            else:
                temp += strng[x]
        return temp

    def dot2csv(self,strng):##replaces . with , char for  sub 'uncsvising them'
        temp = ''
        for x in range(len(strng)):
            if strng[x] == '.':
                temp += ','
            else:
                temp += strng[x]
        return temp
    
class configfile_prog (file_prog):
    def __init__(self):
        self.readup('SETTINGS.CFF')##settings.configfilecustomlinkfile

class customfile_prog (file_prog):
    def __init__(self):
        self.readup('CUSTOM.CLF')##custom.customlinkfile
    def save_customdata(self,dat):
        #self.data = array2csv(dat)
        self.data = dat##csv done in filewriting itself
        print(self.data)
        self.writefile('CUSTOM.CLF')
    def save_customdata2(self,dat):##improvement of the first iteration assumes raw input
        #self.data = array2csv(dat)
        self.data = dat##csv done in filewriting itself(will move at some point)
        self.data[3] = csv2dot(self.data[3])#dotting subcsv
        print(self.data)
        self.writefile('CUSTOM.CLF')
    
        
##class file_reader(file_prog):
##    def readfile(self,fname):
##        if fname == '-1':
##            pass
##        else:
##            f = open(fname,'r')
##            self.data = f.readlines()
##            f.close()
##    
##class conf_file(file_prog):
##    #def executor(self):
        
###subwindow classes#
class Menu_settings_window:
    Warn_Skiplink = IntVar()##settings[0]
    History_Track = IntVar()##settings[1]
    Session_History = IntVar()##settings[2]
    SETTINGS_filename = 'SETTINGS.CFF'
    
    def __init__(self):

        self.Menu_settings_loadsettings()
        
        optionsmenu = Toplevel()
        OCL = LabelFrame(optionsmenu,text = 'toggle options')##options_Checkboxes_labelframe
        OBL = LabelFrame(optionsmenu,text = 'buttons')##options_buttons_labelframe
        
        SKIPWARN_check = Checkbutton(OCL,text = 'skip openbox on link open',variable = self.Warn_Skiplink,onvalue = 1,offvalue =0)
        KEEPHISTORY_checks = Checkbutton(OCL,text = "DON'T keep history",variable = self.History_Track,onvalue = 1,offvalue =0)
        SESSIONHISTORY_checks = Checkbutton(OCL,text = "dont save session to disk",variable = self.Session_History,onvalue = 1,offvalue =0)

        SAVESETTINGS_button = Button(OBL,text = 'Save settings',command = self.Menu_settings_savesettings)##'may be able to put into eventloop a check for the changes
        WIPESETTINGS_button = Button(OBL,text = 'clear settings',command = self.Menu_settings_wipesettings)

        OCL.pack()
        OBL.pack()

        SKIPWARN_check.pack()
        KEEPHISTORY_checks.pack()
        SESSIONHISTORY_checks.pack()

        SAVESETTINGS_button.pack()
        WIPESETTINGS_button.pack()
        
        #root.config()
        optionsmenu.title('options')
        optionsmenu.mainloop()
        
    def Menu_settings_loadsettings(self):
        if 'SETTINGS.CFF' in os.listdir():
            f  = open(self.SETTINGS_filename,'r+')
            data = self.csv2array(f.readline())
            print(data)
            f.close()
            self.Warn_Skiplink.set(data[0])
            self.History_Track.set(data[1])
            self.Session_History.set(data[2])
            #print(data)

        else:
            print('file not found!')
            
        
    def Menu_settings_savesettings(self):##saves settings to SETTINGS.CFF
        #def save_file(name,data,overwrite = False,array = False):#saving funct
        data = self.array2csv(self.Menu_settings_getsettings())

        f = open(self.SETTINGS_filename,'w')
        f.write(data)
        #for x in data:
            #f.write(x+'\n')
        f.close()
        self.Menu_settings_loadsettings()#reload settings to memory to update
        
    def Menu_settings_getsettings(self):##return settings data
        returner = [
        self.Warn_Skiplink.get(),
        self.History_Track.get(),
        self.Session_History.get()
        ]
        print(returner)
        return returner ##returning print(returner) may also work dunno tho
    
    def Menu_settings_wipesettings(self):
    #def save_file(name,data,overwrite = False,array = False):#saving funct
        data = self.array2csv(([0]*len(settings)))

        f = open(self.SETTINGS_filename,'w')
        f.write(data)
        #for x in data:
            #f.write(x+'\n')
        f.close()
        self.Menu_settings_loadsettings()#reload settings to memory

    ###these really shouldnt be here..
    def array2csv(self,array):##from beelib
        temp = ''
        for fl in array:
            print(fl)
            temp += str(fl)+','
        temp+=','
        return temp
    
    def csv2array(self,csvstr):##may need os.isfile() or whatever it is to check file is in dir before declaring eofsame for array2csv      ##from beelib
        arrayreturn = []
        temp = ''
        flag = False
        for x in csvstr:#range(len(csvnames)):
            if flag and (x==','):## ,, delimiter
                break
            if x ==',':
                arrayreturn.append(temp)
                temp = ''
                flag = True
            else:
                temp+=x
                flag = False
        return arrayreturn
    ###

    
class Menu_preview_window:
    PREVIEW_linkname = StringVar()
    def __init__(self):
        previewmenu = Toplevel()
        PVF = LabelFrame(previewmenu,text = 'toggle options')##Preview Label Frame

        t = Checkbutton(PVF,text = 'placeholder',onvalue = 1,offvalue =0)

        
        PVF.pack()

        t.pack()
        #root.config()
        previewmenu.title('preview')
        previewmenu.mainloop()
        
class Menu_customchoose_window:
    Custom_linkprefix = StringVar()
    Custom_linklen = StringVar()#IntVar()##length of link
    Custom_linkstart = StringVar()#IntVar()##inclusive position start of rng link so linklen = 6 linkstart = 4 so random.rng(4,6)
    Custom_charset = StringVar()##csv input string for custom chars
    Custom_enable = IntVar()
    
    cls = customfile_prog()##customlinkstorage ##data for the custom link

    ##defs
    Custom_charset.set('0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,,')
    EVENTLOOP_TIC = 700
    ##END
    
    #hacky globals
    customlinkmenu = ''##menu hacky global tkstuff
    LLF= '' #hacky global ##could assign locally on init within so self llf becomes llfsub/something
    #prefixcustom_entry=''
    #lowerlimitrng_entry = ''
    #upperlimitrng_entry = ''
    #charset_entry = ''
    #END
    
    def __init__(self):
        self.loadcustomlink_settings()
        self.customlinkmenu = Toplevel()
        CLF = LabelFrame(self.customlinkmenu,text = 'custom link')##Custom Label Frame
        self.LLF = LabelFrame(self.customlinkmenu,text = 'cutom link creation')##Link Label Frame

        EnableCL_button = Checkbutton(CLF,text = 'enable custom link',variable = self.Custom_enable,onvalue = 1,offvalue =0)##EnableCustomLink_button
        savesettings_button = Button(CLF,text = 'save settings',command = self.savecustomlink_settings)

        prefixcustom_entry = Entry(self.LLF,textvariable = self.Custom_linkprefix)
        prefixcustom_entry_label = Label(self.LLF,text = 'link prefix')
        lowerlimiting_entry = Entry(self.LLF,textvariable = self.Custom_linkstart)
        lowerlimiting_entry_label = Label(self.LLF,text = 'lower range rng')
        upperlimiting_entry = Entry(self.LLF,textvariable = self.Custom_linklen)
        upperlimiting_entry_label = Label(self.LLF,text = 'upper range rng')
        charset_entry = Entry(self.LLF,textvariable = self.Custom_charset)
        charset_entry_label = Label(self.LLF,text = 'rng charset(CSV)')##print(array2csv(vchars))
        #savesettings_button = Button(self.LLF,text = 'save settings',command = savecustomlink_settings)


        ##setting up
        #self.Custom_charset.set('0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,,')
        ##END
        CLF.pack()
        self.LLF.pack()

        EnableCL_button.pack()
        savesettings_button.pack()
        
        prefixcustom_entry_label.pack()
        prefixcustom_entry.pack()
        lowerlimiting_entry_label.pack()
        lowerlimiting_entry.pack()
        upperlimiting_entry_label.pack()
        upperlimiting_entry.pack()
        charset_entry_label.pack()
        charset_entry.pack()

        
        #root.config()
        self.customlinkmenu.title('custom link creation')
        self.customlinkmenu.after(self.EVENTLOOP_TIC, self.event_TED)

        self.disable_custom()##disable at start
        #self.checkstate_custom()
        self.loadcustomlink_settings()
        self.customlinkmenu.mainloop()
        
    def event_TED(self):##custom event loop
        ##event code here##
        
        #print('test')
        ##hacky stuffWILLFIX LATER

##        print(self.prefixcustom_entry.get(),
##        self.lowerlimitrng_entry.get(),
##        self.upperlimitrng_entry.get(),
##        self.charset_entry.get())
##        
##        self.Custom_linkprefix.set(self.prefixcustom_entry.get())
##        self.Custom_linklen.set(self.lowerlimitrng_entry.get())##length of link
##        self.Custom_linkstart.set(self.upperlimitrng_entry.get())##inclusive position start of rng link so linklen = 6 linkstart = 4 so random.rng(4,6)
##        self.Custom_charset.set(self.charset_entry.get())##csv input string for custom chars
        print(self.Custom_enable.get())
        if self.Custom_enable.get() == 1:
            self.enable_custom()
        else:
            self.disable_custom()
        ##END EVENT CODE##
        self.customlinkmenu.after(self.EVENTLOOP_TIC, self.event_TED)
        
    def enable_custom(self):
        print('enabled!')
        for child in self.LLF.winfo_children():
            child.configure(state='normal')
    def disable_custom(self):
        print('disabled!')
        for child in self.LLF.winfo_children():
            child.configure(state='disable')
            
    def checkstate_custom(self):##checks in settings for if enabled
        ###NOTNEEDED IGNORE here  for refrence
        dat = self.csv2array(cls.get_data())
        prefix = dat[0]
        rngrangelen = dat[1]

    def csv2dot(self,strng):##replaces , with . char for  sub 'csvising them'
        temp = ''
        for x in range(len(strng)):
            if strng[x] == ',':
                temp += '.'
            else:
                temp += strng[x]
        return temp

    def dot2csv(self,strng):##replaces . with , char for  sub 'uncsvising them'
        temp = ''
        for x in range(len(strng)):
            if strng[x] == '.':
                temp += ','
            else:
                temp += strng[x]
        return temp

    def savecustomlink_settings(self):
        global custom_radio
        dat2sav = self.getsettings()
        print('~~~~####~~~~####~~~~')
        print(dat2sav)##check array handlingstuff
        print(self.csv2dot('0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,,'))
        print('~~~~####~~~~####~~~~')
        dat2sav[3] = self.csv2dot(dat2sav[3])
        self.cls.save_customdata(dat2sav)##data is csvised internally in fileclass so no csving needed here
        if str(dat2sav[4]) == '1':
            custom_radio.configure(state = 'normal')
        else:
            custom_radio.configure(state = 'disabled')
        
    def getsettings(self):
        returner = [
        self.Custom_linkprefix.get(),
        self.Custom_linklen.get(),
        self.Custom_linkstart.get(),
        self.Custom_charset.get(),
        self.Custom_enable.get()
        ]
        return returner
            
    def loadcustomlink_settings(self):
        #data = self.csv2array(self.cls.get_data())
        #print(data)

        ##manual load till fix
        f = open('CUSTOM.CLF','r')
        data = f.readline()
        f.close()
        data = csv2array(data)
        print(data)
        ##END
        
        data[3] = self.dot2csv(data[3])
        
        self.Custom_linkprefix.set(data[0])
        self.Custom_linklen.set(data[1])
        self.Custom_linkstart.set(data[2])
        self.Custom_charset.set(data[3])
        self.Custom_enable.set(data[4])
        
    ###these really shouldnt be here..
    def array2csv(self,array):##from beelib
        temp = ''
        for fl in array:
            print(fl)
            temp += str(fl)+','
        temp+=','
        return temp
    
    def csv2array(self,csvstr):##may need os.isfile() or whatever it is to check file is in dir before declaring eofsame for array2csv      ##from beelib
        arrayreturn = []
        temp = ''
        flag = False
        for x in csvstr:#range(len(csvnames)):
            if flag and (x==','):## ,, delimiter
                break
            if x ==',':
                arrayreturn.append(temp)
                temp = ''
                flag = True
            else:
                temp+=x
                flag = False
        return arrayreturn
    ###
    
##END SUBWINDOW CLASSES##

ol_LF = LabelFrame(root,text = 'open link')##openlink
s_ol_LF  = LabelFrame(root,text = 'link')##openlink subframe forlink buttons
lr_LF = LabelFrame(root,text = 'pick a link type')##linkradio
hb_LF = LabelFrame(root,text = 'link history')##historybox
ms_LF = LabelFrame(root,text = 'misc functions')##misc
historyscroller_Scrollbar = Scrollbar(hb_LF)
history_Listbox = Listbox(hb_LF,yscrollcommand = historyscroller_Scrollbar.set)
historyscroller_Scrollbar.config(command = history_Listbox.yview)

tinyurl_radio = Radiobutton(lr_LF,text = 'tinyurl',variable = linktype_Radio,value = 1)
bitly_radio = Radiobutton(lr_LF,text = 'Bit.ly',variable = linktype_Radio,value = 2)
googl_radio = Radiobutton(lr_LF,text = 'goo.gl',variable = linktype_Radio,value = 3)
imgur_radio = Radiobutton(lr_LF,text = 'imgur',variable = linktype_Radio,value = 4)
custom_radio = Radiobutton(lr_LF,text = 'custom',variable = linktype_Radio,value = 5,state='disable')
random_chkbox = Checkbutton(lr_LF,text = 'Random!',variable = linktype_Random,onvalue = 1,offvalue =0)
genlnk_Button = Button(ol_LF,command = genlink,text = 'generate\nlink')
openlnk_Button = Button(ol_LF,command = openrng,text = 'open\nlink')
opengoogle_Button = Button(ms_LF,command = googlehome,text = 'google homepage')
selectlink_Button = Button(hb_LF,command = setlink,text = 'select link')
clearhistory_Button  = Button(ms_LF,command = clearhistory,text = 'clear history')
linkbox_Label = Label(s_ol_LF)


buff = [5,5]##pixel edge buffer/offset
lr_LF.place(x = buff[0]+ 0,y = buff[1]+ 0)#.pack()              ###PACK CHANGED TO PLACE UNCONFIGGED!!!
ol_LF.place(x = buff[0]+ 75,y = buff[1]+ 250)#.pack()
hb_LF.place(x = buff[0]+ 150,y = buff[1]+ 0)#.pack()
ms_LF.place(x = buff[0]+ 0,y = buff[1]+ 175)#.pack()
s_ol_LF.place(x = buff[0]+ 115,y = buff[1]+ 315)


tinyurl_radio.pack()
bitly_radio.pack()
googl_radio.pack()
imgur_radio.pack()
custom_radio.pack()
random_chkbox.pack()
genlnk_Button.pack(side = LEFT)
openlnk_Button.pack(side = LEFT)
opengoogle_Button.pack()
selectlink_Button.pack()
clearhistory_Button.pack()
linkbox_Label.pack(side = BOTTOM)
history_Listbox.pack(side = LEFT)
historyscroller_Scrollbar.pack(side = RIGHT,fill = Y)


def event_TED():##custom event loop
    ##event code here##
    
    ##END EVENT CODE##
    root.after(700, event_TED)


Menu_main = Menu(root)
Menu_settings = Menu(Menu_main,tearoff = 0)
#Menu_settings = Menu(menubar, tearoff=0)
Menu_settings.add_command(label="options", command=Menu_settings_window)
Menu_settings.add_command(label="custom link", command=Menu_customchoose_window)
Menu_main.add_cascade(label = 'options',menu = Menu_settings)
Menu_main.add_command(label="preview", command=Menu_preview_window)
on_run()
root.config(menu=Menu_main)#title = 'Link Roulette'
root.title('Link Roulette')
root.geometry('305x300')
root.after(2000, event_TED)
root.mainloop()
on_close()

