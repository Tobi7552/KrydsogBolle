import os
os.system('clear')

class Board():
    def __init__(self):
        self.cells = ['0','1','2','3','4','5','6','7','8','9']
        
    def display(self):
        print('------------')
        print('| %s | %s | %s|' %(self.cells[1], self.cells[2], self.cells[3]))
        print('------------')
        print('| %s | %s | %s|' %(self.cells[4], self.cells[5], self.cells[6]))
        print('------------')
        print('| %s | %s | %s|' %(self.cells[7], self.cells[8], self.cells[9]))
        print('------------')
    
    
    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == str(cell_no):
            self.cells[cell_no] = player
            
        

    def winner(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True
        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True

    def reset(self):
        self.cells = ['0','1','2','3','4','5','6','7','8','9']        
    
    def uafgjort(self):
        count = 0
        for cell in self.cells:
            if cell == 'O' or cell == 'X':
                count += 1
        if count == 9:
            return True
        else:
            return False           
    
board = Board()

def refresh_screen():
    os.system('clear')
    board.display()

while True:
   refresh_screen()

   x_valg = int(input('\nX) Vælg et tal mellen 1-9 >'))


   board.update_cell(x_valg, 'X')



   refresh_screen()
   
   if board.uafgjort():
    print('\n Uafgjort!\n')
    spil_igen = input('Vil du spille igen? (Y/N) > ').upper()
    if spil_igen == 'N':
        break
    else:
        board.reset()
        continue
        

   if board.winner('X'):
    print('\nX vinder!\n')
    spil_igen = input('Vil du spille igen? (Y/N) > ').upper()
    if spil_igen == 'N':
        break
    else:
        board.reset()
        continue
   
        
    refresh_screen()      
   
   o_valg = int(input('\nO) Vælg et tal mellen 1-9 >'))

   board.update_cell(o_valg, 'O')
   
   if board.winner('O'):
    print('\nO vinder!\n')
    spil_igen = input('Vil du spille igen? (Y/N) > ').upper()
    if spil_igen == 'N':
        break
    else:
        board.reset()
        continue   


    


   
   
   