from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.speed = 3
robotArm.randomLevel(1,7)
# Jouw python instructies zet je vanaf hier:
for x in range(0, 9):
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        for r in range(0, x + 1):
            robotArm.moveRight()
        robotArm.drop()
        for r in range(0, x + 1):
            robotArm.moveLeft()
    elif color == "":
        break

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()