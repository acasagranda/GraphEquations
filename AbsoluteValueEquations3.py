import numpy as np                 
import matplotlib.pyplot as plt    
import random


class intrograph:
    
    def __init__(self):

        #make two columns of graphs
        self.fig, (self.ax1,self.ax2) = plt.subplots(1,2,figsize=(12,12))

        #set up size of graphs
        self.axisdim = 5
        
        #set up axes
        self.ax1.set(xlim=(-self.axisdim, self.axisdim), ylim=(-self.axisdim, self.axisdim), aspect='equal')
        self.ax2.set(xlim=(-self.axisdim, self.axisdim), ylim=(-self.axisdim, self.axisdim), aspect='equal')
        self.ax1.spines['bottom'].set_position('zero')
        self.ax1.spines['left'].set_position('zero')
        self.ax1.spines['top'].set_visible(False)
        self.ax1.spines['right'].set_visible(False)
        self.ax2.spines['bottom'].set_position('zero')
        self.ax2.spines['left'].set_position('zero')
        self.ax2.spines['top'].set_visible(False)
        self.ax2.spines['right'].set_visible(False)

        # Create 'x' and 'y' labels placed at the end of the axes
        self.ax1.set_xlabel('x', size=14, labelpad=-24, x=1.03) 
        self.ax1.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)
        self.ax2.set_xlabel('x', size=14, labelpad=-24, x=1.03)
        self.ax2.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

        #set up ticks
        self.ax1.set_xticks([-5,-4,-3,-2,-1,1,2,3,4,5])
        self.ax1.set_yticks([-5,-4,-3,-2,-1,1,2,3,4,5])
        self.ax2.set_xticks([-5,-4,-3,-2,-1,1,2,3,4,5])
        self.ax2.set_yticks([-5,-4,-3,-2,-1,1,2,3,4,5])

        #put grid behind graphs
        self.ax2.grid(True)
        self.ax1.grid(True)

        #set up arrows
        arrow_fmt = dict(markersize=4, color='black', clip_on=False)
        self.ax1.plot((1), (0), marker='>', transform=self.ax1.get_yaxis_transform(), **arrow_fmt)
        self.ax1.plot((0), (1), marker='^', transform=self.ax1.get_xaxis_transform(), **arrow_fmt)
        self.ax2.plot((1), (0), marker='>', transform=self.ax2.get_yaxis_transform(), **arrow_fmt)
        self.ax2.plot((0), (1), marker='^', transform=self.ax2.get_xaxis_transform(), **arrow_fmt)

        
    def show(self):

        # Enter x and y coordinates of points and colors
        x1 = [-3, 1]
        y1 = [3, 1]
        self.ax1.scatter(x1, y1,c='k')
        # self.ax2.scatter(1, 4,c='b')
        # self.ax2.scatter(1, 0,c='m')
        # self.ax2.scatter(1, 1,c='k')

        #set up lines putting label here used in legend
        x1 =np.linspace(-self.axisdim,0)
        x2=np.linspace(0,self.axisdim)
        y1 = abs(x1)
        y2 = abs(x2)
        x21 =np.linspace(-self.axisdim,2)
        x22=np.linspace(2,self.axisdim)
        y21 = abs(x21-2)+1
        y22 = abs(x22-2)+1
        
        self.ax1.plot(x1, y1,c='k',lw=1.5, label = pe)
        self.ax1.plot(x2, y2,c='k',lw=1.5)
        self.ax2.plot(x21, y21,c='b',lw=1.5, label="y = |x-2| + 1")
        self.ax2.plot(x1, y1,c='k',lw=1.5, label=pe)
        self.ax2.plot(x22, y22,c='b',lw=1.5)
        self.ax2.plot(x2, y2,c='k',lw=1.5,)
     

        #set up legend
        self.ax1.legend(loc="lower right")
        self.ax2.legend(loc="lower right")

        #set up text
        self.ax1.text(-5,6,text1)
        self.ax2.text(-5,6,text2)
        self.ax2.text(-5,-6,text3)

        #display
        plt.show()


