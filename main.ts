function showTreasure() {
    
    led.plot(treasure_x, treasure_y)
    x = arr[0] % 5
    y = Math.trunc(arr[0] / 5)
    if (x == treasure_x && y == treasure_y) {
        arr.push(arr[0])
        treasure_x = randint(0, 4)
        treasure_y = randint(0, 4)
    }
    
}

function moveForward() {
    
    basic.pause(wait)
    x1 = arr[0] % 5
    y1 = Math.trunc(arr[0] / 5)
    if (x1 + x_add < 0) {
        x1 = 4
    } else {
        x1 = (x1 + x_add) % 5
    }
    
    if (y1 + y_add < 0) {
        y1 = 4
    } else {
        y1 = (y1 + y_add) % 5
    }
    
    arr.insertAt(0, x1 + y1 * 5)
    arr.removeAt(arr.length - 1)
}

function generateImage() {
    
    basic.clearScreen()
    let i = 0
    while (i <= arr.length - 1) {
        x = arr[i] % 5
        y = Math.trunc(arr[i] / 5)
        led.plot(x, y)
        i += 1
    }
}

let x_add = 0
let y1 = 0
let x1 = 0
let y = 0
let x = 0
let arr : number[] = []
let wait = 0
let y_add = 0
let treasure_y = 0
let treasure_x = 0
treasure_x = randint(0, 4)
treasure_y = randint(0, 4)
y_add = 1
wait = 200
arr = [0]
bluetooth.startUartService()
basic.forever(function on_forever() {
    showTreasure()
})
basic.forever(function on_forever2() {
    generateImage()
    moveForward()
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (x_add == 0 && y_add == -1) {
        x_add = -1
        y_add = 0
    } else if (x_add == 0 && y_add == 1) {
        x_add = 1
        y_add = 0
    } else if (x_add == 1 && y_add == 0) {
        x_add = 0
        y_add = -1
    } else {
        x_add = 0
        y_add = 1
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (x_add == 0 && y_add == -1) {
        x_add = 1
        y_add = 0
    } else if (x_add == 0 && y_add == 1) {
        x_add = -1
        y_add = 0
    } else if (x_add == 1 && y_add == 0) {
        x_add = 0
        y_add = 1
    } else {
        x_add = 0
        y_add = -1
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    arr = [0]
})
bluetooth.onBluetoothConnected(function on_bluetooth_connected() {
    basic.showIcon(IconNames.Happy)
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Nyan), music.PlaybackMode.InBackground)
    basic.pause(2000)
})
bluetooth.onBluetoothDisconnected(function on_bluetooth_disconnected() {
    basic.showIcon(IconNames.Sad)
    basic.pause(2000)
})
bluetooth.onUartDataReceived("A", function on_uart_data_received() {
    
    if (x_add == 0) {
        x_add = -1
        y_add = 0
    } else if (y_add == 0) {
        x_add = 0
        y_add = -1
    }
    
})
bluetooth.onUartDataReceived("B", function on_uart_data_received2() {
    
    if (x_add == 0) {
        x_add = 1
        y_add = 0
    } else if (y_add == 0) {
        x_add = 0
        y_add = 1
    }
    
})
