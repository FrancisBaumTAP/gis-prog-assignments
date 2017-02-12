#---------------------------------------#
2
# Assignment02
3
# [YOUR NAME HERE]
4
# [Description of what your code does]
5
# Due February 13, 2017 at 5:00pm
6
# Please remember to include "completed" in the description for your final commit
7
# Do not forget to comment your code
8
#---------------------------------------#
9
​
10
# INSTRUCTIONS
11
# Download the .zip "Assignment02.zip" and unzip to your local machine into a folder called "Assignment02."
12
​
13
# PART ONE
14
# Loop through all of the feature classes in the "Assign02_Inputs.gdb" geodatabase (provided)
15
# Run the Buffer tool on each feature class with a linear distance of 100 Meters and the name of the output feature classes
16
# should be the original feature class file name appended with "_Buf100m"
17
# Results should be saved to the "Assign02_Inputs.gdb" geodatabase
18
​
19
# PART TWO
20
# Check to see if the geodatabase "Assign02_Output.gdb" exists in your Assignment02 folder.  If the geodatabase does not exist, create it.
21
​
22
# PART THREE
23
# Use the Clip tool to clip the "MO_Highways" feature class to the "STL_CITY_Tracts_2010" feature class.  The resulting feature class should
24
# be named "STL_Highways" and should be saved in the "Assign02_Output.gdb" created in Part Two.  Use the newly created "STL_Highways" feature
25
# class as the input for the Dissolve tool with an output feature class name of "STL_Highways_ByType" and "TYPE" as the dissolve field 
26
# (do not include any additional optional parameters).  The output of the Dissolve tool should also be saved to "Assign02_Output.gdb."
27
