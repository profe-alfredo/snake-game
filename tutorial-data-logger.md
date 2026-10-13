# Tutorial para data logger

## Configuramos la captura de datos

En el bloque de inicio, asignamos a la variable un falso, y definimos las columnas del bloque de configurar columnas con lo siguiente:
Temperatura
Sonido
Luz

Para agregar más datos se hace click en el **+**

```blocks
let capturar_datos = 0
basic.showIcon(IconNames.Heart)
datalogger.setColumnTitles("")
```

```blocks
loops.everyInterval(60000, function () {
    if (true) {
        datalogger.log(
        datalogger.createCV("", 0),
        datalogger.createCV("", 0),
        datalogger.createCV("", 0),
        datalogger.createCV("", 0)
        )
    }
})
```


