def available_four_strings():
    '''a tuple. each entry'''
    l = []
    for i in range(69):
        l.append([])
    
    ## rows
    r = 0
    iters = 0
    while r <= 5:
        c = 0
        while c <= 3:
            for i in range(4):
                l[iters].append((r,c+i))
            iters += 1
            c += 1
        r += 1
    
    ## columns
    c = 0
    while c <= 6:
        r = 0
        while r <= 2:
            for i in range(4):
                l[iters].append((r+i,c))
            iters += 1
            r += 1
        c += 1
    
    ## nw diagonals
    r = 2
    while r >= 0:
        c = 0
        while c <= 3:
            for i in range(4):
                l[iters].append((r+i,c+i))
            iters += 1
            c += 1
        r -= 1
    

    ## ne diagonals
    r = 2
    while r >= 0:
        c = 6
        while c >= 3:
            for i in range(4):
                l[iters].append((r+i,c-i))
            iters += 1
            c -= 1
        r -= 1

    return l

print available_four_strings()





the old check_four function

    def check_four(self,team):
        '''check for four in a row, rows, columns and diagonals'''
        a = np.array(4*[team],dtype=int)
   
        ## first, check rows
        for t in range(self.height):
            for r in range(self.width-3):
                if np.array_equal(self.arr[t,r:r+4],a):
 
                    return True
        ## columns         
        for r in range(self.width):
            for t in range(self.height-3):
                if np.array_equal(self.arr[t:t+4,r],a):

                    return True
        ## northwest diagonals
        for i in range(-2,4):
            length = len(self.arr.diagonal(i))
            for j in range(length-3):
                if np.array_equal(self.arr.diagonal(i)[j:j+4],a):

                    return True
        ## northeast diagonals
        b = np.fliplr(self.arr)
        for i in range(-2,4):
            length = len(b.diagonal(i))
            for j in range(length-3):
                if np.array_equal(b.diagonal(i)[j:j+4],a):
 
                    return True

        return False


    def check_move_three(self,col,team):
        list_indices = []
        for j in range(5,-1,-1):
            if self.arr[j,col] == 0:
                self.arr[j,col] = team
                list_tuples = self.check_open_three(team)
                self.arr[j,col] = 0
                if list_tuples != False:
                    #list_indices.append(list_tuples)
                    for tup in list_tuples:
                        list_indices.append(tup)
        if len(list_indices) > 0:
            return list_indices
        return False






# def better(comp,human,board):
#     l = range(board.width)
#     minmove = minimum(comp,human,board)
#     if minmove != None:
#         print 'move returned by minimum function ', minmove  
#         return minmove
#     else:      
#         newboard = copy.deepcopy(board)
#         for col in l:
#             ## if the column is full, remove it as an option
#             if board.arr[0:5,col].all() != 0:
#                 l.remove(col)
#             ## otherwise, test a move in each column, and whether it leads to a win for human player
#             else:
#                 newboard.add_move(col, comp)
#                 if newboard.check_move_win(col, human) is True:
#                     l.remove(col)
                
#         if len(l) == 1:
#             print 'move determined by better function ', l[0]
#             return l[0]
#         else: 
#             return l
    

#                 ## from the surrounders strategy function, below 'for col in dictionary_of_moves.keys():''
#                 # ## if the column is full, remove it as an option
#                 # if board.arr[0:5,col].all() != 0:
#                 #     dictionary_of_moves[col] = 0
#                 # ## otherwise, test a move in each potential column, and what its surrounders score is
#                 # else:


# def naive(comp,human,board):
#     '''this function is buggy right now and not a very good strategy anyway.
#     searches for potential threes in a row and makes a move to make them. only searches
#     for 'open threes', that is, threes that could turn into fours'''
#     print board.arr
#     potential_moves = better(comp,human,board)
#     print board.arr
#     if type(potential_moves) == int:  ## only one potential move identified in better() above
#         print 'move determined by previous function ',potential_moves
#         return potential_moves
#     else:
        
#         print 'potential moves list', potential_moves
#         newboard = copy.deepcopy(board)
#         l = potential_moves
#         for col in l:
#             ## if the column is full, remove it as an option
#             if board.arr[0:5,col].all() != 0:
#                 l.remove(col)
#             ## otherwise, test a move in each potential column, and whether it leads to a three in a row
#             else:
#                 openspots = newboard.check_move_three(col,comp)
#                 print openspots
#                 if openspots:
#                     for move in openspots:
#                         if move not in board.indices:
#                             openspots.remove(move)
#                         print openspots
#                         finalmove = random.choice(openspots)

#                         board.indices.remove(finalmove)
#                         print 'move determined to make 3'
#                         return finalmove[1]
#         print 'move determined randomly' 
#         return random.choice(l)





# ## unimplemented method in the Board class: check for three in a row

# def check_open_three(self, team):
#         '''check for three in a row'''
#         list_indices = []
#         a = np.array(3*[team],dtype=int)
#         ## first, check rows
#         for r in range(self.height):
#             for c in range(self.width-2):
#                 if np.array_equal(self.arr[r,c:c+3],a):
#                     if c == 0:
#                         ## check to the right
#                         if self.arr[r,c+5] == 0:
#                             print 'row detected'
#                             list_indices.append((r,c+5))
                            
#                     elif c == 4:
#                         ## check to the left
#                         if self.arr[r,c-1] == 0:
#                             print 'row detected'
#                             list_indices.append((r,c-1))
                            
#                     else:
#                         ## check either side
#                         if self.arr[r,c-1] == 0:
#                             print 'row detected'
#                             list_indices.append((r,c-1))
                             
#                         if self.arr[r,c+5] == 0:
#                             print 'row detected'
                            
#                             list_indices.append((r,c+5))
#                             ## columns         
#         for c in range(self.width):
#             for r in range(self.height-2):
#                 if np.array_equal(self.arr[r:r+3,c],a):
#                     if r != 0: 
                        
#                         list_indices.append((r-1,c))
                        
#         ## nw diagonals, top left open only
#         for i in range(-2,4):

#             length = len(self.arr.diagonal(i))

#             for j in range(length-3):

#                 if np.array_equal(self.arr.diagonal(i)[j+1:j+4],a):
                    
#                     if i >= 0:
#                         if self.arr[j,j+i] == 0:
#                             print 'nw diagonal deetected'
#                             list_indices.append((j,j+1)) 
#                     elif i < 0:
#                         if self.arr[-i,-i+j] == 0:
                            
#                             list_indices.append((-i,-i+j))
         
#         ## ne diagonals, top right open only
#         b = np.fliplr(self.arr)
#         for i in range(-2,4):
#             length = len(b.diagonal(i))
#             for j in range(length-3):
#                 if np.array_equal(b.diagonal(i)[j+1:j+4],a):
#                     if i >= 0:
#                         if b[j,j+i] == 0:
#                             print 'ne diagonal detected'
#                             list_indices.append((j,j+1))
#                     elif i < 0:
#                         if b[-i,-i+j] == 0 :
                            
#                             list_indices.append((-i,7-(-i+j)))
#         if len(list_indices) > 0:
#             return list_indices
#         return False