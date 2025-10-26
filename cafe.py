import random
import sound
from rapidfuzz import fuzz,process

class Visit:
    def __init__(self):
        ...

def main():
    sound.start_music()
    greet()
    newline()
    _=input("Hit enter to go inside ")
    menu()
    final=order()
    serve(final)

def greet():
    cafe="""
            ~ ~ ~      ☀      ~ ~ ~
          __|__|__|__|__|__|__|__|__|
         |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ |
         |   🍷   🍇   🍷   🍇   |      
         |   [▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒]    |
         |   [▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒]    |
         |   [▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒]    |
         |___________││______________|
         |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
         |   ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲   |   
        _|____     ___()___     ____|_
       |  ___|   _|_______|_   |___  |
       | |___|  |___________|  |___| |
       |    /       ___       \      |
       |   /       (___)       \     |   
      /|_____________________________|\ 
     /_|_____________________________|_\
         
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~       ~~~~~~~~~~~
            
    """
    print(cafe)
    print("          Welcome to Shady's Café!")
    
def newline():
    print('')
    
def menu():
    menu="""
       ╔══════════════════════════════════╗
   ║         ✿  C A F É   S H A D Y  ✿        ║
   ║──────────────────────────────────++++++++║
   ║    Item                          Price   ║
   ╠══════════════════════════════════╣       ║
   ║  Biryani ................... $3.50/plate ║
   ║  Pizza (Neo) .............. $11.00/whole ║
   ║  Lasagna ................... $6.00/plate ║
   ║  Ice Cream ................. $3.00/scoop ║
   ║  Mac n’ Cheese ............ $2.50/plate  ║
   ║  Ice Cream Shake .......... $6.00/cup    ║
   ║                                          ║
       ╚══════════════════════════════════╝
    """
    print(menu)
    newline()
    print("What will you order today? ")
    
def order():
    phrases=["Got that.", "Okay.", "Noted.", "Good choice!", "Nice!"]
    negating=["n","no","nah","nope","no, thank you","no thanks","nah, I’m good","no, thanks","no thank you"]
    items=[]
    item=input().strip()
    items.append(item)
    while True:
        print(f"{random.choice(phrases)} Anything else?")
        reply=input().lower().strip()
        if reply in [n.lower() for n in negating]:
            break
        elif reply in ("y", "yes", "uh huh"):
            print("What else, amico mio?")
            nitem=input().strip()
            items.append(nitem)
        elif reply=="":
            break
        else:
            items.append(reply)
    print(summ(items))
    
def summ(order):  #summarize
    valid=["biryani","pizza","lasagna","ice cream","mac n cheese","ice cream shake"]
    rm=0
    final=[]
    removed=[]
    for d in order: #dish
        best,score,_=process.extractOne(d,valid,scorer=fuzz.WRatio)
        if score>70:
            final.append(best)
        else:
            rm+=1
            removed.append(d)
    if removed:
        newline()
        print(f"{rm} request(s) are/isn't on the menu, so they were removed:")
        print(*removed)
    return final
  
def serve(final):
    biryani="""
    """
    lasagna="""
    """
    icecream="""
    """
    shake="""
    """
    mac="""
    """
    pizza="""
    """
      
if __name__=="__main__":
    main()
