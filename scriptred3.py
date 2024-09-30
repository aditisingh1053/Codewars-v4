from random import randint 
from random import choice

name = 'scriptred3'

def binary_to_decimal(binary_string):
    decimal_number = 0
    power = 0
    for digit in binary_string[::-1]:  # Reverse the string
        decimal_number += int(digit) * 2**power
        power += 1
    return decimal_number

def decimal_to_binary(decimal_number):
    binary_string = bin(decimal_number)[2:]  # Remove '0b' prefix
    # Pad with zeros if necessary
    # binary_string = binary_string.zfill(n)
    return binary_string

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
    # print(up)
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
    
def farspread(pirate):
    (x0, y0) = pirate.getPosition()
    s1= checkfriends(pirate,'sw')
    s2=checkfriends(pirate,'se')
    s3=checkfriends(pirate,'nw')
    s4=checkfriends(pirate,'ne')
    s=s1+s2+s3+s4
    if(s<3):
        return spread(pirate)
    else:
        x = x0 + randint(5,35)
        y = y0 + randint(5,35)
        return moveTo(x%40, y%40, pirate)
    
    
def islandspread(x0, y0, pirate):
    x=randint(x0-4,x0+4)
    y=randint(y0-4,y0+4)
    if (x <= x0-3 or x >= x0+3) and (y <= y0-3 or y >= y0+3):
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


#ignore
def CaptureIsland(pirate, i):   
    isl = "island" + str(i)
    n = (i) - 1
    s = pirate.trackPlayers()

    signals = bin(int(pirate.getTeamSignal()[12:]))
    signals = str(signals)[2:]

    beingCaptured = False
    for j in len(signals)/3:
        if signals[3*j+n]==1:
            beingCaptured = True
            break

    if not beingCaptured:
        sig = pirate.getTeamSignal()
        return moveTo(int(sig[4*n:4*n+2]), int(sig[4*n+2:4*n+4]), pirate)
#ignore
    
def FindCaptureIsland(pirate):
    IslandTeamSignal(pirate)
    x = pirate.investigate_current()
    if x == 'island1':
        return CaptureIsland(pirate, 1)
    elif x == 'island2':
        return CaptureIsland(pirate, 2)
    elif x == 'island3':
        return CaptureIsland(pirate, 3)



