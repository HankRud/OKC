
##Harry Rudoloph
##rudolph2@seattleu.edu

##OKC Thunder Coding Assesment
##This program gets shot data contining (Team,xcoord,ycoord,shot made)
##from a CSV file and outputs the effective field goal percentage for 2ptrs,
##NC3's and Corner3's for each team as well as the shot distribution from each
##area for each team
##all assumptions about court dimensions are taken from
##https://proformancehoops.com/basketball-court-dimensions/
##percentages are reported as decimal values

#Import CSV module
import csv
#import math module
import math

#declare   variables for team A and team B


#total_al Corner 3's
corner_attempted_a = 0
corner_attempted_b = 0

#Corner 3's made
corner_made_a = 0
corner_made_b = 0

#total_al NC3's
nc3_attempted_a = 0
nc3_attempted_b = 0

#NC3 made
nc3_made_a = 0 
nc3_made_b = 0

#total_al two's
two_attempted_a = 0
two_attempted_b = 0

#two's made
two_made_a = 0
two_made_b = 0


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

    #sum total_als of all attempts
    total_a = nc3_attempted_a + corner_attempted_a + two_attempted_a
    total_b = nc3_attempted_b + corner_attempted_b + two_attempted_b

    #Print effective_field_goal for Corner Threes 
    print("Corner Three effective field goal percentages: \n\n")
    print_ab(effective_field_goal(corner_made_a,0,corner_attempted_a),effective_field_goal(corner_made_b,0,corner_attempted_b ))

    #Print effective_field_goal for Threes
    print("Non-Corner Three effective field goal percentages: \n\n")
    print_ab(effective_field_goal(nc3_made_a,0,nc3_attempted_a),effective_field_goal(nc3_made_b,0,nc3_attempted_b))

    #Print effective_field_goal for Twos
    print("Two point effective field goal percentages: \n\n")
    print_ab(effective_field_goal(0,two_made_a,two_attempted_a),effective_field_goal(0,two_made_b,two_attempted_b))


    #Print Percentage Shot Distribution for Corner Threes
    print("Shot Distribution for Corner Threes:  \n\n")
    print_ab(shot_distribution(corner_attempted_a, total_a), shot_distribution(corner_attempted_b, total_b))

    #Print Percentage Shot Distribution for Non-Corner Threes\  
    print("Shot Distribution for Non-Corner Threes:  \n\n")
    print_ab(shot_distribution(nc3_attempted_a, total_a), shot_distribution(nc3_attempted_b, total_b) )

    #Print Percentage Shot Distribution for Twos
    print("Shot Distribution for Two:  \n\n")
    print_ab(shot_distribution(two_attempted_a, total_a), shot_distribution(two_attempted_b, total_b ))

        

#the shotCounter adds the shot attempt to the correct   if the
#attempt is taken within the regulation NBA court                     
def shotCounter(team,x,y, make):
    global corner_attempted_a
    global corner_made_a
    global nc3_attempted_a
    global nc3_made_a
    global two_attempted_a
    global two_made_a
    global corner_attempted_b
    global corner_made_b
    global nc3_attempted_b
    global nc3_made_b
    global two_attempted_b
    global two_made_b

    
    #determine if attempt in bounds
    if is_in_bounds(x,y):
        #for teamA
        if team == "Team A":
            #if Corner3 add to corner3 counter
            if is_corner(x,y):
                corner_attempted_a += 1
                #if make add to corner3 make counter
                if make == 1:
                    corner_made_a += 1
            #if NC3 add to NC3 counter   
            elif is_nc3(x,y):
                nc3_attempted_a += 1
                if make == 1:
                      nc3_made_a += 1
            else:
                #otherwise shot is a two 
                two_attempted_a += 1
                if make == 1:
                      two_made_a += 1
        #for teamB             
        else:
        
            if is_corner(x,y):
                corner_attempted_b+= 1
                if make == 1:
                      corner_made_b += 1
            elif is_nc3(x,y):
                nc3_attempted_b += 1
                if make == 1:
                      nc3_made_b += 1
            else:
                two_attempted_b += 1
                if make == 1:
                    two_made_b += 1 
                
            

#is_in_bounds parameters:  x coord, y coord
#return: true if a shot is taken within the bounds of the regulation
#NBA court
def is_in_bounds(x,y):
    if ((x >= -25 and x <= 25) and (y >= -4.75 and y <= 89.25)):
        return True
    else:
        return False

#is_corner parameters: x coord, y coord
#return: true if a shot is a Corner 3 (y<= 7.8)
def is_corner(x,y):
    if (y<= 7.8 and abs(x)> 22.0):
        return True
    else:
        return False

#is_nc3  parameters: x coord, y coord
#return : true if shot is a non-corner three
def is_nc3(x,y):
    c = math.sqrt((x*x) + (y*y))
    if (c > 23.75):
        return True
    else:
        return False

#effective_field_goal parameters: three pointers made, two pointers made, field goals attempted
#return : the effective field goal percentage rounded to three decimal places
def effective_field_goal(three_pointers_made,two_pointers_made,field_goal_attempts):
    if (field_goal_attempts > 0):
        effective_field_goal = (((three_pointers_made+two_pointers_made) + (.5*three_pointers_made))/field_goal_attempts)

        return round(effective_field_goal,3)
    else: return 0

#shot_distribution parameters # of attempts for type, total_al number of attempts
def shot_distribution(type_attempts,attempts):
    if (attempts > 0):
        distribution = (type_attempts/attempts)
        
        return round(distribution,3)
    else: return 0

#takes floats of results for each team and prints them
def print_ab(team_a_result,team_b_result):
    #print team a reasults
    print("Team A: ")
    print(team_a_result)
    print("\n")
    
    print("Team B: ")
    print(team_b_result)
    print("\n")

main()
    

