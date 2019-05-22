import arcpy,os,sys,string,fnmatch
import arcpy.mapping
from arcpy import env

rootPath = 'C:\\Users\\JGardner\\Desktop\\Need to Merge'
counter = 0
matches = []

for root, dirs, files in os.walk(rootPath):
    for filename in files:
        if ".shp" in filename:
            match = ( os.path.join(root, filename))
            matches.append (match)
            counter = counter + 1
            print(filename)
      
arcpy.Merge_management(matches, r"C:\\Users\\JGardner\\Desktop\\Merged\\All boundaries merged.shp")
