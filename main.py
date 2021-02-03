from tkinter import *

window=Tk()
window.configure(background='violet')
window.title('Automatic Wiper Speed Control and Headlight Mode Control using Fuzzy Logic')
window.geometry('1000x650')

# Headlight Mode Rule

"""def headlight_rule(a,b,c):
    if a=="no_rain" and b=="drizzle" and c=="satisfactory":
        return "High Beam Mode"
    
    elif a=="no_rain" and b=="drizzle" and c=="just_acceptable":
        return "High Beam Mode"
    
    elif a=="no_rain" and b=="drizzle" and c=="unbearable":
        return "Low Beam Mode"
    
    elif a=="no_rain" and b=="raining" and c=="satisfactory":
        return "High Beam Mode"

    elif a=="no_rain" and b=="raining" and c=="just_acceptable":
        return "High Beam Mode"

    elif a=="no_rain" and b=="raining" and c=="unbearable":
        return "Low Beam Mode"

    elif a=="no_rain" and b=="heavy" and c=="satisfactory":
        return "High Beam Mode"

    elif a=="no_rain" and b=="heavy" and c=="just_acceptable":
        return "High Beam Mode"

    elif a=="no_rain" and b=="heavy" and c=="unbearable":
        return "Low Beam Mode"

    elif a=="raining" and b=="drizzle" and c=="satisfactory":
        return "High Beam Mode"

    elif a=="raining" and b=="drizzle" and c=="just_acceptable":
        return "High Beam Mode"

    elif a=="raining" and b=="drizzle" and c=="unbearable":
        return "Low Beam Mode"

    elif a=="raining" and b=="raining" and c=="satisfactory":
        return "High Beam Mode"

    elif a=="raining" and b=="raining" and c=="just_acceptable":
        return "Low Beam Mode"

    elif a=="raining" and b=="raining" and c=="unbearable":
        return "Low Beam Mode"

    elif a=="raining" and b=="heavy" and c=="satisfactory":
        return "Low Beam Mode"

    elif a=="raining" and b=="heavy" and c=="just_acceptable":
        return "Low Beam Mode"

    else:
        return "Low Beam Mode" """

# Wiper Speed Rule

"""def rainfall_rule(a,b):
    if a== "no_rain":
        return "OFF"
    
    elif b== "drizzling":
        return "LOW"
    
    elif b== "raining":
        return "LOW"
    
    else:
        return "HIGH" """

