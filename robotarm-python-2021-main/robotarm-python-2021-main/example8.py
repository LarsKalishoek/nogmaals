from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')


# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for z in range(0, 7):
    robotArm.grab()
    for x in range(0, 9):
        robotArm.moveRight()
    robotArm.drop()
    for y in range (1, 9):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()