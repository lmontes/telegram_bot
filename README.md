## Descripción

Se trata de un bot de telegram que nos permite controlar un proceso en remoto, es decir, ponerlo en marcha, pararlo, ver su estado, actualizar su código fuente (si lo tenemos en un repositorio git). Esto puede ser útil para controlar un proceso en un servidor al que no tenemos acceso desde el exterior como por ejemplo una Raspberry Pi.

Para su desarrollo se ha hecho uso de la librería [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).

## Requisitos

Para probar este bot necesitamos:

* Python 3
* La librería [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
* Un token para usar la API de Telegram. Se puede obtener a través de [BotFather](https://core.telegram.org/bots#6-botfather)

## Comandos soportados

* start
* stop
* status
* update
* log

## Configuración

El fichero de configuración tiene formato JSON y puede encontrarse tanto en /etc/bot.conf como en el fichero conf/bot.conf dentro de la ruta donde tenemos el bot. El fichero en /etc tiene prioridad sobre el otro, por lo que si existe no comprobará el del directorio conf. Tiene los siguientes parámetros:

* token: se trata del token necesario para usar la API de telegram.
* git_url: url de un repositorio git donde podemos tener otro proyecto, este proyecto es el que se actualizará cuando se ejecute el comando update en el Bot.
* log_file: fichero de log donde 
* command: comando que ejecutará el bot en el sistema