def raining_1(y,x):
    
    if x>=0 and x<=0.03:
        min_1 = min((0.5-y)/0.25 , x/0.03)  # no rain , drizzling
        min_2 = min((y-0.3)/0.27 , x/0.03)  # raining , drizzling
        if min_1>min_2:
            return "OFF"
        else:
            return "LOW"
        
    if x>=0.03 and x<=0.1:
        min_1 = min((0.5-y)/0.25 , (0.12-x)/0.09)   # no rain , drizzling
        min_2 = min((y-0.3)/0.27 , (0.12-x)/0.09)   # raining , drizzling
        if min_1>min_2:
            return "OFF"
        else:
            return "LOW"
        
    if x>=0.1 and x<=0.12:
        min_1 = min((0.5-y)/0.25 , (0.12-x)/0.09)   # no rain , drizzling
        min_2 = min((0.5-y)/0.25 , (x-0.1)/0.1)     # no rain , raining
        min_3 = min((y-0.3)/0.27 , (0.12-x)/0.09)   # raining , drizzling
        min_4 = min((y-0.3)/0.27 , (x-0.1)/0.1)     # raining , raining
        strength = max(min_1,min_2,min_3,min_4)
        if strength==min_3 or strength==min_4:
            return "LOW"
        else:
            return "OFF"
        
    if x>=0.12 and x<=0.2:
        min_1 = min((0.5-y)/0.25 , (x-0.1)/0.1)     # no rain , raining
        min_2 = min((y-0.3)/0.27 , (x-0.1)/0.1)     # raining , raining
        if min_1>min_2:
            return "OFF"
        else:
            return "LOW"
        
    if x>=0.20 and x<=0.25:
        min_1 = min((0.5-y)/0.25 , (0.3-x)/0.1)     # no rain , raining
        min_2 = min((y-0.3)/0.27 , (0.3-x)/0.1)     # raining , raining
        if min_1>min_2:
            return "OFF"
        else:
            return "LOW"
        
    if x>=0.25 and x<=0.3:
        min_1 = min((0.5-y)/0.25 , (0.3-x)/0.1)     # no rain , raining
        min_2 = min((0.5-y)/0.25 , (x-0.25)/0.75)   # no rain , heavy
        min_3 = min((y-0.3)/0.27 , (0.3-x)/0.1)     # raining , raining
        min_4 = min((y-0.3)/0.27 , (x-0.25)/0.75)   # raining , heavy
        strength = max(min_1,min_2,min_3,min_4)
        if strength == min_4:
            return "HIGH"
        elif strength == min_3:
            return "LOW"
        else:
            return "OFF"
    
    if x>=0.3 and x<=1.0:
        min_1 = min((0.5-y)/0.25 , (x-0.25)/0.75)   # no rain , heavy
        min_2 = min((y-0.3)/0.27 , (2.0-x)/1.0)     # raining , heavy
        if min_1>min_2:
            return "OFF"
        else:
            return "HIGH"
    
    if x>=1.0 and x<=2.0:
        min_1 = min((0.5-y)/0.25 , (2.0-x)/1.0)     # no rain , heavy
        min_2 = min((y-0.3)/0.27 , (2.0-x)/1.0)     # raining , heavy
        if min_1>min_2:
            return "OFF"
        else:
            return "HIGH"
    
def wiper_speed(rainfall,rain_intensity):
    
    if rainfall<0.3:
        return "OFF"
    elif rainfall>0.5:
        if rain_intensity<0.25:
            return "LOW"
        elif rain_intensity>0.30:
            return "HIGH"
        else:
            min_1 = min(rainfall,(0.3-rain_intensity)/0.1)
            min_2 = min(rainfall,(rain_intensity-0.25)/0.75)
            if min_1>min2:
                return "LOW"
            else:
                return "HIGH"
    else:
        return raining_1(rainfall,rain_intensity)

def headlight_1(x,y):
    if y>=4500:
       return "Low Beam Mode"
    elif y>=4000 and y<=4500:
       min_1 = min((0.3-x)/0.1 , (4500-y)/1500)     # raining , satisfactory
       min_2 = min((0.3-x)/0.1 , (y-4000)/2000)     # raining , just acceptable
       min_3 = min((x-0.25)/0.75 , (4500-y)/1500)   # heavy , satisfactory
       min_4 = min((x-0.25)/0.75 , (y-4000)/2000)   # heavy , just acceptable
       strength = max(min_1,min_2,min_3,min_4)
       if strength == min_1:
           return "High Beam Mode"
       else:
           return "Low Beam Mode"
    elif y>=2000 and y<=4000:
        min_1 = min((0.3-x)/0.1 , (4500-y)/1500)    # raining , satisfactory
        min_2 = min((x-0.25)/0.75 , (4500-y)/1500)  # heavy , satisfactory
        strength = max(min_1,min_2)
        if strength == min_1:
            return "High Beam Mode"
        else:
            return "Low Beam Mode"
    else:
        min_1 = min((0.3-x)/0.1 , y/2000)           # raining , satisfactory
        min_2 = min((x-0.25)/0.75 , y/2000)         # heavy , satisfactory
        strength = max(min_1,min_2)
        if strength == min_1:
            return "High Beam Mode"
        else:
            return "Low Beam Mode"

def headlight_2(x,y):
    if y>=4500:
       return "Low Beam Mode"
    elif y>=4000 and y<=4500:
       min_1 = min((0.3-x)/0.1 , (4500-y)/1500)     # raining , satisfactory
       min_2 = min((0.3-x)/0.1 , (y-4000)/2000)     # raining , just acceptable
       strength = max(min_1,min_2)
       if strength == min_1:
           return "High Beam Mode"
       else:
           return "Low Beam Mode"
    else:
        return "High Beam Mode"

