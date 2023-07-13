import numpy as np                 
import matplotlib.pyplot as plt    
import random


class intrograph:
    
    def __init__(self):

        #make two columns of graphs
        self.fig, (self.ax1,self.ax2) = plt.subplots(1,2,figsize=(14,14))

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

        #set up lines putting label here used in legend
        x =np.linspace(-self.axisdim,self.axisdim)
        y = x
        self.ax1.plot(x, y,c='k',lw=1.5, label = pe)
        
        self.ax2.plot(x, y,c='k',lw=1.5, label=pe)
        self.ax2.plot(x, -3*x-4,c='red',lw=1.5, label="y = -3x-4")
        

        #set up legend
        self.ax1.legend(loc="lower right")
        self.ax2.legend(loc="lower right")

        #set up text
        self.ax1.text(-9,11,text1)
        self.ax2.text(-9,10.5,text2)
        self.ax2.text(-9,-11.5,text3)

        #display
        plt.show()


class taskgraph:
    
    def __init__(self,m,b,scale,text1,text2):
        self.m=m
        self.b=b
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
        y2 = x*self.m+self.b
        self.ax.plot(x, y1,c='k',lw=1.5,label = pe)
        self.ax.plot(x, y2,c='r',lw=1.5,label = "y = ?")

        #set up legend
        self.ax.legend(loc="lower right")
        
        #set up text
        self.textarea.text(0,.3,self.text1 + self.text2,fontsize=12)
        plt.show()


class guessgraph:
    
    def __init__(self,m,b,targeteq,scale):
        self.targeteq = targeteq
        self.m=m
        self.b=b
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
        y2 = x*self.m+self.b
        self.ax.plot(x, y1,c='k',lw=1.5,label = pe)
        if self.answer:  
            self.ax.plot(x, y2,c='r',lw=3.5,label = self.targeteq)
        else:
            self.ax.plot(x, y2,c='r',lw=1.5,label = "y = ?")
        
        for idx in range(len(guessm)):
            self.ax.plot(x, x*guessm[idx]+guessb[idx],c=colors[idx],lw=1.5,label = guesseq[idx])

        #set up legend
        self.ax.legend(loc="lower right")
        
        #set up text
        self.textarea.text(0,.6,self.text1,fontsize=12)
        self.textarea.text(0,.4,self.text2,fontsize=12)
        plt.show()



def geteq():
    errortext=f"Equations should follow the format\n      y = ax + b  or  y = 1/a x  or   y = -ax + b  or  y = -1/a x + b\nwhere a is an integer between 2 and 8 and b is an integer between -8 and 8.\n"
    while True:
        userin=input("The equation of the red line could be:")
        print("\n")
        #take out spaces and make all lowercase
        userin2="".join(userin.split())
        userin2=userin2.lower()
        #eq should start with y=
        if len(userin2)<2 or userin2[:2]!= "y=":
            print(errortext)
            continue
        #check for negative or positive slope
        if len(userin2)>2 and userin2[2]=='-':
            sign1=-1
            idx=3
        elif len(userin2)>2:
            sign1=1
            idx=2
        else:
            print(errortext)
            continue
        #slope is fraction
        if len(userin2)>idx and userin2[idx]=="1":
            idx+=1
            if len(userin2)<idx+1 or userin2[idx]!="/":
                print(errortext)
                continue
            idx+=1
            if len(userin2)<idx+1 or not userin2[idx].isnumeric() or int(userin2[idx])<2 or int(userin2[idx])>8:
                print(errortext)
                continue
            m=sign1/int(userin2[idx])
            idx+=1
            if len(userin2)<idx+1 or userin2[idx]!="x":
                print(errortext)
                continue
            idx+=1
        #slope is whole num
        elif len(userin2)>idx and userin2[idx].isnumeric() and int(userin2[idx])>=2 and int(userin2[idx])<=8:
            m=sign1*int(userin2[idx])
            idx+=1
            if len(userin2)<idx+1 or userin2[idx]!="x":
                print(errortext)
                continue
            idx+=1
        elif len(userin2)>idx and userin2[idx]=='x':
            m=sign1
            idx+=1
        else:
            print(errortext)
            continue
        if len(userin2)==idx:
            return m,0,userin
        #b is positive
        elif len(userin2)>idx and userin2[idx]=='+':
            idx+=1
            sign2=1
        #b is negative
        if len(userin2)>idx and userin2[idx]=='-':
            sign2=-1
            idx+=1
        if len(userin2)>idx and userin2[idx].isnumeric() and int(userin2[idx])>=0 and int(userin2[idx])<=8:
            b=sign2*int(userin2[idx])
            idx+=1
            if len(userin2)==idx:
                return m,b,userin
        print(errortext)
        continue
            


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
colors=['violet','darkviolet','blue','deepskyblue','aquamarine','green','chartreuse','yellow','darkorange','orangered']

