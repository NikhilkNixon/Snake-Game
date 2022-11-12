#IMPORTING NECESSARY MODULES

from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
import turtle
import mysql.connector
import random
import time
import datetime
from playsound import playsound
import winsound
 




#MYSQL DATABASE
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="tomnik")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists NN_SNAKEGAME")
mycursor.close()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tomnik",
  database="NN_SNAKEGAME")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists SNAKE (PCODE INT PRIMARY KEY "
                 "AUTO_INCREMENT, NAME VARCHAR(30), DATE VARCHAR(30),"
                 " SCORE INT)")
if mydb.is_connected():
    print('Successfully Connected')
else:
    print('Failed')
    




#CREATING THE MAIN WINDOW
cp=Tk()                                                                     
cp.title("Snake Game")
cp.iconbitmap(r'logo.ico')
cp.configure(bg='#5a824f')                                                  
cp.resizable(False, False)                                                  

#Centering the window
window_height = 600                                                        
window_width = 800                                                          
screen_width = cp.winfo_screenwidth()                                      
screen_height = cp.winfo_screenheight()                                     
x_cor= int((screen_width/2) - (window_width/2))                              
y_cor= int((screen_height/2) - (window_height/2))                           
cp.geometry("{}x{}+{}+{}".format(window_width,window_height, x_cor, y_cor))
#Centering_end

#Creating canvas on tk window where we place the widgets
canvas=Canvas(cp,width=800,height=600, bg='#5a824f')
canvas.pack()                                                               
canvas.create_rectangle(25,25,775,575, outline = "white", width=5)
canvas.create_line(200,370,600,370,dash=(4,2),fill='#456b3b', width=5)

label=Label(canvas, text="SNAKE GAME",
            font=('Shinji blues',55,'normal'),
            fg='white', bg='#5a824f')
label.place(x=160,y=75)


#EXECUTING SQL STATEMENT TO GET THE HIGHEST SCORE FROM THE DATABASE
mycursor.execute("SELECT MAX(SCORE) FROM SNAKE")
hsc=mycursor.fetchall()
if hsc[0][0] == None:
    high_score = 0
else:
    high_score = hsc[0][0]


    
#CREATING THE WRITEUPS ON MAIN WINDOW LIKE CURRENT HIGHSCORE AND CONTROLS
lbl=Label(cp, text="Current High Score  :  {}".format(high_score),
          font=('bradley hand itc',13,'bold'),fg='white', bg='#5a824f')
lbl.place(x=290,y=405)

lbl1=Label(cp, text='Move Up\n    Move Down\n    Move Right\n Move Left',
           font=('bradley hand itc',13,'bold'),fg='white', bg='#5a824f')
lbl1.place(x=250,y=445)

lbl2=Label(cp, text=':\n:\n:\n:',
           font=('bradley hand itc',13,'bold'),fg='white', bg='#5a824f')
lbl2.place(x=380,y=445)

lbl3=Label(cp, text='   Up Arrow/ W\nDown Arrow/ S\nRight Arrow/ D\n'
           '  Left Arrow/ A', anchor='w', padx=0,
           font=('bradley hand itc',13,'bold'),fg='white', bg='#5a824f')
lbl3.place(x=400,y=445)





#DEFINING THE NECESSARY FUNCTIONS 


def inst():      #FUNCTION TO BE CALLED WHEN INSTRUCTIONS BUTTON IS CLICKED
    winsound.PlaySound(r'Button.wav', winsound.SND_ASYNC)
    messagebox.showinfo('Instructions',"One Red food       = 10 Points\n"
                        "One Yellow food   = 50 Points\n\nEach time the "
                        "snake eats a Yellow or Red food, length of snake "
                        "increases by 1 dot and if it is a red food, speed"
                        " of\nthe snake increases. Yellow food is a bonus "
                        "that appears randomly and disappears after 5 "
                        "seconds. The game ends when the snake moves into "
                        "itself.\n\nPress X to quit in between the game."
                        "\nPress R to restart the game.")


