
# Lenguaje de Señas a Texto con Python

## Descripción

Este proyecto es una aplicación en Python que detecta el lenguaje de señas utilizando la cámara de la computadora y lo interpreta en texto en tiempo real. Utiliza `OpenCV` para capturar video, `MediaPipe` para la detección de manos y `TensorFlow/Keras` para el reconocimiento de las señas.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas:

- Python 3.x
- OpenCV
- MediaPipe
- TensorFlow o PyTorch
- Numpy

Puedes instalarlas ejecutando:

```bash
pip install opencv-python mediapipe tensorflow numpy
```

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/lenguaje_senas.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd lenguaje_senas
   ```

3. Instala las dependencias mencionadas en la sección de Requisitos.

## Uso

1. Inicia la aplicación ejecutando:

   ```bash
   python main.py
   ```

2. La cámara se abrirá y comenzará a detectar las manos. Si realizas una seña reconocida, esta será interpretada y convertida a texto, el cual se mostrará en la pantalla.

3. Presiona `q` para salir de la aplicación.

## Estructura del Proyecto

```plaintext
.
├── data/                    # Carpeta con datos de entrenamiento (imágenes, etiquetas)
├── models/                  # Modelos entrenados y guardados
├── src/
│   ├── main.py              # Script principal de la aplicación
│   ├── detection.py         # Módulo para la detección de manos y dedos
│   ├── recognition.py       # Módulo para el reconocimiento de señas
│   └── utils.py             # Funciones auxiliares
└── README.md                # Este archivo
```

## Entrenamiento del Modelo

Si deseas entrenar tu propio modelo para reconocer nuevas señas, sigue estos pasos:

1. Añade las imágenes de las señas a la carpeta `data/` y asegúrate de etiquetarlas correctamente.
2. Ejecuta el script de entrenamiento:

   ```bash
   python src/train.py
   ```

3. El modelo entrenado se guardará en la carpeta `models/`.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el proyecto o deseas añadir nuevas funcionalidades, no dudes en abrir un issue o enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

## Contacto

Si tienes alguna pregunta o sugerencia, puedes contactarme a través de [adrian.german1019@gmail.com](mailto:adrian.german1019@gmail.com).
