import tkinter
import random
import turtle
import time

class Simon() :
    '''
    This class makes the game board for the Simon Memory Game. 
    The only thing you need to pass into the class is tkinter.Tk(). 
    Currently this class does not have the function of clicking the game board
    due to syntax errors with object binding. 
    Also the idea of the "show_sequence" and "flash_color" functions came from an outside source cited below.
    
    To do: Fix onclick handler method for the rectangles.
    
    '''
    def __init__ (self, seed):
        '''
        Method creates canvas for the squares to be built.
        Also defines lists and variables to maintain little amount of magic numbers.
        '''
        self.sequence = [1,2,3,4,1]
        self.guesses = []
        self.sequence_position = 0
        self.score = 0
        self.number_of_clicks = 0
        
        self.quadrant_border = 300
        self.canvas_size = 600
        
        self.Square_Colors = { 1: 'red', 2: 'blue', 3 : 'green', 4 : 'yellow'}
        self.Current_Colors = { 1: 'red', 2: 'blue', 3 : 'green', 4 : 'yellow'}
        self.Flashing_color = 'black'
        
        self.seed = seed
        self.seed.title("Ryan's Memory Game")
        self.seed.geometry("1000x1000")
        self.game_canvas = tkinter.Canvas(self.seed, 
                                          height=self.canvas_size, 
                                          width=self.canvas_size,)
        self.game_canvas.pack()
        
        #Body using function starts
        self.Draw_Lights()
        self.show_sequence()
        self.click_on_box()
        self.seed.mainloop()
        
    def Draw_Lights(self):
        #Makes all squares using coordinates defined above.
        self.quadrant_1=self.game_canvas.create_rectangle(0, 0, 
                                                          self.quadrant_border, 
                                                          self.quadrant_border, 
                                                          fill=self.Current_Colors[1])
        
        self.quadrant_2=self.game_canvas.create_rectangle(self.quadrant_border,
                                                          self.quadrant_border,
                                                          self.canvas_size,
                                                          self.canvas_size,
                                                          fill=self.Current_Colors[2])
        
        self.quadrant_3=self.game_canvas.create_rectangle( self.quadrant_border,
                                                          0,
                                                          self.canvas_size,
                                                          self.quadrant_border,
                                                          fill=self.Current_Colors[3])
        
        self.quadrant_4=self.game_canvas.create_rectangle(0,
                                                          self.quadrant_border,
                                                          self.quadrant_border,
                                                          self.canvas_size,
                                                          fill=self.Current_Colors[4])
        
        
    def show_sequence(self):
        '''
        Function was modeled after code from "https://github.com/MrJHBauer/Simon/blob/master/Simon.py".
        This function was originally supposed to iterate over each number within the sequence,
        then pass the number into the flash_color function.
        However the functions "time.sleep" and "seed.after" would delay the time of the application opening,
        instead of delaying when the flashing would start.
        This successfully worked,
        because previously the seed.after did not call a function, only passed some time.
        This gives another way to check each item in the tuple without iterating it.
        '''
        self.flash_color(self.sequence[self.sequence_position])
        if(self.sequence_position < len(self.sequence) - 1):
            self.sequence_position += 1
            self.seed.after(1200, self.show_sequence)
        else:
            self.sequence_position = 0
        
        
    def flash_color(self, color):
        '''
        This function was based off code from the link above in the doc strings for show_sequences.
        While writing this function, the same problem from above arose.
        I had to adapt another way of "flashing a color",
        instead of setting the object to a color, setting a time, then setting the color back.
        When I tried to do the method of changing the color, setting a time, then setting it back,
        the squares would not appear, even though the function "Draw_Lights" were there.
        '''
        index_color = self.Square_Colors[color]
        if index_color == self.Current_Colors[color]:
            self.Current_Colors[color] = "black"
            self.seed.after(1000, self.flash_color, color)
        else:
            self.Current_Colors[color] = self.Square_Colors[color]
        self.Draw_Lights()
    
    
    def click_on_box(self):
        '''
        To Do:
        Fix binding and bind each object to function with proper argument passed in.
        No Arguments to pass into method.
        '''
        self.game_canvas.tag_bind( self.quadrant_1, '<Button-1>', self.check_sequence(1))
        self.game_canvas.tag_bind( self.quadrant_2, '<Button-1>', self.check_sequence(2))
        self.game_canvas.tag_bind( self.quadrant_3, '<Button-1>', self.check_sequence(3))
        self.game_canvas.tag_bind( self.quadrant_4, '<Button-1>', self.check_sequence(4))
        
        
    def check_sequence(self, click_color):
        '''
        Must fix method above for this method to work.
        Currently prints clicked four times, meaning the above method calls
        this method with the argument shown above.
        Does not raise any errors currently.
        '''
        self.number_of_clicks += 1
        #Checks if color clicked is color in sequence.
        if click_color == self.sequence[self.number_of_clicks - 1]:
            #Checks length of clicked is same as sequence
            if len(self.sequence) == len(self.guesses):
                self.sequence.append(random.randrange(1,5))
                self.score += 1
                self.guesses.append(click_color)
                self.show_sequence
                print("clicked")
            #If not done clicking sequence, allows more clicks and checks if it's clicked.
            else:
                self.guesses.append(click_color)
                print("clicked")
        #Clicked wrong tile and ends game.
        else:
            self.seed.title(
                "Game Over Score: {} Please Close And Restart Program For Next Game".format(self.score))
            
            

        
        
        
        
       