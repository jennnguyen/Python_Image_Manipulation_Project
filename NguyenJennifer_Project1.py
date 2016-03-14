# CST 205 Project 1
# Jennifer Nguyen

pictures = []  #Creates lists to hold pictures and Red, Green, Blue values
redList = [] 
greenList = []
blueList = []

for im in range(1,10):   #Adds nine pictures to a list
  imagePath = 'C:/Users/Jennifer/Desktop/CST205Proj1/Images/' + str(im) + '.png'
  pictures.append(makePicture(imagePath))
#Dallas reference 
   
width = getWidth(pictures[1])
height = getHeight(pictures[1])
newImage = makeEmptyPicture(width, height)  #Creating new empty picture

for x in range(0, width):
  for y in range(0, height):
    for images in range(0, 9):    
      pixel = getPixel(pictures[images], x, y)      #Adds pixels to lists
      redList.append(getRed(pixel))
      greenList.append(getGreen(pixel))
      blueList.append(getBlue(pixel))
      
    sortRed = sorted(redList)  #Sorts the list values
    sortGreen = sorted(greenList)      
    sortBlue = sorted(blueList)
    
    medianRed = sortRed[(len(sortRed)+1)/2]    #Chooses the median values
    medianGreen = sortGreen[(len(sortGreen)+1)/2]
    medianBlue = sortBlue[(len(sortBlue)+1)/2]
    
    
    newColor = makeColor(medianRed, medianGreen, medianBlue) #Creates and sets the new colors in the new empty picture
    setColor(getPixel(newImage, x, y), newColor)
    
    redList = [] #Resets list
    greenList = []
    blueList = []
    
show(newImage)        
