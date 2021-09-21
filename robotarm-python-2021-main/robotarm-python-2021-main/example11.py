from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:
for y in range(0, 9):
    robotArm.moveRight()
for x in range(0, 10):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft()
    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()