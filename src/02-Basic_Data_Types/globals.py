
def OutputRocketText():
    rocketNumber = 1
    print("Rocket will launch soon!")

    return
OutputRocketText()
print(rocketNumber) # getting error


rocketText = "We will launch in"
def OutputRocketText():
    rocketText = rocketText + " two days" # getting error
    return
OutputRocketText()


rocketText = "We will launch in"
def OutputRocketText():
    global rocketText
    rocketText = rocketText + " two days"
    return
OutputRocketText()
print(rocketText)


#better approach is to use variables pass arguments
def OutputRocketText(textInput):
    textInput = textInput + " two days"
    return textInput
rocketText = "We will launch in"
newRocketText = OutputRocketText(rocketText)
print(newRocketText)