class taskgraph:
    
    def __init__(self,c,d,scale,text1,text2):
        self.c=c
        self.d=d
        self.scale=scale
        self.text1=text1
        self.text2=text2

        #set up size of graph
        self.axisdim=self.scale*10+10

        #make to columns of graphs
        self.fig, (self.ax,self.textarea) = plt.subplots(1,2,figsize=(15,15))

        #set up axes
        self.ax.set(xlim=(-self.axisdim, self.axisdim), ylim=(-self.axisdim, self.axisdim), aspect='equal')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.textarea.axis('off')

        # Create 'x' and 'y' labels placed at the end of the axes
        self.ax.set_xlabel('x', size=14, labelpad=-24, x=1.03) 
        self.ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)
        
        # Hide X and Y axes label marks
        self.ax.xaxis.set_tick_params(labelbottom=False)
        self.ax.yaxis.set_tick_params(labelleft=False)

        # Hide X and Y axes tick marks
        self.ax.set_xticks([])
        self.ax.set_yticks([])
       
        #no background grid
        self.ax.grid(False)
        # set up arrows

        arrow_fmt = dict(markersize=4, color='black', clip_on=False)
        self.ax.plot((1), (0), marker='>', transform=self.ax.get_yaxis_transform(), **arrow_fmt)
        self.ax.plot((0), (1), marker='^', transform=self.ax.get_xaxis_transform(), **arrow_fmt)


        
    def show(self):
        #set up lines putting label here used in legend
        x1 =np.linspace(-self.axisdim,0)
        x2=np.linspace(0,self.axisdim)
        x21 =np.linspace(-self.axisdim,-self.c)
        x22=np.linspace(-self.c,self.axisdim)
        y1 = abs(x1)
        y2 = abs(x2)
        y3 = abs(x21+ self.c)+self.d
        y4 = abs(x22+ self.c)+self.d
        self.ax.plot(x1, y1,c='k',lw=1.5,label = pe)
        self.ax.plot(x21, y3,c='r',lw=1.5,label = "y = ?")
        self.ax.plot(x2, y2,c='k',lw=1.5)
        self.ax.plot(x22, y4,c='r',lw=1.5)

        #set up legend
        self.ax.legend(loc="lower right")
        
        #set up text
        self.textarea.text(0,.3,self.text1 + self.text2,fontsize=12)
        plt.show()


class guessgraph:
    
    def __init__(self,c,d,targeteq,scale):
        self.targeteq = targeteq
        self.c=c
        self.d=d
        self.scale=scale

        #set up size of graph
        self.axisdim=self.scale*10+10

        #make to columns of graphs
        self.fig, (self.ax,self.textarea) = plt.subplots(1,2,figsize=(15,15))

        #set up axes
        self.ax.set(xlim=(-self.axisdim, self.axisdim), ylim=(-self.axisdim, self.axisdim), aspect='equal')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.textarea.axis('off')

        # Create 'x' and 'y' labels placed at the end of the axes
        self.ax.set_xlabel('x', size=14, labelpad=-24, x=1.03) 
        self.ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)
        
        # Hide X and Y axes label marks
        self.ax.xaxis.set_tick_params(labelbottom=False)
        self.ax.yaxis.set_tick_params(labelleft=False)

        # Hide X and Y axes tick marks
        self.ax.set_xticks([])
        self.ax.set_yticks([])
       
        #no background grid
        self.ax.grid(False)

        # set up arrows
        arrow_fmt = dict(markersize=4, color='black', clip_on=False)
        self.ax.plot((1), (0), marker='>', transform=self.ax.get_yaxis_transform(), **arrow_fmt)
        self.ax.plot((0), (1), marker='^', transform=self.ax.get_xaxis_transform(), **arrow_fmt)
        
        
        
    def show(self,text1,text2,answer):
        self.text1=text1
        self.text2=text2
        self.answer=answer
        
        #set up lines putting label here used in legend
        x1 =np.linspace(-self.axisdim,0)
        x2=np.linspace(0,self.axisdim)
        x21 =np.linspace(-self.axisdim,-self.c)
        x22 =np.linspace(-self.c,self.axisdim)
        y1 = abs(x1)
        y2 = abs(x2)
        y3 = abs(x21+ self.c)+self.d
        y4 = abs(x22+ self.c)+self.d
        self.ax.plot(x1, y1,c='k',lw=1.5,label = pe)
        self.ax.plot(x2, y2,c='k',lw=1.5)
        
        if self.answer:  
            self.ax.plot(x21, y3,c='r',lw=3.5,label = self.targeteq)
            self.ax.plot(x22, y4,c='r',lw=3.5)
        else:
            self.ax.plot(x21, y3,c='r',lw=1.5,label = "y = ?")
            self.ax.plot(x22, y4,c='r',lw=1.5)
        
        for idx in range(len(guessc)):
            x31 =np.linspace(-self.axisdim,-guessc[idx])
            x32=np.linspace(-guessc[idx],self.axisdim)
            self.ax.plot(x31, abs(x31+guessc[idx])+guessd[idx],c=colors[idx],lw=1.5,label = guesseq[idx])
            self.ax.plot(x32, abs(x32+guessc[idx])+guessd[idx],c=colors[idx],lw=1.5)

        #set up legend
        self.ax.legend(loc="lower right")
        
        #set up text
        self.textarea.text(0,.6,self.text1,fontsize=12)
        self.textarea.text(0,.4,self.text2,fontsize=12)
        plt.show()



