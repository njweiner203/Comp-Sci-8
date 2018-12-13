import pyautogui as pg
import webbrowser as wb
import time as t
 
points = 0

show = pg.prompt("what is your favorite show? ")

if show == "The Office":
    wb.open("https://www.youtube.com/watch?v=YId_6G-YLpQ")
    t.sleep(10)
    pg.alert("Michael SCARN!")
    points += 1
elif show == "The Flash":
    wb.open("https://www.youtube.com/watch?v=bRCy8dOknoM")
    t.sleep(10)
    points += 1
    pg.alert("Sooooooo Gooood!")
elif show == "riverdale":
    pg.alert("WOW")

elif show == "the lazerbeam show":
    wb.open("https://www.youtube.com/watch?v=IfVLAzo84Co")
    t.sleep(10)
    points += 1
    pg.alert("giday giday")
elif show == "Blue mountain state":
    pg.alert("funny")
elif show == "troydan show":
    wb.open("https://www.google.com/search?q=troydan&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiQ_obC6bPeAhVG2VMKHWYDBrEQ_AUIDygC&biw=1152&bih=403#imgrc=S8UF1N0Q0aNDoM:")
    pg.alert("so good")
else:
    pg.alert("your favorite show is " + show)




game = pg.prompt("what is your favorite game? ")
if game == "Fortnite":
    wb.open("https://www.google.com/search?q=fortnite&rlz=1C1GCEA_enUS752US761&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiaibjr6bPeAhURy1MKHf7UAvgQ_AUIECgD&biw=1152&bih=403#imgrc=-TbjN9jxnuRdFM:")
    pg.alert("The Rex is Amazing")
    points += 1
elif game == "NBA 2K":
    wb.open("https://www.youtube.com/watch?v=d0W5MhoOoQY")
    t.sleep(10)
    pg.alert("Donovan is cheese in that game")
    points += 1

elif game == "pubG":
    pg.alert("Booooooo")

elif game == "NBA Playgrounds":
    wb.open("https://www.youtube.com/watch?v=C3qYh5MjqbU")
    t.sleep(10)
    pg.alert("Sure")
    wb.open("https://www.youtube.com/watch?v=WOv-yJK23DM")
    t.sleep(10)
elif game == "fifa":
    pg.alert("really good")
elif game == "H1Z1":
    pg.alert("OK SURE")

else:
    pg.alert ("your favorite game is trash")


team = pg.prompt("what is your favorite basketball team")
if team == "New York Knicks":
    wb.open("https://www.youtube.com/watch?v=0g2X4afNbgY")
    t.sleep(10)
    pg.alert("Go Knicks")
    points += 100
elif team == "Warriors":
    wb.open("https://www.youtube.com/watch?v=P2884ydbYb4")
    t.sleep(10)
    pg.alert("banwagon")
    points -= 3
elif team == "Jazz":
    wb.open("https://www.youtube.com/watch?v=PJBbl7N9BQc")
    t.sleep(10)
    pg.alert("SPIDA for MVP")
    points += 23
elif team == "Cavs":
    wb.open("https://www.youtube.com/watch?v=Cj_4DupKfuk")
    t.sleep(10)
    pg.alert("wheres LeBron")
elif team == "Lakers":
    pg.alert("Meam team")
elif team == "Heat":
    pg.alert("Wade Country")
    points += 12
else:
    pg.alert ("Your favorite team is bad")


food = pg.prompt("what is your favorite food? ")

if food == "Felet Mingon":
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US761&tbm=isch&q=filet+mignon&chips=q:filet+mignon,g_1:steak:vciT7aPqJ9c%3D&usg=AI4_-kRKLFWn2xzuzISJNPkIRGJwlTqsVg&sa=X&ved=0ahUKEwjJwo-37LPeAhWOmOAKHW1IDdsQ4lYIKSgB&biw=1152&bih=403&dpr=1")
    pg.alert("sooo good")
    points += 1
elif food == "pizza":
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US761&biw=1152&bih=403&tbm=isch&sa=1&ei=BknbW-H6LdKJggfTmZQI&q=pizza&oq=pizza&gs_l=img.3..0i67j0l2j0i67j0l6.64107.65238..66828...0.0..0.63.257.5......0....1..gws-wiz-img.ckj6DZQuNZ0")
    pg.alert("Sooooooo Gooood!")
    points += 1
elif food == "pasta":
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US761&biw=1152&bih=403&tbm=isch&sa=1&ei=SknbW_XnFOPF_QaxrLbYCg&q=pasta&oq=pasta&gs_l=img.3..0i67j0l3j0i67l2j0l3j0i67.33754.34939..35616...0.0..0.53.241.5......0....1..gws-wiz-img.rS-6URxqwHc")
    pg.alert("WOW")
    points += 1
elif food == "tacos":
    pg.alert("yessss")
elif food == "hamburger":
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US761&biw=1152&bih=403&tbm=isch&sa=1&ei=bknbW4mTJYmxggfEkIiIBg&q=hamburger&oq=hambu&gs_l=img.1.0.0i67j0j0i67j0l7.38753.39993..41513...0.0..0.67.290.5......0....1..gws-wiz-img.Q0vKqHFewTo")
    pg.alert("YUM")
elif food == "Fries":
    pg.alert("yum")
else:
    pg.alert("your favorite food is " + food)

sport = pg.prompt("what is your favorite sport? ")

if sport == "basketball":
    wb.open("https://www.youtube.com/watch?v=xkOhIjAW1cg")
    t.sleep(2)
    pg.alert("best sport!")
    points += 100
elif sport == "football":
    wb.open("https://www.youtube.com/watch?v=xqmbQ5XEGPM")
    t.sleep(10)
    pg.alert("Sooooooo Gooood!")
    points += 110
elif sport == "soccer":
    wb.open("https://www.youtube.com/watch?v=i0rymXLIjuM")
    t.sleep(10)
    pg.alert("Why?")
    points -= 13
elif sport == "baseball":
    wb.open("https://www.youtube.com/watch?v=xiXJxHYfrbk")
    t.sleep(10)
    pg.alert("americans pastime")
elif sport == "LAX":
    pg.alert("FUN")
    points -= 12
elif sport == "hockey":
    pg.alert("decent")

else:
    pg.alert("your favorite sport is " + sport)

pg.alert(points)
