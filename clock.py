#make a clock use 7-segment
from tkinter import *
from time import *
root = Tk()
root.title("CLOCK")
canvas = Canvas(root, width= 500, height= 200, background="green")
canvas.pack()


#create a matrix to config number from 0 to 9
matrix = [[1,1,1,1,1,0,1],
          [0,1,1,0,0,0,0],
          [1,1,0,1,1,1,0],
          [1,1,1,1,0,1,0],
          [0,1,1,0,0,1,1],
          [1,0,1,1,0,1,1],
          [1,0,1,1,1,1,1],
          [1,1,1,0,0,0,0],
          [1,1,1,1,1,1,1],
          [1,1,1,1,0,1,1]]

#init a matrix save coord of segments
matrix_coord=[[10,10,60,20],
              [50,10,60,60],
              [50,70,60,120],
              [10,110,60,120],
              [10,70,20,110],
              [10,60,60,70],
              [10,10,20,60]]
#init variable
run = True# run clock
h=0 #hour
m=0 #minute
s=0 #second
a1=a2=a3=a4=a5=a6=None# 6 numbers to make a clock (hh:mm:ss), it has 6 positons

# create 1 of 6 positions
def add_coord(arr,pos):
    new_arr=[]
    dis = 0
    if pos == 0:
        dis == 0
    if pos == 1:
        dis=70
    if pos == 2:
        dis = 160
    if pos == 3:
        dis = 230
    if pos == 4:
        dis = 320
    if pos == 5:
        dis = 390
    for i in range(4):
        if i==0 or i==2:
            new_arr.append(arr[i]+dis)
        if i==1 or i==3:
            new_arr.append(arr[i])
            
    return new_arr

def draw_segment(arr,pos):# draw segment
    global matrix_coord
    seg = canvas.create_rectangle(add_coord(arr,pos), outline="gray", fill="gray", width=2) 
    return seg 
    
def display_segments(num, pos):# display segments as display a number by draw segments
    tmp = matrix[num]
    segments = []

    for i in range(7):
        if tmp[i] == 1:
            seg = draw_segment(matrix_coord[i],pos)
            segments.append(seg)
        canvas.update()
    
    return  segments
    
def delete_segments(segments):# delete segments as delete a number
    for i in segments:
        canvas.delete(i)
    canvas.update()

def stop():# change variable run to stop clock
    global run
    run = False
    return 


def init():# init clock with all variable equal 0
    global h,m,s,run
    global a1,a2,a3,a4,a5,a6
    h=0
    m=0
    s=0
    run = True
    
    # create colon 
    canvas.create_rectangle(145,50,155,60, outline="gray", fill="gray", width=2)
    canvas.create_rectangle(145,70,155,80, outline="gray", fill="gray", width=2)

    canvas.create_rectangle(305,50,315,60, outline="gray", fill="gray", width=2)
    canvas.create_rectangle(305,70,315,80, outline="gray", fill="gray", width=2)
    # init number in 6 positions
    a5=display_segments(int(s/10),4)#second1
    a6=display_segments(int(s%10),5)#second2
    a1=display_segments(int(h/10),0)#hour1
    a2=display_segments(int(h%10),1)#hour2
    a3=display_segments(int(m/10),2)#minute1
    a4=display_segments(int(m%10),3)#minute2
    

def run_clock():# start the clock
    global h,m,s,run
    global a1,a2,a3,a4,a5,a6
    
    while run:
        
        if s>=60:
            
            s=0
            delete_segments(a3)
            delete_segments(a4)
            m+=1
            a3=display_segments(int(m/10),2)#minute1
            a4=display_segments(int(m%10),3)#minute2
        if m>=60:
            m=0
            delete_segments(a1)
            delete_segments(a2)
            h+=1
            a1=display_segments(int(h/10),0)#hour1
            a2=display_segments(int(h%10),1)#hour2
        if h>=24:
            h=0
            delete_segments(a1)
            delete_segments(a2)
            a1=display_segments(int(h/10),0)#hour1
            a2=display_segments(int(h%10),1)#hour2
    
        delete_segments(a5)
        delete_segments(a6)
    
        a5=display_segments(int(s/10),4)
        a6=display_segments(int(s%10),5)
    
        sleep(1)
        s+=1

def reset():# reset clock to 0
    global h,m,s,run
    global a1,a2,a3,a4,a5,a6
    delete_segments(a1)
    delete_segments(a2)
    delete_segments(a3)
    delete_segments(a4)
    delete_segments(a5)
    delete_segments(a6)
    init()
    
#create 3 button start,stop and reset        
btn = Button(root, text="Start", width=4, height=1, bg='silver', command=run_clock)
btn.place(x=150,y=150)
btn = Button(root, text="Stop", width=4, height=1, bg='silver', command=stop)
btn.place(x=250,y=150)
btn = Button(root, text="Reset", width=4, height=1, bg='silver', command=reset)
btn.place(x=350,y=150)


init()    
    

root.mainloop()
