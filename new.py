from random import randint 
from random import choice

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
    
    
def spread(pirate):
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
    
def islandspread(x0, y0, pirate):
    x=randint(x0-3,x0+3)
    y=randint(y0-3,y0+3)
    if (x <= x0-2 or x >= x0+2) and (y <= y0-2 or y >= y0+2):
        return moveTo(x,y,pirate)
    else:
        if x == x0-1: x=x-1
        elif x == x0+1: x=x+1
        else: x = x + choice([-2,2])

        if y == y0-1: y=y-1
        elif y == y0+1: y=y+1
        else: y = y + choice([-2,2])

        return moveTo(x,y,pirate)
        

import numpy as np

def IslandFlag(Pirate, i):
    x=np.array([Pirate.investigate_up(),Pirate.investigate_ne(),Pirate.investigate_right(),Pirate.investigate_se(),Pirate.investigate_down(),Pirate.investigate_sw(),Pirate.investigate_left(),Pirate.investigate_nw()])
    sum=0
    isl = "island" + str(i)
    IslandFlag=['','']
    a=Pirate.getPosition()
    #print(a)
    #print(x)
    for i in range(0,8):
        if x[i][0]==isl:
            sum=sum+1
            #print(sum)
    #print(sum)
    if sum==5:
        #up of island
        if x[0][0]!=isl:
            IslandFlag=[a[0],a[1]+1]
        #down of island
        elif x[4][0]!=isl:
            IslandFlag=[a[0],a[1]-1]
        #right of island
        elif x[2][0]!=isl:
            IslandFlag=[a[0]-1,a[1]]
        #left of island
        elif x[6][0]!=isl:
            IslandFlag=[a[0]+1,a[1]]
    elif sum==3:
        #ne of island
        if ((x[0][0]!=isl) and
            (x[2][0]!=isl)
        ):
            IslandFlag=[a[0]-1,a[1]+1]
        #nw of island
        elif ((x[0][0]!=isl) and
            (x[6][0]!=isl)
        ):
            IslandFlag=[a[0]+1,a[1]+1]
        #se of island
        elif ((x[4][0]!=isl) and
            (x[2][0]!=isl)
        ):
            IslandFlag=[a[0]-1,a[1]-1]
        #sw of island
        elif ((x[4][0]!=isl) and
            (x[6][0]!=isl)
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


def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    nw = pirate.investigate_nw()[0]
    ne = pirate.investigate_nw()[0]
    sw = pirate.investigate_sw()[0]
    se = pirate.investigate_se()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    curren=pirate.investigate_current()[0]
    # print(curren)
    bcd=pirate.getID()
    # if bcd=='':
    #     print("helloooo")
    # print(bcd)
    time_frame=pirate.getCurrentFrame()
    time_frame=int(time_frame)
    
    if bcd!='':

        if int(time_frame)<50 :
            if int(bcd)%3==0:
                if(curren=='island1'):
                    IslandTeamSignal(pirate)

                elif(curren=='island2'):
                    IslandTeamSignal(pirate)

                elif(curren=='island3'):
                    IslandTeamSignal(pirate)

                return spread(pirate)
            if int(bcd)%3==1:
                if(curren=='island1'):
                    IslandTeamSignal(pirate)

                elif(curren=='island2'):
                    IslandTeamSignal(pirate)

                elif(curren=='island3'):
                    IslandTeamSignal(pirate)
                return spread(pirate)
            
            if int(bcd)%3==2:
                if(curren=='island1'):
                    IslandTeamSignal(pirate)

                elif(curren=='island2'):
                    IslandTeamSignal(pirate)

                elif(curren=='island3'):
                    IslandTeamSignal(pirate)
                return spread(pirate)
            
        else:
            if int(pirate.getID())%4 == 0 and pirate.getTeamSignal()[0:4]!='....':
                x1 = int(pirate.getTeamSignal()[0:2])
                y1 = int(pirate.getTeamSignal()[2:4])
            
                if (up=='island1' or down=='island1' or left=='island1' or right=='island1'
                    or nw=='island1' or ne=='island1' or se=='island1' or sw=='island1') and (curren!='island1'):
                    if s[0] == 'myCapturing' or s[0] ==  'myCaptured':
                        return islandspread(x1, y1, pirate)
                    else:
                        return moveTo(x1,y1,pirate)
                
                elif(curren=='island1' ):
                    if s[0] == 'myCapturing':
                        return moveTo(x1,y1,pirate)
                    elif s[0] == 'myCaptured':
                        return islandspread(x1,y1,pirate)
                
                else:
                    return islandspread(x1,y1,pirate)
                    
            elif int(pirate.getID())%4 == 1 and pirate.getTeamSignal()[4:8]!='....':
                x2 = int(pirate.getTeamSignal()[4:6])
                y2 = int(pirate.getTeamSignal()[6:8])
                if (up=='island2' or down=='island2' or left=='island2' or right=='island2'
                    or nw=='island2' or ne=='island2' or se=='island2' or sw=='island2') and (curren!='island2'):
                    if s[1] == 'myCapturing' or s[1] ==  'myCaptured':
                        return islandspread(x2, y2, pirate)
                    else:
                        return moveTo(x2,y2,pirate)
                
                elif curren=='island2':
                    if s[1] == 'myCapturing':
                        return moveTo(x2,y2,pirate)
                    elif s[1] == 'myCaptured':
                        return islandspread(x2,y2,pirate)
                    
                else:
                    return islandspread(x2,y2,pirate)
                    
            elif int(pirate.getID())%4 == 2 and pirate.getTeamSignal()[8:12]!='....':
                x3 = int(pirate.getTeamSignal()[8:10])
                y3 = int(pirate.getTeamSignal()[10:12])
                if (up=='island3' or down=='island3' or left=='island3' or right=='island3'
                    or nw=='island3' or ne=='island3' or se=='island3' or sw=='island3') and curren!='island3':
                    if s[2] == 'myCapturing' or s[2] ==  'myCaptured':
                        return islandspread(x3, y3, pirate)
                    else:
                        return moveTo(x3,y3,pirate)
                
                elif (curren=='island3'):
                    if s[2] == 'myCapturing':
                        return moveTo(x3,y3,pirate)
                    elif s[2] == 'myCaptured':
                        return islandspread(x3,y3,pirate)
                    
                else:
                    islandspread(x3,y3,pirate)
                    
                    
            else:
                if(curren=='island1'):
                    if(pirate.getTeamSignal()[0:4]=="...."):
                        [xdash, ydash] = IslandFlag(pirate,1)
                        if xdash <= 9: xdash = '0' + str(xdash)
                        else: xdash = str(xdash)
                        if ydash <= 9: ydash = '0' + str(ydash)
                        else: ydash = str(ydash)
                        final = pirate.getTeamSignal()[4:]
                        final = xdash + ydash + final
                        pirate.setTeamSignal(final)

                elif(curren=='island2'):
                    if(pirate.getTeamSignal()[4:8]=="...."):
                        [xdash, ydash] = IslandFlag(pirate,2)
                        if xdash <= 9: xdash = '0' + str(xdash)
                        else: xdash = str(xdash)
                        if ydash <= 9: ydash = '0' + str(ydash)
                        else: ydash = str(ydash)
                        final1 = pirate.getTeamSignal()[:4]
                        final2=pirate.getTeamSignal()[8:]
                        final = final1+xdash + ydash + final2
                        pirate.setTeamSignal(final)

                elif(curren=='island3'):
                    if(pirate.getTeamSignal()[8:12]=="...."):
                        [xdash, ydash] = IslandFlag(pirate,3)
                        if xdash <= 9: xdash = '0' + str(xdash)
                        else: xdash = str(xdash)
                        if ydash <= 9: ydash = '0' + str(ydash)
                        else: ydash = str(ydash)
                        final = pirate.getTeamSignal()[:8]
                        final = final + xdash + ydash
                        pirate.setTeamSignal(final)
                return spread(pirate)
            
    else:
        return spread(pirate)

def ActTeam(team):
    if team.getTeamSignal()=='':
        team.setTeamSignal("............")

    print(team.getTeamSignal())
    global xsize
    xsize=team.getDimensionX()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)