def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    nw = pirate.investigate_nw()[0]
    ne = pirate.investigate_nw()[0]
    sw = pirate.investigate_sw()[0]
    se = pirate.investigate_se()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    (x, y) = pirate.getPosition()
    if (x, y) == pirate.getDeployPoint():
        pirate.setSignal("000")
    s = pirate.trackPlayers()
    curren=pirate.investigate_current()[0]
    bcd=pirate.getID()
    time_frame=pirate.getCurrentFrame()
    time_frame=int(time_frame)
    
    if bcd!='':

        if int(bcd)%3==1 and int(time_frame)<100 :
                for i in range(3):
                    isl = 'island' + str(i+1)
                    if curren==isl:
                        IslandTeamSignal(pirate)
                        signals = decimal_to_binary(int(pirate.getTeamSignal()[12:]))
                        if len(signals)%3==1:
                            signals = '00' + signals
                        elif len(signals)%3==2:
                            signals = '0' + signals
                        beingCaptured = False
                        for j in range(len(signals)//3):
                            if signals[3*j+i]==1:
                                beingCaptured = True
                                break

                        if not beingCaptured:
                            sig = pirate.getTeamSignal()
                            new = pirate.getSignal()
                            new = new[:i] + '1' + new[i+1:] 
                            pirate.setSignal(new)
                            return moveTo(int(sig[4*i:4*i+2]), int(sig[4*i+2:4*i+4]), pirate)
                        
                return spread2(pirate)
            
        elif int(bcd)%3==2 and int(time_frame)<100 :
                for i in range(3):
                    isl = 'island' + str(i+1)
                    if curren==isl:
                        IslandTeamSignal(pirate)
                        signals = decimal_to_binary(int(pirate.getTeamSignal()[12:]))
                        if len(signals)%3==1:
                            signals = '00' + signals
                        elif len(signals)%3==2:
                            signals = '0' + signals
                        beingCaptured = False
                        for j in range(len(signals)//3):
                            if signals[3*j+i]==1:
                                beingCaptured = True
                                break

                        if not beingCaptured:
                            sig = pirate.getTeamSignal()
                            new = pirate.getSignal()
                            new = new[:i] + '1' + new[i+1:] 
                            pirate.setSignal(new)
                            return moveTo(int(sig[4*i:4*i+2]), int(sig[4*i+2:4*i+4]), pirate)
                        
                    
                return spread3(pirate)
        
        
        elif int(bcd)%3==0 and int(time_frame)<120:
                for i in range(3):
                    isl = 'island' + str(i+1)
                    if curren==isl:
                        IslandTeamSignal(pirate)
                        signals = decimal_to_binary(int(pirate.getTeamSignal()[12:]))
                        if len(signals)%3==1:
                            signals = '00' + signals
                        elif len(signals)%3==2:
                            signals = '0' + signals

                        beingCaptured = False
                        for j in range(len(signals)//3):
                            if signals[3*j+i]==1:
                                beingCaptured = True
                                break

                        if not beingCaptured:
                            sig = pirate.getTeamSignal()
                            new = pirate.getSignal()
                            new = new[:i] + '1' + new[i+1:] 
                            pirate.setSignal(new)
                            return moveTo(int(sig[4*i:4*i+2]), int(sig[4*i+2:4*i+4]), pirate)

                return spread1(pirate)
            
        else:
                piratePresent = [False, False, False]
                for i in range(3):
                    isl = 'island' + str(i+1)
                    if curren==isl:
                        IslandTeamSignal(pirate)
                        signals = decimal_to_binary(int(pirate.getTeamSignal()[12:]))
                        if len(signals)%3==1:
                            signals = '00' + signals
                        elif len(signals)%3==2:
                            signals = '0' + signals

                        beingCaptured = False
                        for j in range(len(signals)//3):
                            if signals[3*j+i]==1:
                                beingCaptured = True
                                break
                        
                        piratePresent[i] = beingCaptured

                        if not beingCaptured:
                            sig = pirate.getTeamSignal()
                            new = pirate.getSignal()
                            new = new[:i] + '1' + new[i+1:] 
                            pirate.setSignal(new)
                            return moveTo(int(sig[4*i:4*i+2]), int(sig[4*i+2:4*i+4]), pirate)
                
                # for i in range(3):
                #     sig = pirate.getTeamSignal()
                #     if piratePresent[i]==False and sig[4*i:4*i+4]!='....':
                #         return moveTo(int(sig[4*i:4*i+2]), int(sig[4*i+2:4*i+4]), pirate)
                       

                # return spread(pirate)
                  
    else:
                piratePresent = [False, False, False]
                for i in range(3):
                    isl = 'island' + str(i+1)
                    if curren==isl:
                        IslandTeamSignal(pirate)
                        signals = decimal_to_binary(int(pirate.getTeamSignal()[12:]))
                        if len(signals)%3==1:
                            signals = '00' + signals
                        elif len(signals)%3==2:
                            signals = '0' + signals
                        beingCaptured = False
                        for j in range(len(signals)//3):
                            if signals[3*j+i]==1:
                                beingCaptured = True
                                break

                        piratePresent[i] = beingCaptured

                        if not beingCaptured:
                            sig = pirate.getTeamSignal()
                            new = pirate.getSignal()
                            new = new[:i] + '1' + new[i+1:] 
                            pirate.setSignal(new)
                            return moveTo(int(sig[4*i:4*i+2]), int(sig[4*i+2:4*i+4]), pirate)
                        
                # for i in range(3):
                #     sig = pirate.getTeamSignal()
                #     if piratePresent[i]==False and sig[4*i:4*i+4]!='....':
                #         return moveTo(int(sig[4*i:4*i+2]), int(sig[4*i+2:4*i+4]), pirate)
                
                # return spread(pirate)

def ActTeam(team):
    if team.getTeamSignal()=='':
        team.setTeamSignal("............")
    
    pirateSignals = team.getListOfSignals()
    if len(pirateSignals)>0 and pirateSignals[0]!='000':
        pirateSignals = ['000','000','000','000','000','000','000','000']
    binstr = "".join(pirateSignals)
    print(team.getTeamSignal())
    dec = binary_to_decimal(binstr)
    orig = team.getTeamSignal()[:12]
    team.setTeamSignal(orig + str(dec))

    # print(pirateSignals)

    # print(team.getTeamSignal())
    global xsize
    xsize=team.getDimensionX()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)



    