def headlight_3(x,y):
    if y>=4500:
       return "Low Beam Mode"
    elif y>=4000 and y<=4500:
       min_1 = min((x-0.1)/0.1 , (4500-y)/1500)     # raining , satisfactory
       min_2 = min((x-0.1)/0.1 , (y-4000)/2000)     # raining , just acceptable
       strength = max(min_1,min_2)
       if strength == min_1:
           return "High Beam Mode"
       else:
           return "Low Beam Mode"
    else:
        return "High Beam Mode"

def headlight_4(x,y):
    if y<=4000:
        return "High Beam Mode"
    
    elif y>=4000 and y<=4500:
        min_1 = ((0.12-x)/0.09 , (4500-y)/1500)   # drizzle , satisfactory
        min_2 = ((0.12-x)/0.09 , (y-4000)/2000)   # drizzle , just acceptable
        min_3 = ((x-0.1)/0.1 , (4500-y)/1500)     # raining , satisfactory
        min_4 = ((x-0.1)/0.1 , (y-4000)/2000)     # raining , just acceptable
        strength = max(min_1,min_2,min_3,min_4)
        if strength == min_4:
            return "Low Beam Mode"
        else:
            return "High Beam Mode"
        
    elif y>=4500 and y<=6000:
        min_1 = ((0.12-x)/0.09 , (y-4000)/2000)   # drizzle , just acceptable
        min_2 = ((x-0.1)/0.1 , (y-4000)/2000)     # raining , just acceptable
        if min_1>min_2:
            return "High Beam Mode"
        else:
            return "Low Beam Mode"
        
    elif y>=6000 and y<=8000:
        min_1 = ((0.12-x)/0.09 , (8200-y)/2200)   # drizzle , just acceptable
        min_2 = ((x-0.1)/0.1 , (8200-y)/2200)     # raining , just acceptable
        if min_1>min_2:
            return "High Beam Mode"
        else:
            return "Low Beam Mode"

    elif y>=8000 and y<=8200:
        min_1 = ((0.12-x)/0.09 , (8200-y)/2200)   # drizzle , just acceptable
        min_2 = ((0.12-x)/0.09 , (y-8000)/2000)   # drizzle , unbearable
        min_3 = ((x-0.1)/0.1 , (8200-y)/2200)     # raining , just acceptable
        min_4 = ((x-0.1)/0.1 , (y-8000)/2000)     # raining , unbearable
        strength = max(min_1,min_2,min_3,min_4)
        if strength == min_1:
            "High Beam Mode"
        else:
            "Low Beam Mode"

    else:
        return "Low Beam Mode"
        

def headlight_5(x,y):
    if y<=8000:
        return "High Beam Mode"

    elif y>=8000 and y<=8200:
        min_1 = ((0.12-x)/0.09 , (8200-y)/2200)   # drizzle , just acceptable
        min_2 = ((0.12-x)/0.09 , (y-8000)/2000)   # drizzle , unbearable
        if min_1>min_2:
            return "High Beam Mode"
        else:
            return "Low Beam Mode"

    else:
        return "Low Beam Mode"

def headlight_6(x,y):
    if y<=8000:
        return "High Beam Mode"

    elif y>=8000 and y<=8200:
        min_1 = (x/0.03 , (8200-y)/2200)   # drizzle , just acceptable
        min_2 = (x/0.03 , (y-8000)/2000)   # drizzle , unbearable
        if min_1>min_2:
            return "High Beam Mode"
        else:
            return "Low Beam Mode"

    else:
        return "Low Beam Mode"

