... implement a class called players that represent a cricket player the player class should have a 
method called play{}watch print *the playing cricket.derive two classes.batsman and Bowler.
bowler, from teh player class.override the play()method in each derived class to print *the batsman 
is playing cricket.batsman, from the player class.override the play()method in each derived class to 
print *the bowler is playing cricket.


#define the base class name:
class player:
  def play(self):
    print("the player is playing cricket")
    
#define the cricket class batsman:
class batsman(player):
  def play(self):
    print("the batsman is playing cricket")
    
#define the cricket class bowler:
class bowler(player):
  def play(self):
    print("the bowler is boiling.*)

        #create object of batsman and bowler classes
          batsman=batsman()
          bowler=bowler()

          #call the play()class method
batsmen.play()
bowler.play()

          

          



      
