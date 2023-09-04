# write your code here
def padel_court_cost(court_type):
    if court_type == "indoor":
        return(30)
    if court_type == "outdoor":
        return(20)
def rackets_cost(racket_brand):
    if racket_brand == "bullpadel":
        return(100)
    if racket_brand == "nox":
        return(140)
    if racket_brand == "siux":
        return(200)
def padel_balls_cost(ball_boxes):
    if ball_boxes==1:
        return(2)
    elif ball_boxes==2:
        return(3.5)
    elif ball_boxes==3:
        return(5)
def padel_game_cost():
 padel_court_cost=input("enter the court track")
 rackets_cost=input("enter the racket brand")
 padel_balls_cost=int(input("enter the number of ball boxes"))
 result=(padel_court_cost + rackets_cost + padel_game_cost)
 return result
padel_court_cost
rackets_cost
padel_balls_cost
print(padel_game_cost)
