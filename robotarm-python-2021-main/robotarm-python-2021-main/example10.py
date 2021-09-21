from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 1
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:


for x in range(9, 0, -2):
    robotArm.grab()
    for d in range(0, x):
        robotArm.moveRight()
    robotArm.drop()
    x = x - 1
    for y in range(0, x):
        robotArm.moveLeft()
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()