def showTreasure():
    global x, y, treasure_x, treasure_y
    led.plot(treasure_x, treasure_y)
    x = arr[0] % 5
    y = int(arr[0] / 5)
    if x == treasure_x and y == treasure_y:
        arr.append(arr[0])
        treasure_x = randint(0, 4)
        treasure_y = randint(0, 4)
def moveForward():
    global x1, y1
    basic.pause(wait)
    x1 = arr[0] % 5
    y1 = int(arr[0] / 5)
    if x1 + x_add < 0:
        x1 = 4
    else:
        x1 = (x1 + x_add) % 5
    if y1 + y_add < 0:
        y1 = 4
    else:
        y1 = (y1 + y_add) % 5
    arr.insert_at(0, x1 + y1 * 5)
    arr.remove_at(len(arr) - 1)
def generateImage():
    global x, y
    basic.clear_screen()
    i = 0
    while i <= len(arr) - 1:
        x = arr[i] % 5
        y = int(arr[i] / 5)
        led.plot(x, y)
        i += 1
x_add = 0
y1 = 0
x1 = 0
y = 0
x = 0
arr: List[number] = []
wait = 0
y_add = 0
treasure_y = 0
treasure_x = 0
treasure_x = randint(0, 4)
treasure_y = randint(0, 4)
y_add = 1
wait = 200
arr = [0]
bluetooth.start_uart_service()

def on_forever():
    showTreasure()
basic.forever(on_forever)

def on_forever2():
    generateImage()
    moveForward()
basic.forever(on_forever2)

def on_button_pressed_a():
    global x_add, y_add
    if x_add == 0 and y_add == -1:
        x_add = -1
        y_add = 0
    elif x_add == 0 and y_add == 1:
        x_add = 1
        y_add = 0
    elif x_add == 1 and y_add == 0:
        x_add = 0
        y_add = -1
    else:
        x_add = 0
        y_add = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x_add, y_add
    if x_add == 0 and y_add == -1:
        x_add = 1
        y_add = 0
    elif x_add == 0 and y_add == 1:
        x_add = -1
        y_add = 0
    elif x_add == 1 and y_add == 0:
        x_add = 0
        y_add = 1
    else:
        x_add = 0
        y_add = -1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    global arr
    arr = [0]
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_bluetooth_connected():
    basic.show_icon(IconNames.HAPPY)
    music._play_default_background(music.built_in_playable_melody(Melodies.NYAN),
        music.PlaybackMode.IN_BACKGROUND)
    basic.pause(2000)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.SAD)
    basic.pause(2000)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_uart_data_received():
    global x_add, y_add
    if x_add == 0:
        x_add = -1
        y_add = 0
    elif y_add == 0:
        x_add = 0
        y_add = -1
bluetooth.on_uart_data_received("A", on_uart_data_received)

def on_uart_data_received2():
    global x_add, y_add
    if x_add == 0:
        x_add = 1
        y_add = 0
    elif y_add == 0:
        x_add = 0
        y_add = 1
bluetooth.on_uart_data_received("B", on_uart_data_received2)
