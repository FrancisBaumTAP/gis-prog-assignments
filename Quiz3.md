## Quiz 03 - 4/3/2017 - Francis Baum ##

_**1. Given the code block below that creates a dataframe 'bldg_df', provide the line of code that will display the first four rows and first three columns of 'bldg_df' in the console window. (5 pts)**_
```r
# Creates vectors with the data
bldgs <- c("Rudolph Hall","Olin Library","Simon Hall","Bauer Hall","Givens Hall","Brown Hall","Mallinckrodt Center")
year_built <- c(2004, 1960, 1985, 2014, 1931, 1936, 1971)
sq_ft <- c(34000,44500,44800,9100,12300,13400,45400)
bldg_id <- c(99,72,55,26,11,87,56)

# Combines the vectors into a data frame
bldg_df <- data.frame(bldgs,year_built,sq_ft,bldg_id)

# Insert code here
View(bldg_df[1:4,1:3])

_**2. Using the data frame 'bldg_df' from Question 1, provide a line of code that will apply the column names BldgName, YearBuilt, SqFt and BldgID to columns 1, 2, 3, and 4, respectively.**_
```r
# Insert code here
names(bldg_df) <- c("BldgName", "YearBuilt", "SqFt", "BldgID")

_**3. Provide a line of code that would result in 'NaN' displayed as the result in the console window. (5 pts)**_
```r
# Insert code here
0/0

_**4. Use the 'rgdal' package to bring in the provided "STL_Metro_Counties.shp" and plot the polygons with a fill color of your choice (not hollow). (10 pts)**_
```r
# Insert code here
path <- "C:\\Users\\LabUser\\Desktop\\Quiz03"
setwd(path)
myshp <- readOGR(dsn=".",layer="STL_Metro_Counties")
plot(myshp,col="green")
