#!/usr/local/opt/python/bin/python3.7

##############################################################################################
# xyMerge.py
#
# Simple program to merge two X and Y stepper motor
#   gcode music tracks into a single XY trajectory.
#   I think this is what professional musicians do.
# Author: Doug James, 2019
##############################################################################################

import math

def getG01Lines(lines):
    glines = [];
    for line in lines:
        if(line.startswith("G01")):
            glines.append(line);
    return glines;

# Parses a G01 line of the form:
#          G01 X1.23600000 F247.20000000
# and returns the position and feed as a list, [X,F].
def parseG01Line(line):
    if(not line.startswith("G01")):
        print("!line.startswith(G01)");
        exit();

    tokens = line.split();
    X  = 0; # X or Y coord
    F  = 0; # Feed rate
    for token in tokens:
        if(token.startswith("F")):
            F = float(token[1:]);
        elif(token.startswith("X")):
            X = float(token[1:]);
        elif(token.startswith("Y")):
            X = float(token[1:]);

    return [X, F];
        
    

xfile  = "GameofThrones_-_1voice_-_melody.nc"
yfile  = "GameofThrones_-_1voice_-_bass.nc"
xyfile = "GameofThrones_-_2voice_-_xyMerge.nc"

xfo = open(xfile, "r")
yfo = open(yfile, "r")
print("X file: ", xfo.name)
print("Y file: ", yfo.name)
xLines = xfo.readlines()
yLines = yfo.readlines()
xfo.close()
yfo.close()


print("|xLines|: ", len(xLines))
print("|yLines|: ", len(yLines))

# extract just the G01 commands:
xG1 = getG01Lines(xLines);
yG1 = getG01Lines(yLines);

print("|xG1|: ", len(xG1))
print("|yG1|: ", len(yG1))

# reverse lists for pop convenience:
xG1.reverse()
yG1.reverse()
    
# Example: Relevant line is a G01:
#          G01 X1.23600000 F247.20000000

xyfo = open(xyfile, "w")

xyfo.write("(xyMerge output from Doug's crazy code - USE AT OWN RISK!!! \n");
xyfo.write("G21 G90 G94 \n")
xyfo.write("G00 X0 Y0 \n")

x = 0.0;
y = 0.0;
dx   = 0.0;
dy   = 0.0;
fx   = 0.;
fy   = 0.;
fxy  = 0.;
dtx  = 0;
dty  = 0;

notDone = True;
while(notDone):

    if(dtx==0): # Try to get next line:
        if(len(xG1)==0):
            print("xG1 is empty");
            print("dtx=",dtx,", dty=",dty);
            notDone = False;
        else: # Process new pos/feed
            [newX, fx] = parseG01Line(xG1.pop());
            dx  = newX - x;
            dtx = dx/fx;
            
    if(dty==0): # Try to get next line:
        if(len(yG1)==0):
            print("yG1 is empty");
            print("dtx=",dtx,", dty=",dty);
            notDone = False;
        else: # Process new pos/feed
            [newY, fy] = parseG01Line(yG1.pop());
            dy  = newY - y;
            dty = dy/fy;

    # Find shortest axis time and split:
    fxy = math.sqrt( fx*fx + fy*fy ); # xy feed rate

    if(dtx < dty): # advance to end of x segment:
        # move for dtx time:
        x += dtx*fx;
        y += dtx*fy;
        dty -= dtx;
        dtx  = 0;
    elif(dty < dtx): # advance to end of x segment:
        # move for dty time:
        x += dty*fx;
        y += dty*fy;
        dtx -= dty;
        dty  = 0;
    else: # same length:
        x += dtx*fx;
        y += dtx*fy;
        dtx  = 0;
        dty  = 0;        

    g01code = "G01 X"+str(x)+ " Y"+str(y)+ " F"+str(fxy)+ "\n";
    #print(g01code);
    xyfo.write(g01code);

xyfo.write("M02\n"); # end of program
