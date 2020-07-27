from IPython.display import clear_output


def board(c=[' ',' ',' ',' ',' ',' ',' ',' ',' ']):
    clear_output()
    print('   |   |   \n')
    print(' {} | {} | {} \n'.format(c[0],c[1],c[2]))
    print('   |   |   \n')
    print('___________')
    print('   |   |   \n')
    print(' {} | {} | {} \n'.format(c[3],c[4],c[5]))
    print('   |   |   \n')
    print('___________')
    print('   |   |   \n')
    print(' {} | {} | {} \n'.format(c[6],c[7],c[8]))
    print('   |   |   \n')
def assign_c(c,x,i):
    if i=='1':
        c[int(x)-1]='X'
    else:
        c[int(x)-1]='O'
    return c
    
def args(i,c):
   
    if i=='1':
        x=input("Player 1 please choose where to put X between 1 to 9 : ")
        if c[int(x)-1]==' ':
            c=assign_c(c,x,'1')
        else: 
            print("The position is already taken")
            args(1)
        board(c)
    if i=='2':
        y=input("Player 2 please choose where to put O between 1 to 9 : ")
        if c[int(y)-1]==' ':
            c=assign_c(c,y,'2')
        else:
            print("The position is already taken")
        board(c)
    return c
def toggle_i(i):
    if i=='1':
        return '2'
    if i=='2':
        return '1'
def result(c,player_x):
    if c[0]==c[1] and c[1]==c[2] and c[0]!=' ':
        if c[0]=='X':
            return(player_x)
        if c[0]=='O':
            return(int(toggle_i(player_x))) 
    if c[0]==c[4] and c[4]==c[8] and c[0]!=' ':
        if c[0]=='X':
            return(player_x)
        if c[0]=='O':
            return(int(toggle_i(player_x))) 
    if c[2]==c[4] and c[4]==c[6] and c[2]!=' ':
        if c[2]=='X':
            return(player_x)
        if c[2]=='O':
            return(int(toggle_i(player_x)))  
    if c[2]==c[5] and c[5]==c[8] and c[2]!=' ':
        if c[2]=='X':
            return(player_x)
        if c[2]=='O':
            return(int(toggle_i(player_x))) 
    if c[1]==c[4] and c[4]==c[7] and c[1]!=' ':
        if c[1]=='X':
            return(player_x)
        if c[1]=='O':
            return(int(toggle_i(player_x))) 
    if c[0]==c[3] and c[3]==c[6] and c[0]!=' ':
        if c[0]=='X':
            return(player_x)
        if c[0]=='O':
            return(int(toggle_i(player_x))) 
    if c[3]==c[4] and c[4]==c[5] and c[3]!=' ':
        if c[3]=='X':
            return(player_x)
        if c[3]=='O':
            return(int(toggle_i(player_x))) 
    if c[6]==c[7] and c[7]==c[8] and c[6]!=' ':
        if c[6]=='X':
            return(player_x)
        if c[6]=='O':
            return(int(toggle_i(player_x)))  
    else:
        if ' ' in c:
            return "continue"
        else:
            return "draw"
        
        

c=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
i='1'
z=input("Player 1, Choose X or O : ")
if z.upper()=='X':
    player_x='1'
    print("Great, you start first")
else:
    player_x='2'
    print("Player 2 starts first")
while(result(c,player_x)=="continue"):
    c=args(i,c)
    i=toggle_i(i)
print("Game Over")
r=result(c,player_x)
if r!="draw":
    print("Congratulations Player {} won".format(r))
else:
    print("Game is Draw!")
    