def roboReturn(moves):
    xPos = 0
    yPos = 0
    for i in moves:
        if(i =="U"):
            yPos+=1
        elif(i=="D"):
            yPos =yPos-1
        elif(i=="R"):
            xPos+=1
        elif(i=="L"):
            xPos-=1
    print(xPos, " , ", yPos)
    if(xPos+yPos!=0):
        return(False)
    else:
        return(True)
    
def returnAdv(moves):
    if(moves.count("D")!= moves.count("D") ):
        return(False)
    elif(moves.count("R")!= moves.count("L")):
        return(False)
    else:
        return(True)
    
if __name__ == '__main__':
    moves = ["U","D"]
    # Function call
    print("Output: ",returnAdv(moves))
