import LowLevelRequest
import time
import serial
import cv

#open port and wait for connection
port = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
time.sleep(2)
#set state to program 2
port.write("P2\n")

#create request object
print "creating a request object"
request = LowLevelRequest.LowLevelRequest()

print "creating cv object"
pic = cv.CV()
object = pic.get_all_objects()

ball = object[0]
objectColor = ball[0]
objectDistance = ball[1]

print "color: " + str(objectColor) + " objectDistance: " + str(objectDistance)

#if it's purple, stop far enough away to put the arm down and push
if objectColor == "Purple":
    distance = .8
else:
    distance = .4

#move forward until the robot is at the object
while objectDistance > distance:
    request.movement = "Forward"
    message = request.giveMessage()
    print "sending " + message
    port.write(message)
    port.write(message)
    time.sleep(.5)
    object = pic.get_all_objects()
    ball = object[0]
    objectDistance = ball[1]
    print "color: " + str(objectColor) + " objectDistance: " + str(objectDistance)


#stop moving and lower the servo arm... wait a bit to give it time to happen
print "stop moving... lower arm"
request.movement = "NoMovement"
request.servo = "Down"
port.write(request.giveMessage())
time.sleep(1)

#perform action
if objectColor == "orange":
    #turn left 45 degrees
    request.wheelTurn = "Left"
    request.turnDegrees = 45
    port.write(request.giveMessage())
elif objectColor == "green":
    #turn right 45 degrees
    print "pushing right"
    request.wheelTurn = "Right"
    request.turnDegrees = 45
    port.write(request.giveMessage())
elif objectColor == "purple":
    #move forward 10 times
    request.movement = "Forward"
    for i in range(0, 10):
        port.write(request.giveMessage())
elif objectColor == "yellow":
    #move backward 10 times
    request.movement = "Backward"
    for i in range(0, 10):
        port.write(request.giveMessage())
else:
    print "unidentified color"

request.movement = "NoMovement"
request.wheelTurn = "NoTurn"
request.servo = "Up"

port.write(request.giveMessage())