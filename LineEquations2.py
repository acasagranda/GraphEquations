import numpy as np                 
import matplotlib.pyplot as plt    
import random


class intrograph:
    
    def __init__(self):

        #make two columns of graphs
        self.fig, (self.ax1,self.ax2) = plt.subplots(1,2,figsize=(12,12))

        #set up size of graphs
        self.axisdim = 9
        
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
        self.ax1.set_xticks([-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9])
        self.ax1.set_yticks([-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9])
        self.ax2.set_xticks([-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9])
        self.ax2.set_yticks([-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9])

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
        y1 = [-3, 1]
        self.ax1.scatter(x1, y1,c='k')
        self.ax2.scatter(1, 3,c='b')
        self.ax2.scatter(1, 0.5,c='m')
        self.ax2.scatter(1, 1,c='k')

        #set up lines putting label here used in legend
        x =np.linspace(-self.axisdim,self.axisdim)
        y = x
        self.ax1.plot(x, y,c='k',lw=1.5, label = pe)
        self.ax2.plot(x, 3*x,c='b',lw=1.5, label="y = 3x")
        self.ax2.plot(x, y,c='k',lw=1.5, label=pe)
        self.ax2.plot(x, x*.5,c='m',lw=1.5, label="y = 1/2 x")

        #set up legend
        self.ax1.legend(loc="lower right")
        self.ax2.legend(loc="lower right")

        #set up text
        self.ax1.text(-9,10.5,text1)
        self.ax2.text(-9,10.5,text2)
        self.ax2.text(-9,-11.5,text3)

        #display
        plt.show()


class taskgraph:
    
    def __init__(self,m,scale,text1,text2):
        self.m=m
        self.scale=scale
        self.text1=text1
        self.text2=text2

        #set up size of graph
        self.axisdim=self.scale*10+10

        #make to columns of graphs
        self.fig, (self.ax,self.textarea) = plt.subplots(1,2,figsize=(13,13))

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
        x =np.linspace(-self.axisdim,self.axisdim)
        y1 = x
        y2 = x*self.m
        self.ax.plot(x, y1,c='k',lw=1.5,label = pe)
        self.ax.plot(x, y2,c='r',lw=1.5,label = "y = ?")

        #set up legend
        self.ax.legend(loc="lower right")
        
        #set up text
        self.textarea.text(0,.3,self.text1 + self.text2,fontsize=12)
        plt.show()


class guessgraph:
    
    def __init__(self,m,targeteq,scale):
        self.targeteq = targeteq
        self.m=m
        self.scale=scale

        #set up size of graph
        self.axisdim=self.scale*10+10

        #make to columns of graphs
        self.fig, (self.ax,self.textarea) = plt.subplots(1,2,figsize=(13,13))

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
        x =np.linspace(-self.axisdim,self.axisdim)
        y1=x
        y2 = x*self.m
        self.ax.plot(x, y1,c='k',lw=1.5,label = pe)
        if self.answer:  
            self.ax.plot(x, y2,c='r',lw=3.5,label = self.targeteq)
        else:
            self.ax.plot(x, y2,c='r',lw=1.5,label = "y = ?")
        
        for idx in range(len(guessm)):
            self.ax.plot(x, x*guessm[idx],c=colors[idx],lw=1.5,label = guesseq[idx])

        #set up legend
        self.ax.legend(loc="lower right")
        
        #set up text
        self.textarea.text(0,.6,self.text1,fontsize=12)
        self.textarea.text(0,.4,self.text2,fontsize=12)
        plt.show()




