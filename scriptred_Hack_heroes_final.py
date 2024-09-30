from random import randint 
import numpy as np

name = 'aditi_code'

def moveTo(x , y , Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        # print(Pirate.getID(),Pirate.getSignal())
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1
def IslandFlag(Pirate):
    x=np.array([Pirate.investigate_up(),Pirate.investigate_ne(),Pirate.investigate_right(),Pirate.investigate_se(),Pirate.investigate_down(),Pirate.investigate_sw(),Pirate.investigate_left(),Pirate.investigate_nw()])
    sum=0
    IslandFlag=['','']
    a=Pirate.getPosition()
    #print(a)
    #print(x)
    for i in range(0,8):
        if x[i][0]=="island1" or x[i][0]=="island2" or x[i][0]=="island3":
            sum=sum+1
            #print(sum)
    #print(sum)
    if sum==5:
        #up of island
        if x[0][0]!="island1" or x[0][0]!="island2" or x[0][0]!="island3":
            IslandFlag=[a[0],a[1]+1]
        #down of island
        elif x[4][0]!="island1" or x[4][0]!="island2" or x[4][0]!="island3":
            IslandFlag=[a[0],a[1]-1]
        #right of island
        elif x[2][0]!="island1" or x[2][0]!="island2" or x[2][0]!="island3":
            IslandFlag=[a[0]-1,a[1]]
        #left of island
        elif x[6][0]!="island1" or x[6][0]!="island2" or x[6][0]!="island3":
            IslandFlag=[a[0]+1,a[1]]
    elif sum==3:
        #ne of island
        if ((x[0][0]!="island1" or x[0][0]!="island2" or x[0][0]!="island3") and
            (x[2][0]!="island1" or x[2][0]!="island2" or x[2][0]!="island3")
        ):
            IslandFlag=[a[0]-1,a[1]+1]
        #nw of island
        elif ((x[0][0]!="island1" or x[0][0]!="island2" or x[0][0]!="island3") and
            (x[6][0]!="island1" or x[6][0]!="island2" or x[6][0]!="island3")
        ):
            IslandFlag=[a[0]+1,a[1]+1]
        #se of island
        elif ((x[4][0]!="island1" or x[4][0]!="island2" or x[4][0]!="island3") and
            (x[2][0]!="island1" or x[2][0]!="island2" or x[2][0]!="island3")
        ):
            IslandFlag=[a[0]-1,a[1]-1]
        #sw of island
        elif ((x[4][0]!="island1" or x[4][0]!="island2" or x[4][0]!="island3") and
            (x[6][0]!="island1" or x[6][0]!="island2" or x[6][0]!="island3")
        ):
            IslandFlag=[a[0]+1,a[1]-1]
    elif sum==8:
        #centre of island
        IslandFlag=[a[0],a[1]]

    return IslandFlag    
def IslandTeamSignal(pirate):
    current = pirate.investigate_current()[0]
    if(current=='island1'):
        [x, y] = IslandFlag(pirate,1)
        rest = pirate.getTeamSignal()[4:]
        if x<=9:
            x = '0'+str(x)
        else:
            x = str(x)

        if y<=9:
            y = '0'+str(y)
        else:
            y = str(y)
        pirate.setTeamSignal(x+y+rest)

    elif(current=='island2'):
        [x, y] = IslandFlag(pirate,2)
        rest1 = pirate.getTeamSignal()[:4]
        rest2 = pirate.getTeamSignal()[8:]
        if x<=9:
            x = '0'+str(x)
        else:
            x = str(x)

        if y<=9:
            y = '0'+str(y)
        else:
            y = str(y)
        pirate.setTeamSignal(rest1+x+y+rest2)

    if(current=='island3'):
        [x, y] = IslandFlag(pirate,3)
        rest1 = pirate.getTeamSignal()[:8]
        if len(pirate.getTeamSignal())>12: rest2 = pirate.getTeamSignal()[12:]
        else: rest2 = ''
        if x<=9:
            x = '0'+str(x)
        else:
            x = str(x)

        if y<=9:
            y = '0'+str(y)
        else:
            y = str(y)
        pirate.setTeamSignal(rest1+x+y+rest2)

def checkfriends(pirate , quad ):
    sum = 0 
    up = pirate.investigate_up()[1]
    down = pirate.investigate_down()[1]
    left = pirate.investigate_left()[1]
    right = pirate.investigate_right()[1]
    ne = pirate.investigate_ne()[1]
    nw = pirate.investigate_nw()[1]
    se = pirate.investigate_se()[1]
    sw = pirate.investigate_sw()[1]
    
    if(quad=='ne'):
        if(up == 'friend'):
            sum +=1 
        if(ne== 'friend'):
            sum +=1 
        if(right == 'friend'):
            sum +=1 
    if(quad=='se'):
        if(down == 'friend'):
            sum +=1 
        if(right== 'friend'):
            sum +=1 
        if(se == 'friend'):
            sum +=1 
    if(quad=='sw'):
        if(down == 'friend'):
            sum +=1 
        if(sw== 'friend'): 
            sum +=1 
        if(left == 'friend'):
            sum +=1 
    if(quad=='nw'):
        if(up == 'friend'):
            sum +=1 
        if(nw == 'friend'):
            sum +=1 
        if(left == 'friend'):
            sum +=1 

    return sum

def spread2(pirate):
    X_orig=pirate.getDimensionX()
    X_orig=int(X_orig)-1
    Y_orig=pirate.getDimensionX()
    Y_orig=int(Y_orig)-1
    X=randint(X_orig//7,X_orig//3)
    Y=randint(Y_orig//7,Y_orig//3)
    deploy=pirate.getDeployPoint()
    if(deploy[0]==0 and deploy[1]==0):
        return moveTo(X_orig,Y,pirate)
    if(deploy[0]==0 and deploy[1]==Y_orig):
        return moveTo(X,0,pirate)
    if(deploy[0]==X_orig and deploy[1]==Y_orig):
        return moveTo(0,Y_orig-Y,pirate)
    if(deploy[0]==X_orig and deploy[1]==0):
        return moveTo(X_orig-X,Y_orig,pirate)

def spread3(pirate):
    X_orig=pirate.getDimensionX()
    X_orig=int(X_orig)-1
    Y_orig=pirate.getDimensionX()
    Y_orig=int(Y_orig)-1
    deploy=pirate.getDeployPoint()
    X=randint(X_orig//7,X_orig//3)
    Y=randint(Y_orig//7,Y_orig//3)
    if(deploy[0]==0 and deploy[1]==0):
        return moveTo(X,Y_orig,pirate)
    if(deploy[0]==0 and deploy[1]==Y_orig):
        return moveTo(X_orig,Y_orig-Y,pirate)
    if(deploy[0]==X_orig and deploy[1]==Y_orig):
        return moveTo(X_orig-X,0,pirate)
    if(deploy[0]==X_orig and deploy[1]==0):
        return moveTo(0,Y,pirate)
    
def spread1(pirate):
    X_orig=pirate.getDimensionX()
    X_orig=int(X_orig)-1
    Y_orig=pirate.getDimensionX()
    Y_orig=int(Y_orig)-1
    deploy=pirate.getDeployPoint()
    # Xi=randint(X_orig//2,X_orig//3)
    # Yi=randint(Y_orig//7,Y_orig//3)
    if(deploy[0]==0 and deploy[1]==0):
        return moveTo(X_orig,Y_orig,pirate)
    if(deploy[0]==0 and deploy[1]==Y_orig):
        return moveTo(X_orig,0,pirate)
    if(deploy[0]==X_orig and deploy[1]==Y_orig):
        return moveTo(0,0,pirate)
    if(deploy[0]==X_orig and deploy[1]==0):
        return moveTo(0,Y_orig,pirate)
    
def spread(pirate):
    sw = checkfriends(pirate ,'sw' )
    se = checkfriends(pirate ,'se' )
    ne = checkfriends(pirate ,'ne' )
    nw = checkfriends(pirate ,'nw' )
   
    my_dict = {'sw': sw, 'se': se, 'ne': ne, 'nw': nw}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    x, y = pirate.getPosition()
    
    if( x == 0 , y == 0):
        return randint(1,4)
    
    if(sorted_dict[list(sorted_dict())[3]] == 0 ):
        return randint(1,4)
    
    if(list(sorted_dict())[0] == 'sw'):
        return moveTo(x-1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'se'):
        return moveTo(x+1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'ne'):
        return moveTo(x+1 , y-1 , pirate)
    elif(list(sorted_dict())[0] == 'nw'):
        return moveTo(x-1 , y-1 , pirate)

def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    s = pirate.trackPlayers()
    curren=pirate.investigate_current()[0]
    abc=pirate.getPosition()
    bcd=pirate.getID()
    # print(bcd)
    time_frame=pirate.getCurrentFrame()
    time_frame=int(time_frame)
    X_orig=pirate.getDimensionX()
    X_orig=int(X_orig)-1

    Y_orig=pirate.getDimensionX()
    Y_orig=int(Y_orig)-1
    Mx=0
    My=0
    if len(pirate.getSignal())>1:
        si=pirate.getSignal()
        l = si.split(",")
        Mx=int(l[1])
        My=int(l[2])
    if pirate.getSignal()=="":
        pirate.setSignal("0") 
    if len(pirate.getSignal())==1:
        Mx=randint(0,X_orig)
        My=randint(0,Y_orig)
        si=pirate.getSignal()[0]+","+str(Mx)+","+str(My)
        pirate.setSignal(si)

    if x==Mx and y==My:
        si=pirate.getSignal()[0]
        pirate.setSignal(si)         
    if (
        (up == "island1" and s[0] != "myCaptured" and s[0] != 'myCapturing' and time_frame>100)
        or (up == "island2" and s[1] != "myCaptured" and s[1] != 'myCapturing' and time_frame>100)
        or (up == "island3" and s[2] != "myCaptured" and s[2] != 'myCapturing' and time_frame>100)
    ):
        si = up[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(si)

    if (
        (down == "island1" and s[0] != "myCaptured" and s[0] != 'myCapturing' and time_frame>100)
        or (down == "island2" and s[1] != "myCaptured" and s[1] != 'myCapturing' and time_frame>100)
        or (down == "island3" and s[2] != "myCaptured" and s[2] != 'myCapturing' and time_frame>100)
    ):
        si = down[-1] + str(x) + "," + str(y + 1)
        pirate.setTeamSignal(si)

    if (
        (left == "island1" and s[0] != "myCaptured" and s[0] != 'myCapturing' and time_frame>100)
        or (left == "island2" and s[1] != "myCaptured" and s[1] != 'myCapturing'  and time_frame>100)
        or (left == "island3" and s[2] != "myCaptured" and s[2] != 'myCapturing' and time_frame>100)
    ):
        si = left[-1] + str(x - 1) + "," + str(y)
        pirate.setTeamSignal(si)

    if (
        (right == "island1" and s[0] != "myCaptured" and s[0] != 'myCapturing' and time_frame>100) 
        or (right == "island2" and s[1] != "myCaptured" and s[1] != 'myCapturing' and time_frame>100)
        or (right == "island3" and s[2] != "myCaptured" and s[2] != 'myCapturing' and time_frame>100)
    ):
        si = right[-1] + str(x + 1) + "," + str(y)
        pirate.setTeamSignal(si)
    # if ( s[0] == 'myCapturing' or s[1] == 'myCapturing' or s[2] == 'myCapturing' or s[0]=="" or s[1]=="" or s[2]=="" ):
    #     si=""
    #     pirate.setSignal(si)
    if( s[0] == 'myCapturing' or s[1] == 'myCapturing' or s[2] == 'myCapturing' or s[0]=="" or s[1]=="" or s[2]=="" ):
        si=""
        pirate.setTeamSignal(si)
    if ((curren=='island1' and s[0]=='myCapturing') or (curren=='island2' and s[1]=='myCapturing')
        or (curren=='island3' and s[2]=='myCapturing')
    ):
        abcd=pirate.getSignal()
        si="1"+abcd[1:]
        pirate.setSignal(si)
    if ((curren=='island1' and s[0]=='myCaptured') or (curren=='island2' and s[1]=='myCaptured')
        or (curren=='island3' and s[2]=='myCaptured')
    ):
        abcd=pirate.getSignal()
        si="0"+abcd[1:]
        # print(si)
        pirate.setSignal(si)

    

    # print(bcd,pirate.getSignal())

    if pirate.getTeamSignal() != "" and time_frame>125:
        s = pirate.getTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])
        return moveTo(x, y, pirate)
    
    elif pirate.getSignal()[0]=='1' and time_frame>125 and (curren=="island1" or curren=="island2" or curren=="island3"):
        if (up[:6]=="island"):
            return moveTo(x,y-1,pirate)
        elif left[:6]=="island":
            return moveTo(x-1,y,pirate)
        elif down[:6]=="island":
            return moveTo(x,y+1,pirate)
        elif right[:6]=="island":
            return moveTo(x+1,y,pirate)
        return moveTo(abc[0],abc[1],pirate)
    elif len(pirate.getSignal())>1:
        si=pirate.getSignal()
        l = si.split(",")
        x=int(l[1])
        y=int(l[2])
        return moveTo(x,y,pirate)

    else:

        if True :
            if int(bcd)%3==0:
                return spread2(pirate)
            if int(bcd)%3==1:
                return spread3(pirate)
            if int(bcd)%3==2:
                return spread1(pirate)
        else:
            return spread(pirate)
    return spread(pirate)


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()
    global abc
    abc=team.getDimensionX()
    # print(team.getListOfSignals())
    # print("---------------------------") 
    t=team.getCurrentFrame()   

    if (t>150):
        team.buildWalls(1)
        team.buildWalls(2)
        team.buildWalls(3)

    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")