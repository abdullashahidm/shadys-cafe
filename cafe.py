import random
import sound
from rapidfuzz import fuzz,process
import time
import re

def main():
    sound.start_music()
    greet()
    newline()
    _=input("Hit enter to go inside ")
    menu()
    final,price=order()
    newline()
    print("Getting order ready...")
    newline()
    time.sleep(3)
    serve()
    time.sleep(1)
    _=input("When you've eaten, press enter ")
    newline()
    slip(final,price)
    newline()
    _=input("Hit enter to pay ")
    newline()
    print(f"Recieved payment: --${price}--")
    time.sleep(1)
    newline()
    print("Thank you for coming! Come again soon")
    time.sleep(1)

def greet():
    cafe="""
            ~ ~ ~      ☀      ~ ~ ~
          __|__|__|__|__|__|__|__|__|
         |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ |
         |   🍷   🍇   🍷   🍇       |      
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
    return (summ(items))
    
def summ(order):  #summarize
    price=0
    valid=["biryani","pizza","lasagna","ice cream","mac n cheese","ice cream shake"]
    prices={"biryani":3.5,"pizza":11,"lasagna":6,"ice cream":3,"mac n cheese":2.5,"ice cream shake":6}
    rm=0
    final=[]
    removed=[]
    for d in order: #dish
        qty,txt=gq(d)
        best,score,_=process.extractOne(d,valid,scorer=fuzz.WRatio)
        if score>70:
            if qty>0:
                final.append(f"{qty} {best.capitalize()}")
                price+=prices[best]*qty
        else:
            rm+=1
            removed.append(d)
    if removed:
        print(f"{rm} request(s) are/isn't on the menu, so they were removed:")
        for _ in removed:
            print(_.capitalize())
        newline()
    return final,price
  
def serve():
    tray="""
              .-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
          |            DINNER TABLE               |
.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
|       ( )      ( )      ( )      ( )      ( )         |
|      (___)    (___)    (___)    (___)    (___)        |
|       | |      | |      | |      | |      | |         |
|       | |      | |      | |      | |      | |         |
|        \        \        \        \        \          |
|         \________\________\________\________\         |
|        ---      ---      ---      ---      ---        |
|       (___)    (___)    (___)    (___)    (___)       |
|        / \      / \      / \      / \      / \        |
|       /___\    /___\    /___\    /___\    /___\       |
|                                                     🍷 |
`-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
    """
    print(tray)
    
def slip(o,p): #order
    print("+--------------------+")
    print("|     ITEM BILL      |")
    print("----------------------")
    print("|                    |")
    for e in o:
        print(f"|>{e}")
        print("|                    |")
    print(f"|TOTAL: ${p}")
    print("+--------------------+")
   
def gq(txt): #get quantity
    wTn={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10} #word to number
    match=re.match(r"(\d+)\s+(.*)",txt)
    if match:
        qty=int(match.group(1))
        name=match.group(2)
    else:
        qty=1
        name=txt
    if qty>10:
        newline()
        print(f"About the {name}... O_O. That won't be possible, sir. (Or madam).")
        qty=0
        time.sleep(2)
    return qty,name
             
if __name__=="__main__":
    main()
