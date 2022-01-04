
##Harry Rudoloph
##rudolph2@seattleu.edu

##OKC Thunder Coding Assesment
##This program gets shot data contining (Team,xcoord,ycoord,shot made)
##from a CSV file and outputs the effective field goal percentage for 2ptrs,
##NC3's and Corner3's for each team as well as the shot distribution from each
##area for each team
##all assumptions about court dimensions are taken from
##https://proformancehoops.com/basketball-court-dimensions/

#Import CSV module
import csv
#import math module
import math

#declare   variables for team A and team B


#total Corner 3's
cornerA = 0
cornerB = 0

#Corner 3's made
cornerMadeA = 0
cornerMadeB = 0

#total NC3's
nc3A = 0
nc3B = 0

#NC3 made
nc3MadeA = 0 
nc3MadeB = 0

#total two's
twoA = 0
twoB = 0

#two's made
twoMadeA = 0
twoMadeB = 0


#class driver
def main():
    
  #filename
    fName= "shots_data.csv"
    with open(fName) as file:

        #instantitate csv reader
        readIn= csv.reader(file)
        #read header 
        next(readIn)

        #get each row/attempt and read into variables
        for row in readIn:
            team, x,y, make= tuple(row)
            #evaluate incoming data using shotCounter
            xcoord = float(x)
            ycoord = float(y)
            mk = float(make)
            shotCounter(team,xcoord,ycoord,mk)

    #Print EFG for Corner Threes
    print("Corner Three effective field goal percentages: \n\n")
    print("Team A: " + eFG(cornerMadeA,0,cornerA) + "\n")
    print("Team B: " + eFG(cornerMadeB,0,cornerB ) + "\n")

    #Print EFG for Threes
    print("Non-Corner Three effective field goal percentages: \n\n")
    print("Team A: " + eFG(nc3MadeA,0,nc3A) + "\n")
    print("Team B: " + eFG(nc3MadeB,0,nc3B) + "\n")

    #Print EFG for Twos
    print("Two point effective field goal percentages: \n\n")
    print("Team A: " + eFG(twoMadeA,0,twoA) + "\n")
    print("Team B: " + eFG(twoMadeB,0,twoB) + "\n\n")

    totA = nc3A + cornerA + twoA
    totB = nc3B + cornerB + twoB

    #Print Percentage Shot Distribution for Corner Threes
    print("Shot Distribution for Corner Threes:  \n\n")
    print("Team A: " + shotDistribution(cornerA, totA) + "\n")
    print("Team B: " + shotDistribution(cornerB, totB) + "\n")

    #Print Percentage Shot Distribution for Non-Corner Threes\  
    print("Shot Distribution for Non-Corner Threes:  \n\n")
    print("Team A: " + shotDistribution(nc3A, totA) + "\n")
    print("Team B: " + shotDistribution(nc3B, totB) + "\n")

    #Print Percentage Shot Distribution for Twos
    print("Shot Distribution for Two:  \n\n")
    print("Team A: " + shotDistribution(twoA, totA ) + "\n")
    print("Team B: " + shotDistribution(twoB, totB ) + "\n")

        

#the shotCounter adds the shot attempt to the correct   if the
#attempt is taken within the regulation NBA court                     
def shotCounter(team,x,y, make):
    global cornerA
    global cornerMadeA
    global nc3A
    global nc3MadeA
    global twoA
    global twoMadeA
    global cornerB
    global cornerMadeB
    global nc3B
    global nc3MadeB
    global twoB
    global twoMadeB

    
    #determine if attempt in bounds
    if isInBounds(x,y):
        #for teamA
        if team == "Team A":
            #if Corner3 add to corner3 counter
            if isCorner(x,y):
                cornerA += 1
                #if make add to corner3 make counter
                if make == 1:
                    cornerMadeA += 1
            #if NC3 add to NC3 counter   
            elif isNC3(x,y):
                nc3A += 1
                if make == 1:
                      nc3MadeA += 1
            else:
                twoA += 1
                if make == 1:
                      twoMadeA += 1
        #for teamB             
        else:
        
            if isCorner(x,y):
                cornerB+= 1
                if make == 1:
                      cornerMadeB += 1
            elif isNC3(x,y):
                nc3B += 1
                if make == 1:
                      nc3MadeB += 1
            else:
                twoB += 1
                if make == 1:
                    twoMadeB += 1 
                
            

#isInBounds parameters:  x coord, y coord
#return: true if a shot is taken within the bounds of the regulation
#NBA court
def isInBounds(x,y):
    if ((x >= -25 and x <= 25) and (y >= -4.75 and y <= 89.25)):
        return True
    else:
        return False

#isCorner parameters: x coord, y coord
#return: true if a shot is a Corner 3 (y<= 7.8)
def isCorner(x,y):
    if (y<= 7.8 and abs(x)> 22.0):
        return True
    else:
        return False

#isNC3  parameters: x coord, y coord
#return : true if shot is a non-corner three
def isNC3(x,y):
    c = math.sqrt((x*x) + (y*y))
    if (c > 23.75):
        return True
    else:
        return False

#eFG parameters: three pointers made, two pointers made, field goals attempted
#return : the effective field goal percentage rounded to three decimal places
def eFG(threePM,twoPM,fGA):
    if (fGA > 0):
        efg = (((threePM+twoPM) + (.5*threePM))/fGA)*100
        formatter = "{0:10.5}"
        output= formatter.format(efg)
        return output
    else: return "0"

#shotDistribution parameters # of attempts for type, total number of attempts
def shotDistribution(typeAttempts,attempts):
    if (attempts > 0):
        dist = (typeAttempts/attempts) * 100
        formatter = "{0:10.5}"
        output = formatter.format(dist)
        return output
    else: return "0"
        

main()
    

