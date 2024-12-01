# Generador de historia con API Text WebUI

Esta aplicación Python consiste en un chat en el que el usuario pregunta por una historia, incluyendo el personaje principal, el personaje secundario, un lugar y un acontecimiento importante.

## Implementación de API

En este caso, he utilizado la API Qwen, en concreto la Qwen_Qwen2.5-1.5B-Instruct.

<img src="https://drive.google.com/uc?id=1mELJY5to96lwDrU6MShpgs43p5UMSJ0J">

## Prueba de diferentes LLM

Vamos a preguntarle sobre la siguiente historia

<img src="https://drive.google.com/uc?id=1jWFfViBS-nbf5rKS1lXzc4SFbv15nptG">

### Primer modelo

Primeramente probé con el modelo por defecto, incluyendo un máximo de 200 palabras (`tokens`)

<img src="https://drive.google.com/uc?id=1WxeHQfAL8FtOwoeVN7uTjOJn6906tHuz">
<img src="https://drive.google.com/uc?id=1E3QR4v4QIoIxRIMbGobw1CWIeogEEjJ0">

Se ve que la historia que se ha generado apenas tiene sentido.

### Segundo modelo

Luego ajusté un poco los ajustes de temperatura y la semilla.

<img src="https://drive.google.com/uc?id=1v5xdVmO-z4JIufvfNmcpBQLPyghcbM3q">
<img src="https://drive.google.com/uc?id=1RpGJXnRdMX9n_HRg76P6Uo-qhg-sKsWF">

Hemos obtenido mejora, pero aún así se puede mejorar.

### Tercer modelo

Ajustamos la semilla y la temperatura de diferente manera, bajando un poco la creatividad.

<img src="https://drive.google.com/uc?id=1l8yDD9Ex0FOdYMf4nb6AM08fZvKsolUf">
<img src="https://drive.google.com/uc?id=1CZ51dNA1QoQkmgQgrVDwaqWFhhmLhI1U">

Vemos que esta historia es bastante coherente, por lo que el modelo funciona perfectamente.