def geteq():
    errortext=f"Equations should follow the format\n      y = ax     or    y = 1/a x\nwhere a is an integer between 2 and 8.\n"
    while True:
        userin=input("The equation of the red line could be:")
        print("\n")
        userin2="".join(userin.split())
        userin2=userin2.lower()
        if len(userin2)<2 or userin2[:2]!= "y=":
            print(errortext)
            continue
        if len(userin2)<3 or not userin2[2].isnumeric() or int(userin2[2])<1 or int(userin2[2])>8:
            print(errortext)
            continue
        if int(userin2[2])!=1:
            m=int(userin2[2])
            if len(userin2)<4 or userin2[3]!="x" or userin2[4:]!="":
                print(errortext)
                continue
            return m, userin
        else:
            if len(userin2)<4 or userin2[3]!="/":
                print(errortext)
                continue
            if len(userin2)<5 or not userin2[4].isnumeric() or int(userin2[4])<2 or int(userin2[4])>8:
                print(errortext)
                continue
            m=1/int(userin2[4])
            if len(userin2)<6 or userin2[5]!="x" or userin2[6:]!="":
                print(errortext)
                continue
            return m, userin

       
    

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
colors=['darkviolet','blue','deepskyblue','lime','yellow','orange']

#set up parent equation and texts for intrograph
pe="y = x"
text1="This is a graph of "+ pe + ".\n\nAll of the points on this line\nhave the same x-coordinate and y-coordinate;\
                 \nfor example, (1,1) and (-3,-3)."
text2="If we tilt the line about the origin,\nthe x- and y-coordinates of the points are no longer the same.\
                 \n\nThis means that the equation of the new line cannot be "+ pe +"."
text3="The equation changes by multiplying x by a number.\
                 \n\nClose this graph window when you are ready to move on."

g1=intrograph()
g1.show()


#choose b of first and second target lines
list1 = [2,3,4, 5, 6,7,8]
m1=random.choice(list1)
m2=random.choice(list1)

mlist=[1/m2,m1]
targeteq1="y = "+str(m1)+"x"
targeteq2="y = 1/"+str(m2)+"x"

targeteqlist=[targeteq2,targeteq1]

#set up texts for taskgraph
text1="The "+ r"$\bf{"+ 'black' +"}$" + f" line graphed to the left is the \'parent\' function " + pe +"."
text2="\n\nYour task is to find the equation of the "+ r"$\bf{"+ 'red' +"}$" + f" line.\
                      \n\nSince there are no marks on the graph, you'll have to guess\
                      \nand then use the result to get closer and closer\
                      \nuntil you find the red line\'s equaton.\
                      \n\nThe equation used in this puzzle will either look like\
                      \ny = ax or y=1/a x where a is an integer between 2 and 8.\
                      \n\n(The equation can be y=c/a x for any c\
                       \nbut we are limiting it to 1/a x for this puzzle.)\
                      \n\n\nWhen you have your guess,\
                      \nclose the graph window and enter it into the terminal."
again=True
while again:
    #choose random scale of axes
    scale=random.random()
    if mlist:
        m=mlist.pop()
        targeteq=targeteqlist.pop()
    else:
        m=random.randint(2, 8)
        frac=random.randint(1,2)
        if frac==1:
            targeteq="y = "+str(m)+"x"
        else:
            targeteq="y = (1/"+str(m2)+")x"
            m=1/m


    #set up taskgraph
    g2=taskgraph(m,scale,text1,text2)
    g2.show()

    #set up texts for guessgraph
    text3="Use the results to make another guess."
    text4="When you have your guess,\nclose the graph window and enter your next guess in the terminal."


    #user can take up to 7 guesses - last one answer is revealed
    guessm=[]
    guesseq=[]
    for turn in range(7):
        userm,usereq=geteq()

        if userm==m:
            found=True
            text5="That is correct!! \n\nThe red line has the equation "+usereq
            text6="Close the graph window when you are ready to move on."
            g3=guessgraph(m,usereq,scale)
            g3.show(text5,text6,True)
            break
        elif turn!=6:
            guessm.append(userm)
            guesseq.append(usereq)
            g3=guessgraph(m,targeteq,scale)
            g3.show(text3,text4,False)
        else:
            text7="The red line has the equation "+targeteq
            text8="Close the graph window when you are ready to move on."
            g3=guessgraph(m,targeteq,scale)
            g3.show(text7,text8,True)
    again=getagain()

