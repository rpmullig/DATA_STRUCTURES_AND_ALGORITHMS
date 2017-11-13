#! /usr/bin/env python

import sys, time, random
import pygame

e_aplh = "abcdefghijklmnopqrstuvwxyz"
dna_alph = "ACGT"

# generate random string drawn from the given alphabet and of a given length
def gen_random_string(alphabet, length):
    a_len = len(alphabet)
    ret = ""
    for n in range(length):
        ret += alphabet[random.randint(0, a_len-1)]
    return ret

# print gen_random_string(e_aplh, 5)

SPACE_CHAR = '_'
SPACE_PENALTY = -1

# the scoring function
def s(x, y):
    if x == SPACE_CHAR or y == SPACE_CHAR:
        return SPACE_PENALTY
    elif x == y:
        return 2
    else:
        return -2

TILE_SIZE = 40
tile_color = (255, 255, 255)
highlight_color = (120, 129, 250)

def init_board(m, n):
    screen = pygame.display.set_mode(((m+2)*TILE_SIZE, (n+2)*TILE_SIZE))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Dot Board')
    pygame.font.init()
    font = pygame.font.Font(None, 15)
    return screen, font

def create_tile(font, text, color):
    tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
    tile.fill(color)
    b1 = font.render(text, 1, (0, 0, 0))
    tile.blit(b1, (TILE_SIZE/2, TILE_SIZE/2))
    return tile

def render_board(board, font, s1, s2, F):
    for i in range(len(s1)):
        tile = create_tile(font, s1[i], tile_color)
        board.blit(tile, ((i+2)*TILE_SIZE, 0))
    tile = create_tile(font, '', tile_color); board.blit(tile, (0, 0))
    tile = create_tile(font, '', tile_color); board.blit(tile, (TILE_SIZE, 0))
    for j in range(len(s2)):
        tile = create_tile(font, s2[j], tile_color)
        board.blit(tile, (0, (j+2)*TILE_SIZE))
    tile = create_tile(font, '', tile_color); board.blit(tile, (0, TILE_SIZE))
    for (x,y) in sorted(F.keys()):
        tile = create_tile(font, str(F[(x,y)]), tile_color)
        board.blit(tile, ((x+1)*TILE_SIZE, (y+1)*TILE_SIZE))
############################################################################
   
   
def seq_align(s1, s2, enable_graphics=True):
   

   # variables  
    length_1 = len(s1)+1   # since 0 is the first cell, we use this length in matrix
    length_2 = len(s2)+1
    a = s1        # call class so easily returned
    b = s2        # call class so easily returned
    best = 0           # we will have an optimal score and need to keep track
  # make a matrix array with the allocated size   
    matrix = [[0 for x in range(length_1)] for y in range(length_2)]

  # get the outer bounds of the matrix for the left
    for x in range(1, length_2):
        matrix[x][0] = x * -1
    
    for y in range(1, length_1):
        matrix[0][y] = y * -1
        

    for x in range(1, length_2):
        for y in range(1, length_1):
            #diagonal = matrix[i-1][j-1] + s(s1[i], s2[j])
            #gap_s2 = matrix[i-1][j] - SPACE_PENALTY  #right
            #gap_s1 = matrix[i][j-1] - SPACE_PENALTY  #left
            matrix[x][y] = max(
                matrix[x-1][y-1] + s(s1[y-1], s2[x-1]),
                matrix[x-1][y] + SPACE_PENALTY,
                matrix[x][y-1] + SPACE_PENALTY
                )
            
            if matrix[x][y] > best:
                best = matrix[x][y]



    current = (len(s2),len(s1))
    s1_inc = len(s1)
    s2_inc = len(s2)


    while current[0] >= 0 and current[1] >= 0:
        
        x = current[0]
        y = current[1]

        best = max(
            matrix[x][y-1],   # up
            matrix[x-1][y],   # left
            matrix[x-1][y-1]  # diag
            )


        if best == matrix[x-1][y-1]: # diag
            current = (x-1, y-1)
            s1_inc -= 1
            s2_inc -= 1

        elif best == matrix[x][y-1]: # up
            current = (x, y-1)
            s1_inc -= 1
            s2 = s2[:s2_inc] + '_' + s2[s2_inc:]

        elif best == matrix[x-1][y]: # left
            current = (x-1, y)
            s2_inc -= 1
            s1 = s1[:s1_inc] + '_' + s1[s1_inc:]

#    F = [(x,y) for x in s1 for y in s2]

 #   if enable_graphics:
  #      render_board(init_board(length_1, length_2), "garamond", s1, s2, F)
   #     pygame.display.flip()
    #    time.sleep(2)
            

    return s1, s2


        # a.addSpace(i)  add a space if down
        # b.addSpace(i)  add a space if right
        # string = string[:i] + '_' + string[i:]
        # matrix[i][j] = max(diag, down, right)
############################################################################

if len(sys.argv) == 2 and sys.argv[1] == 'test':
    f=open('tests.txt', 'r');tests= eval(f.read());f.close()
    cnt = 0; passed = True
    for ((s1, s2), (a1, a2)) in tests:
        (ret_a1, ret_a2) = seq_align(s1, s2, False)
        if (ret_a1 != a1) or (ret_a2 != a2):
            print("test#" + str(cnt) + " failed...")
            passed = False
        cnt += 1
    if passed: print("All tests passed!")
elif len(sys.argv) == 2 and sys.argv[1] == 'gentests':
    tests = []
    for n in range(25):
        m = random.randint(8, 70); n = random.randint(8, 70)
        (s1, s2) = (gen_random_string(dna_alph, m), gen_random_string(dna_alph, n))
        (a1, a2) = seq_align(s1, s2, False)
        tests.append(((s1, s2), (a1, a2)))
    f=open('tests.txt', 'w');f.write(str(tests));f.close()
else:
    l = [('ACACACTA', 'AGCACACA'), ('IMISSMISSISSIPI', 'MYMISSISAHIPPIE')]
    enable_graphics = True
    if enable_graphics: pygame.init()
    for (s1, s2) in l:
        print ('sequences:')
        print (s1, s2)
        
        m = len(s1)
        n = len(s2)
        
        print ('alignment: ')
        print (seq_align(s1, s2, enable_graphics))

    if enable_graphics: pygame.quit()




  #  score = 0
  #  d = {}
  #  dictionary =  map(lambda a, b: d.update({a, b}), s1, s2)