#set up parent equation and texts for intrograph
pe="y = x"

text1="This is a graph of "+ pe + "."
    
text2="In this puzzle, the line "+ pe + " will be BOTH moved and tilted."
                
text3="Close this graph window when you are ready to move on."

g1=intrograph()
g1.show()


#choose b and m of first target lines
list1 = [2,3,4,5,6,7,8]
b=random.choice(list1)
blist=[b]
list1.remove(b)
mv=random.choice(list1)
mlist=[1/mv]


targeteq1="y = 1/"+str(mv)+" x + " + str(b)



#set up texts for taskgraph
text1="The "+ r"$\bf{"+ 'black' +"}$" + f" line graphed to the left is the \'parent\' function " + pe +"."
text2="\n\nYour task is to find the equation of the "+ r"$\bf{"+ 'red' +"}$" + f" line.\
                      \n\nSince there are no marks on the graph, you'll have to guess\
                      \nand then use the result to get closer and closer\
                      \nuntil you find the red line\'s equaton.\
                      \n\nThe equation used in this puzzle will either look like\
                      \ny = ax + b  or  y = 1/a x + b  or   y = -ax + b  or  y = -1/a x + b\
                      \nwhere a is an integer between 2 and 8 \
                      \nand b is an integer between -8 and 8.\
                      \n\n\nWhen you have your guess,\
                      \nclose the graph window and enter it into the terminal."
again=True
while again:
    #choose random scale of axes
    scale=random.random()
    if mlist:
        m=mlist.pop()
        b=blist.pop()
        targeteq=targeteq1
    else:
        m=random.randint(2, 8)
        b=random.randint(1,8)
        sign1=random.choice([-1,1])
        sign2=random.choice([-1,1])
        frac=random.choice([0,1])
        print(frac)

        if frac==1 and sign2==-1:   
            targeteq="y = "+str(sign1)+"/"+str(m)+" x - " +str(b)  
            m=1/m  
        elif frac==1 and sign2==1:
            targeteq="y = "+str(sign1)+"/"+str(m)+" x + " +str(b) 
            m=1/m
        m=sign1*m
            
        if frac==0 and sign2==-1:
            targeteq="y = "+str(m)+"x - "  +str(b)
        elif frac==0 and sign2==1:
            targeteq="y = "+str(m)+"x + "  +str(b)
        b=sign2*b 
           
            


    #set up taskgraph
    g2=taskgraph(m,b,scale,text1,text2)
    g2.show()

    #set up texts for guessgraph
    text3="Use the results to make another guess."
    text4="When you have your guess,\nclose the graph window and enter your next guess in the terminal."


    #user can take up to 11 guesses - last one answer is revealed
    guessm=[]
    guessb=[]
    guesseq=[]
    for turn in range(11):
        userm,userb,usereq=geteq()

        if userm==m and userb==b:
            found=True
            text5="That is correct!! \n\nThe red line has the equation "+usereq
            text6="Close the graph window when you are ready to move on."
            g3=guessgraph(m,b,usereq,scale)
            g3.show(text5,text6,True)
            break
        elif turn!=10:
            guessm.append(userm)
            guessb.append(userb)
            guesseq.append(usereq)
            g3=guessgraph(m,b,targeteq,scale)
            g3.show(text3,text4,False)
        else:
            text7="The red line has the equation "+targeteq
            text8="Close the graph window when you are ready to move on."
            g3=guessgraph(m,b,targeteq,scale)
            g3.show(text7,text8,True)
    again=getagain()