def NAME():       #FUNCTION TO BE CALLED WHEN PLAY BUTTON IS CLICKED
    winsound.PlaySound(r'Button.wav', winsound.SND_ASYNC)
    cp.withdraw()
    cp08=Tk()
    cp08.iconbitmap(r'logo.ico')
    cp08.title("Name")
    cp08.configure(bg='#5a824f')
    cp08.resizable(False, False)


    #Centering the window
    window_height = 200
    window_width = 400

    screen_width = cp08.winfo_screenwidth()
    screen_height = cp08.winfo_screenheight()
    x_cor= int((screen_width/2) - (window_width/2))
    y_cor= int((screen_height/2) - (window_height/2))
    cp08.geometry(
        "{}x{}+{}+{}".format(window_width, window_height, x_cor, y_cor))
    #centering_end
    

    canvas08=Canvas(cp08,width=400,height=250, bg='#5a824f')
    canvas08.pack()


    def play(): #WHEN THE PLAY BUTTON OF 'YOUR NAME' WINDOW IS CLICKED

        winsound.PlaySound(r'Button.wav', winsound.SND_ASYNC)

        global running
        running = True

        try:
            cp08.destroy()
        except:
            pass

        x = datetime.datetime.now()
        d = x.strftime("%d %b %Y %I:%M %p")
        c = random.randint(1000,1999)
        n = namevar.get()
        if n == '':
            pname = 'Unknown'
        else:
            pname = n

        delay=0.15

        score=0

        if hsc[0][0] == None:
            high_score = 0
        else:
            high_score = hsc[0][0]

    
        t=1
        yelfood = 0
        redfood = 0
        

        root=turtle.Screen()
        root.title('Snake Game')
        root.bgcolor('#5a824f')
        root.setup(width=800, height=600)
        root.tracer(0)
        root.cv._rootwindow.resizable(False, False)
    
        head=turtle.Turtle()          #Creating Snake's head
        head.speed(0)
        head.shape('circle')
        head.color("white")
        head.penup()
        head.goto(0,0)
        head.direction="stop"
    
        food=turtle.Turtle()          #Creating red food
        food.speed(0)
        food.shape('circle')
        food.color('red')
        food.penup()
        food.goto(0,100)
    
        food_2x=turtle.Turtle()       #Creating yellow food
        food_2x.speed(0)
        food_2x.shape('square')
        food_2x.color('yellow')
        food_2x.penup()
        food_2x.goto(1000,1000)

        segments = []                  #List containing each element of
                                       #snake's body
    
        sc=turtle.Turtle()
        sc.speed(0)
        sc.shape('square')
        sc.color('white')
        sc.penup()
        sc.hideturtle()
        sc.goto(0,245)
        sc.write('Your Score: 0                      High Score: {}'
                 .format(high_score),
                 align='center',
                 font=('lethal injector regular',20,'bold'))
        
        sc3=turtle.Turtle()
        sc3.speed(0)
        sc3.shape('square')
        sc3.color('white')
        sc3.penup()
        sc3.hideturtle()
        sc3.goto(280,-285)
        sc3.write('Enter X to QUIT', align='center',
                  font=('courier new',12,'normal'))
    
        sc4=turtle.Turtle()
        sc4.speed(0)
        sc4.shape('square')
        sc4.color('white')
        sc4.penup()
        sc4.hideturtle()
        sc4.goto(-270,-285)
        sc4.write('Enter R to RESTART', align='center',
                  font=('courier new',12,'normal'))
  


        def go_up():                    #WHEN UP ARROW OR W IS PRESSED
            if head.direction != 'down':
                head.direction='up'

        def go_down():                  #WHEN DOWN ARROW OR S IS PRESSED
            if head.direction != 'up':
                head.direction='down'

        def go_left():                  #WHEN LEFT ARROW OR A IS PRESSED
            if head.direction != 'right':
                head.direction='left'

        def go_right():                 #WHEN RIGHT ARROW OR D IS PRESSED
            if head.direction != 'left':
                head.direction='right'



        def move():
            if head.direction == 'up':
                y = head.ycor()
                head.sety(y+20)
            if head.direction == 'down':
                y = head.ycor()
                head.sety(y-20)
            if head.direction == 'left':
                x = head.xcor()
                head.setx(x-20)
            if head.direction == 'right':
                x = head.xcor()
                head.setx(x+20)
    
        def destroy():
            global running
            running = False
            
    
        def restart():
            m3=messagebox.askquestion('Restart','Restarting...\nDo you want'
                                      ' to change the name?')
            if m3=='yes':
                root.clear()
                NAME()
            else:
                root.clear()
                play()



        g=random.randint(5,10)

  
        #BINDING THE KEYS TO RESPECTIVE FUNCTIONS
        root.listen()
        root.onkey(destroy, 'x')
        root.onkey(restart, 'r')
        root.onkey(go_up, 'Up')
        root.onkey(go_up, 'w')
        root.onkey(go_down, 'Down')
        root.onkey(go_down, 's')
        root.onkey(go_left, 'Left')
        root.onkey(go_left, 'a')
        root.onkey(go_right, 'Right')
        root.onkey(go_right, 'd')


        


        #MAINLOOP
        while running:
            root.update()

            #checking collision with border area
            if head.xcor()>390 or head.xcor()<-390 or head.ycor()>290 or head.ycor()<-290:
                time.sleep(0)
                x=head.xcor()
                y=head.ycor()


                if x<1000 and y<1000:
                    if head.xcor()>390:
                        head.goto(-390,y)
                        head.direction = 'right'
                    elif head.xcor()<-390:
                        head.goto(390,y)
                        head.direction = 'left'
                    elif head.ycor()>290:
                        head.goto(x,-290)
                        head.direction = 'up'
                    elif head.ycor()<-290:
                        head.goto(x,290)
                        head.direction = 'down'




            #checking collision with red food
            if head.distance(food)<20:
                playsound('red.wav',False)
                redfood += 1
                #move the red food to random place
                x=random.randint(-380,380)
                y=random.randint(-280,250)
                food.goto(x,y)
                t+=1
            
            

                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape('circle')
                new_segment.color('white')
                new_segment.penup()
                segments.append(new_segment)


                if t<40:
                    delay-= 0.003
                elif t>60:
                    pass
                else:
                    delay-= 0.001

                score+=10
            
            

                if score>int(high_score):
                    high_score=score
                
                sc.clear()
                sc.write('Your Score: {}                     '
                         'High Score: {}'.format(score, high_score),
                         align='center',
                         font=('lethal injector regular',20,'bold'))
    
                g=random.randint(2,20)


            def food_2x_del():
                food_2x.goto(-1000,-1000)


            if t%g==0:
                t+=1
                x=random.randint(-380,380)
                y=random.randint(-280,250)
                food_2x.goto(x,y)
            
                winsound.PlaySound(r'Countdown.wav', winsound.SND_ASYNC)
                                
                turtle.ontimer(food_2x_del, t=4500)



            #checking collision with yellow food
            if head.distance(food_2x)<20:
                winsound.PlaySound(r'yellow2.wav', winsound.SND_ASYNC)
                yelfood += 1
    
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape('circle')
                new_segment.color('white')
                new_segment.penup()
                segments.append(new_segment)

                delay-= 0.003

                score+=50

                food_2x.goto(-1000,-1000)

                if score>int(high_score):
                    high_score=score

                sc.clear()
                sc.write('Your Score: {}                     '
                         'High Score: {}'.format(score, high_score),
                         align='center',
                         font=('lethal injector regular',20,'bold'))
                 

        

            
            #move the segments in reverse order
            for index in range(len(segments)-1,0,-1):
                x=segments[index-1].xcor()
                y=segments[index-1].ycor()
                segments[index].goto(x,y)

            #move segment 0 to head
            if len(segments)>0:
                x=head.xcor()
                y=head.ycor()
                segments[0].goto(x,y)
            move()

            #check for collision with body
            for segment in segments:
                if segment.distance(head)<20:    
                    head.goto(1000,-1000)
                    head.clear()
                    food.goto(1000,1040)
                    food.clear()
                    sc.goto(-1000,-1000)
                    root.bgcolor('#851414')
                    time.sleep(0)

                    
                    winsound.PlaySound(r'Gameover3.wav',
                                       winsound.SND_ASYNC)


                    sc1=turtle.Turtle()
                    sc1.speed(0)
                    sc1.shape('square')
                    sc1.color('white')
                    sc1.penup()
                    sc1.hideturtle()
                    sc1.goto(0,0)
                    sc1.write('GAME OVER' , align='center',
                              font=('magmawave caps',30,'normal'))
                    

                    

                    mycursor = mydb.cursor()
                    sql = "INSERT INTO snake (name, date, score) VALUES (%s , %s, %s)"
                    val = (pname, d, score)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print(mycursor.rowcount, "record inserted.")

                

                    print('********************************************')
                    print('>>> Player : ',pname)
                    print('>>> Score : ',score)                           
                    print('>>> Number of red foods collected : ',redfood)
                    print('>>> Number of yellow foods collected :',yelfood)
                    print('********************************************')

                    time.sleep(2.5)


                    u=int(high_score)-score

                    if score<int(high_score):
                        ck=messagebox.showinfo('Score','Your Score: {}\n\n'
                                               'You are {} points away from '
                                               'the High score.'
                                               .format(score,u))
                    else:
                        ck=messagebox.showinfo('Score','Your Score: '
                                               '{}\n\nCONGRATULATIONS!!!\n'
                                               'You made a new'
                                               ' High Score'.format(score))

                
                    m=messagebox.askquestion('Play Again?',
                                             'Do you want to play again?')
                    if m=='yes':
                        root.clear()
                        NAME()
                    else:
                        root.bye()
                        cp.deiconify()

            time.sleep(delay)
        else:
            mydb.close()
            root.bye()
            cp.destroy()


    def cancel():
        winsound.PlaySound(r'Button.wav', winsound.SND_ASYNC)
        cp08.destroy()
        cp.deiconify()

    cp08.protocol("WM_DELETE_WINDOW", cancel)

    namevar=StringVar(cp08)

    entry08 = Entry(cp08, textvariable=namevar, bd=0, bg= 'white',
                    fg='black', width=40)
    canvas08.create_window(200,105,window=entry08)

    lb08 = Label(cp08, text="Your Name",
                 font=('lethal injector regular',20,'bold'),
                 fg='white', bg='#5a824f')
    canvas08.create_window(200,53,window=lb08)

    btn081 = Button(cp08, text='>>>', command= play, bd = 0,
                    bg='#5a824f',fg='white',
                    font=('lethal injector regular',14,'bold'),width=8,
                    activebackground = '#456b3b', activeforeground='white')
    canvas08.create_window(290,160,window=btn081)
    btn082 = Button(cp08, text='<<<', command= cancel, bd = 0,
                    bg='#5a824f',fg='white',
                    font=('lethal injector regular',14,'bold'),width=8,
                    activebackground = '#456b3b', activeforeground='white')
    canvas08.create_window(110,160,window=btn082)
    