def geteq():
    errortext=f"Equations should follow the format\
        \n      y = |x + c| + d     \nwhere d is an integer between -9 and 9.\
        \n (The | key is typically on the keyboard between the Enter and Backspace keys.)\n"
    while True:
        userin=input("The equation of the red graph could be:")
        print("\n")
        userin2="".join(userin.split())
        userin2=userin2.lower()
        if len(userin2)>9 or len(userin2)<4 or userin2[:4]!= "y=|x":
            print(errortext)
            continue
        if len(userin2)<5 or (userin2[4]!="+" and userin2[4]!="-"):
            print(errortext)
            continue
        c=userin2[5]
        if not c.isnumeric():
            print(errortext)
            continue
        c=int(userin2[4:6])
        if not (-9<=c<=9):
            print(errortext)
            continue
        if userin2[6]!='|':
            print(errortext)
            continue
        if len(userin2)<9 or (userin2[7]!="+" and userin2[7]!="-"):
            print(errortext)
            continue
        d=userin2[8]
        if not d.isnumeric():
            print(errortext)
            continue
        d=int(userin2[7:9])
        if not (-9<=d<=9):
            print(errortext)
            continue

        return c,d,userin

def getagain():
    ans=input("Do you want to start a new challenge? Type y or n:")
    ans=ans.lower()
    if ans=='y':
        return True
    elif ans=='n':
        return False
    else:
         return getagain()
    
    


#set up colors of guesses
colors=['violet','darkviolet','blue','deepskyblue','green','chartreuse','yellow','orange']

#set up parent equation and texts for intrograph
pe="y = |x|"
text1="This is a graph of "+ pe + ".\n\nAll of the points on the right side of the V\nhave the same x-coordinate and y-coordinate;\
                 \nfor example, (1,1).  This is part of the line y = x.\
                  \n\nAll of the points on the left hand side\nhave a y-coordinate that is the positive of the x-coordinate;\
                   \nfor example, (-3,3).  This is part of the line y = -x."
text2="If we move it, the equation of the new graph cannot be "+ pe +".\
                \n\nThe equation changes by adding or subtracting a number from x\
                 \n     inside of the absolute value\n" + r"$\bf{"+ 'and' +"}$" +\
                " adding or subtracting a number\n     outside the absolute value."
text3="Close this graph window when you are ready to move on."


g1=intrograph()
g1.show()


#choose c of first and second target lines
list1 = [3,4,5,6,7,8,9]
c=-random.choice(list1)
list1.remove(-c)
d=random.choice(list1)
clist=[c]
dlist=[d]
targeteq="y = |x + "+str(-c) +" | + "+str(d)



#set up texts for taskgraph
text1="The "+ r"$\bf{"+ 'black' +"}$" + f" graph to the left is the \'parent\' function " + pe +"."
text2="\n\nYour task is to find the equation of the "+ r"$\bf{"+ 'red' +"}$" + f" graph.\
                      \n\nSince there are no marks on the graph, you'll have to guess\
                      \nand then use the result to get closer and closer\
                      \nuntil you find the red graph\'s equaton.\
                      \n\nAll numbers used in the equation will be integers\
                      \nbetween -9 and 9.\
                      \n\nWhen you have your guess,\
                      \nclose the graph window and enter it into the terminal."
again=True
while again:
    #choose random scale of axes
    scale=random.random()
    if clist:
        c=clist.pop()
        d=dlist.pop()
        
    else:
        c=0
        while c==0:
            c=random.randrange(-9, 9)
        d=0
        while d==0:
            d=random.randrange(-9, 9)
        if c>0 and d>0:
            targeteq="y = |x + "+str(c)+"| + "+str(d)
        elif c>0 and d<0:
            targeteq="y = |x + "+str(c)+"| - "+str(-d)
        elif c<0 and d<0:
            targeteq="y = |x - "+str(-c)+"| - "+str(-d)
        else:
            targeteq="y = |x - "+str(-c)+"| + "+str(d)

    #set up taskgraph
    g2=taskgraph(c,d,scale,text1,text2)
    g2.show()

    #set up texts for guessgraph
    text3="Use the results to make another guess."
    text4="Close the graph window and enter your next guess in the terminal."


    #user can take up to 9 guesses - last one answer is revealed
    guessc=[]
    guessd=[]
    guesseq=[]
    for turn in range(9):
        userc,userd,usereq=geteq()

        if userc==c and userd==d:
            found=True
            text5="That is correct!! \n\nThe red graph has the equation "+usereq
            text6="Close the graph window when you are ready to move on."
            g3=guessgraph(c,d,usereq,scale)
            g3.show(text5,text6,True)
            break
        elif turn!=8:
            guessc.append(userc)
            guessd.append(userd)
            guesseq.append(usereq)
            g3=guessgraph(c,d,targeteq,scale)
            g3.show(text3,text4,False)
        else:
            text7="The red graph has the equation "+targeteq
            text8="Close the graph window when you are ready to move on."
            g3=guessgraph(c,d,targeteq,scale)
            g3.show(text7,text8,True)
    again=getagain()