def headlight_mode(rainfall,rain_intensity,light_intensity):
    
    if wiper_speed(rainfall,rain_intensity)== "OFF":
        if light_intensity<=8100:
            return "Low Beam Mode"
        else:
            return "High Beam Mode"
        
    elif rain_intensity>=0.3:
        return "Low Beam Mode"
    
    elif rain_intensity>=0.25 and rain_intensity<=0.3:
        return headlight_1(rain_intensity,light_intensity)

    elif rain_intensity>=0.2 and rain_intensity<=0.25:
        return headlight_2(rain_intensity,light_intensity)

    elif rain_intensity>=0.12 and rain_intensity<=0.2:
        return headlight_3(rain_intensity,light_intensity)

    elif rain_intensity>=0.1 and rain_intensity<=0.12:
        return headlight_4(rain_intensity,light_intensity)

    elif rain_intensity>=0.03 and rain_intensity<=0.1:
        return headlight_5(rain_intensity,light_intensity)

    else:
        return headlight_6(rain_intensity,light_intensity)
        

def show():
    light_intensity=slider1.get()
    rainfall=slider2.get()
    rain_intensity=slider3.get()
    speed = wiper_speed(rainfall,rain_intensity)
    mode = headlight_mode(rainfall,rain_intensity,light_intensity)
    headlight.set(mode)
    wiper.set(speed)
    

label1=Label(window,text='Automatic wiper speed &\n headlight mode controller',
             font=('Book Antiqua',27,'bold','underline'), bg='light yellow',fg='red')
label1.place(x=0,y=0,relwidth=1,height=120)

msg=Label(window, text="You can change the intensity of rain and opposite vehicle light using slider to get the result",
          font=('times new roman',15,'bold'),fg='dark blue',bg='violet')
msg.place(x=0,y=130,relwidth=1)

label2 = Label(window, text = ' Headlight Mode ',font=(10),bg='violet')
label2.place(x=10,y=180)

headlight=StringVar()
entry1 = Entry(window,textvariable= headlight)
entry1.place(x=200,y=181)

label3 = Label(window, text = ' Wiper Speed ',font=(10),bg='violet')
label3.place(x=10,y=220)

wiper=StringVar()
entry1 = Entry(window,textvariable= wiper)
entry1.place(x=200,y=221)

slider1 = Scale(window, from_ =0, to=12000,resolution=500 ,tickinterval=2000, orient= HORIZONTAL,
                bg='black',fg='white',length=400, cursor='circle',)
slider1.set(3000)
slider1.place(x=20,y=280)
label3 = Label(window, text = ' Opposite Vechicle\'s Light Intensity (Lux/hour)',
               font=('forte',13), bg='violet',fg='black')
label3.place(x=50,y=347)

slider2 = Scale(window, from_ =0.0, to=5.0, resolution=0.1,tickinterval=0.5,
                orient= HORIZONTAL,fg='black',bg='white',length=400, cursor='dot',)
slider2.set(1.3)
slider2.place(x=20,y=390)
label4 = Label(window, text = ' Rainfall (mm)',font=('forte',13),
               bg='violet')
label4.place(x=145,y=457)

slider3 = Scale(window, from_ =0, to=2.0,resolution=0.01 ,tickinterval=0.2, orient= HORIZONTAL,
                bg='black',fg='white',length=400, cursor='dot',)
slider3.set(0.2)
slider3.place(x=20,y=490)
label5 = Label(window, text = ' Rainfall Intensity (inch/hour)',font=('forte',13),
               bg='violet')
label5.place(x=105,y=557)


img1=PhotoImage(file='rain.png')
img2=PhotoImage(file='rainfall.png')
img3=PhotoImage(file='light.png')
img1=img1.subsample(3)
img2=img2.subsample(3)
img3=img3.subsample(3)
label2=Label(window,image=img1)
label2.place(x=600,y=170)
label3=Label(window,image=img2)
label3.place(x=600,y=330)
label4=Label(window,image=img3)
label4.place(x=600,y=492)

button1= Button(window,text='Show',font=('arial',11,'bold'),bg='blue',fg='white',bd=5, command=show)
button1.place(x=170,y=600,height=40,width=80)