def history():
    winsound.PlaySound(r'Button.wav', winsound.SND_ASYNC)
    cp.withdraw()

    ld = Tk()
    ld.iconbitmap(r'logo.ico')
    ld.title('Play History')
    ld.geometry('400x300')
    ld['bg']='white'
    ld.resizable(False, False)
    scrollbar = Scrollbar(ld)
    scrollbar.pack( side = RIGHT, fill = Y )

    #Centering_begin
    window_height = 270
    window_width = 380
    screen_width = ld.winfo_screenwidth()
    screen_height = ld.winfo_screenheight()
    x_cor= int((screen_width/2) - (window_width/2))
    y_cor= int((screen_height/2) - (window_height/2))
    ld.geometry("{}x{}+{}+{}".format(window_width, window_height,
                                     x_cor, y_cor))
    #centering_end


    style = ttk.Style(ld)
    style.theme_use('default')
    style.configure('Treeview',
                    background='#9cc991',
                    foreground='black',
                    rowheight=25,
                    fieldbackground='#9cc991')
    style.configure('Treeview.Heading',
                    background='#629656',
                    foreground='black')

                    
    style.map('Treeview',
              background=[('selected','#7aa86f')])
    
    tv = ttk.Treeview(ld, yscrollcommand = scrollbar.set)
    tv.pack()

    scrollbar.config( command = tv.yview )

    tv['columns'] = ('1', '2', '3', '4')
    tv['show'] = 'headings'
    tv.column('1', anchor=CENTER, width=50)
    tv.column('2', anchor=CENTER, width=80)
    tv.column('3', anchor=CENTER, width=165)
    tv.column('4', anchor=CENTER, width=62)
    tv.heading('1', text='---')
    tv.heading('2', text='NAME')
    tv.heading('3', text='TIMESTAMP')
    tv.heading('4', text='SCORE')

    mycursor.execute("SELECT * FROM SNAKE")
    res = mycursor.fetchall()

    for i in res:
        tv.insert('', '0', iid=i[0], text='',
                  values=(i[0],i[1],i[2],i[3]))

    def cl():
        winsound.PlaySound(r'Button.wav', winsound.SND_ASYNC)
        ld.destroy()
        cp.deiconify()

    canvasld=Canvas(ld,width=400,height=200, bg='white')
    canvasld.pack()    

    ld.protocol("WM_DELETE_WINDOW", cl)



def quit():
    winsound.PlaySound(r'Button.wav', winsound.SND_ASYNC)
    mydb.close()
    cp.destroy()



btn1=Button(text='PLAY', command= NAME, bd=0, bg='#5a824f',fg='white',
            font=('lethal injector regular',15,'bold'),width=14,
            activebackground = '#456b3b', activeforeground='white')
canvas.create_window(400,215,window=btn1)
btn4=Button(text='INSTRUCTIONS', command= inst, bd=0, bg='#5a824f',
            fg='white', font=('lethal injector regular',15,'bold')
            ,width=14,activebackground = '#456b3b',
            activeforeground='white')
canvas.create_window(400,250,window=btn4)
btn2=Button(text='HISTORY', command= history, bd=0, bg='#5a824f',
            fg='white',font=('lethal injector regular',15,'bold'),
            width=14,activebackground = '#456b3b',
            activeforeground='white')
canvas.create_window(400,285,window=btn2)
btn3=Button(text='QUIT', command= quit, bd=0, bg='#5a824f',fg='white',
            font=('lethal injector regular',15,'bold'),width=14,
            activebackground = '#456b3b', activeforeground='white')
canvas.create_window(400,320,window=btn3)



cp.mainloop()


