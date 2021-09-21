from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:

for x in range(0, 9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for r in range(x, 9):
            robotArm.moveRight()
        robotArm.drop()
        for c in range(x, 9):
            robotArm.moveLeft()
        robotArm.moveRight()
    else:
        robotArm.drop()
        robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()