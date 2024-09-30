from random import randint 

name = 'sample4'

def moveTo(x , y , Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1
    
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
    X=randint(X_orig//6,X_orig//3)
    Y=randint(X_orig//6,X_orig//3)
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
    X=randint(X_orig//6,X_orig//3)
    Y=randint(X_orig//6,X_orig//3)
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
    pirate.setSignal("")
    s = pirate.trackPlayers()
    curren=pirate.investigate_current()[0]
    abc=pirate.getPosition()
    bcd=pirate.getID()
    time_frame=pirate.getCurrentFrame()
    time_frame=int(time_frame)
    if (
        (up == "island1" and s[0] != "myCaptured" and s[0] != 'myCapturing')
        or (up == "island2" and s[1] != "myCaptured" and s[1] != 'myCapturing')
        or (up == "island3" and s[2] != "myCaptured" and s[2] != 'myCapturing')
    ):
        si = up[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(si)
        print(si)

    if (
        (down == "island1" and s[0] != "myCaptured" and s[0] != 'myCapturing')
        or (down == "island2" and s[1] != "myCaptured" and s[1] != 'myCapturing')
        or (down == "island3" and s[2] != "myCaptured" and s[2] != 'myCapturing')
    ):
        si = down[-1] + str(x) + "," + str(y + 1)
        pirate.setTeamSignal(si)
        print(si)

    if (
        (left == "island1" and s[0] != "myCaptured" and s[0] != 'myCapturing')
        or (left == "island2" and s[1] != "myCaptured" and s[1] != 'myCapturing')
        or (left == "island3" and s[2] != "myCaptured" and s[2] != 'myCapturing')
    ):
        si = left[-1] + str(x - 1) + "," + str(y)
        pirate.setTeamSignal(si)
        print(si)

    if (
        (right == "island1" and s[0] != "myCaptured" and s[0] != 'myCapturing') 
        or (right == "island2" and s[1] != "myCaptured" and s[1] != 'myCapturing')
        or (right == "island3" and s[2] != "myCaptured" and s[2] != 'myCapturing')
    ):
        si = right[-1] + str(x + 1) + "," + str(y)
        pirate.setTeamSignal(si)
        print(si)
    if ( s[0] == 'myCapturing' or s[1] == 'myCapturing' or s[2] == 'myCapturing' or s[0]=="" or s[1]=="" or s[2]=="" ):
        si=""
        pirate.setTeamSignal(si)
    if ((curren=='island1' and s[0]=='myCapturing') or (curren=='island2' and s[1]=='myCapturing')
        or (curren=='island3' and s[2]=='myCapturing')
    ):
        si="capturing"
        pirate.setSignal(si)
    if pirate.getTeamSignal() != "":
        s = pirate.getTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])
        return moveTo(x, y, pirate)
    
    elif pirate.getSignal()=='capturing':
        return moveTo(abc[0],abc[1],pirate)
    else:
        if int(time_frame)<100 or (time_frame>150 and time_frame<180) :
            if int(bcd)%3==0:
                return spread2(pirate)
            if int(bcd)%3==1:
                return spread3(pirate)
            if int(bcd)%3==2:
                return spread1(pirate)
        else:
            return spread(pirate)



def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()
    global abc
    abc=team.getDimensionX()
    

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)

    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")