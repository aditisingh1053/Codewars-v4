from random import randint 
import numpy as np

name = 'sample4'

explored = np.full((40,40), False, dtype=bool)

def moveTo(x , y , Pirate):
    position = Pirate.getPosition()
    explored[x][y]=True
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
    
def spread(pirate):
    # 
    deploy=pirate.getDeployPoint()
    if(deploy[0]==0 and deploy[1]==0):
        return moveTo(39,39,pirate)
    if(deploy[0]==0 and deploy[1]==39):
        return moveTo(39,0,pirate)
    if(deploy[0]==39 and deploy[1]==39):
        return moveTo(0,0,pirate)
    if(deploy[0]==39 and deploy[1]==0):
        return moveTo(0,39,pirate)
#on the basis of array
    # if explored[x][y-1]:
    #     if explored[x+1][y]:
    #         if explored[x][y+1]:
    #             if not explored[x-1][y]:
    #                 return moveTo(x-1, y, pirate)
    #             else:
    #                 return randint(1,4)
    #         else:
    #             if explored[x-1][y]:
    #                 return moveTo(x, y+1, pirate)
    #             else:
    #                 if randint(1,2) == 1:
    #                     return moveTo(x, y+1, pirate)
    #                 else:
    #                     return moveTo(x-1, y, pirate)
    #     else:
    #         if not explored[x][y+1]:
    #             if not explored[x-1][y]:
    #                 return moveTo(x+1, y, pirate)
    #             else:
    #                 if randint(1,2)==1:
    #                     return moveTo(x-1, y, pirate)
    #                 else:
    #                     return moveTo(x+1, y, pirate)
    #         else:
    #             if not explored[x-1][y]:
    #                 if randint(1,2)==1:
    #                     return moveTo(x-1,y,pirate)
    #                 else:
    #                     return moveTo(x+1,y,pirate)
    #             else:
    #                 return moveTo(x+1,y,pirate)
    # else:
    #     if explored[x+1][y]:
    #         if explored[x][y+1]:
    #             if not explored[x-1][y]:
    #                 if randint(1,2)==1:
    #                     return moveTo(x-1,y,pirate)
    #                 else:
    #                     return moveTo(x,y-1,pirate)
    #             else:
    #                 return moveTo(x,y-1,pirate)
    #         else:
    #             if explored[x-1][y]:
    #                 if randint(1,2)==1:
    #                     return moveTo(x,y-1,pirate)
    #                 else:
    #                     return moveTo(x,y+1)
    #             else:
    #                 if randint(1,3)==1:
    #                     return moveTo(x,y-1,pirate)
    #                 elif randint(1,3)==2:
    #                     return moveTo(x-1,y,pirate)
    #                 else:
    #                     return moveTo(x,y+1,pirate)
    #     else:
    #         if explored[x][y+1]:
    #             if explored[x-1][y]:
    #                 if randint(1,2)==1:
    #                     return moveTo(x+1,y,pirate)
    #                 else:
    #                     return moveTo(x,y-1,pirate)
    #             else:
    #                 if randint(1,3)==1:
    #                     return moveTo(x,y-1,pirate)
    #                 elif randint(1,3)==2:
    #                     return moveTo(x-1,y,pirate)
    #                 else:
    #                     return moveTo(x+1,y,pirate)
    #         else:
    #             if explored[x][y-1]:
    #                 if explored[x-1][y]:
    #                     if randint(1,2)==1:
    #                         return moveTo(x,y+1,pirate)
    #                     else:
    #                         return moveTo(x+1,y,pirate)
    #                 else:
    #                     if randint(1,3)==1:
    #                         return moveTo(x,y+1,pirate)
    #                     elif randint(1,3)==2:
    #                         return moveTo(x-1,y,pirate)
    #                     else:
    #                         return moveTo(x+1,y,pirate)
    #             else:
    #                 if randint(1,4)==1:
    #                     return moveTo(x,y-1,pirate)
    #                 elif randint(1,4)==2:
    #                     return moveTo(x+1,y,pirate)
    #                 elif randint(1,4)==3:
    #                     return moveTo(x,y+1,pirate)
    #                 else:
    #                     return moveTo(x-1,y,pirate)
            
                    


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
    if (
        (up == "island1" and s[0] != "myCaptured" and s[0] != 'myCapturing')
        or (up == "island2" and s[1] != "myCaptured" and s[1] != 'myCapturing')
        or (up == "island3" and s[2] != "myCaptured" and s[2] != 'myCapturing')
    ):
        si = up[-1] + str(x) + "," + str(y - 1)
        pirate.setTeamSignal(si)

    if (
        (down == "island1" and s[0] != "myCaptured" and s[0] != 'myCapturing')
        or (down == "island2" and s[1] != "myCaptured" and s[1] != 'myCapturing')
        or (down == "island3" and s[2] != "myCaptured" and s[2] != 'myCapturing')
    ):
        si = down[-1] + str(x) + "," + str(y + 1)
        pirate.setTeamSignal(si)

    if (
        (left == "island1" and s[0] != "myCaptured" and s[0] != 'myCapturing')
        or (left == "island2" and s[1] != "myCaptured" and s[1] != 'myCapturing')
        or (left == "island3" and s[2] != "myCaptured" and s[2] != 'myCapturing')
    ):
        si = left[-1] + str(x - 1) + "," + str(y)
        pirate.setTeamSignal(si)

    if (
        (right == "island1" and s[0] != "myCaptured" and s[0] != 'myCapturing') 
        or (right == "island2" and s[1] != "myCaptured" and s[1] != 'myCapturing')
        or (right == "island3" and s[2] != "myCaptured" and s[2] != 'myCapturing')
    ):
        si = right[-1] + str(x + 1) + "," + str(y)
        pirate.setTeamSignal(si)
    if( s[0] == 'myCapturing' or s[1] == 'myCapturing' or s[2] == 'myCapturing' ):
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
        return spread(pirate)


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()
    # print(team.getDimensionX())
    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)

    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")