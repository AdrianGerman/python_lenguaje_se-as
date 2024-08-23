import cv2
from hand_detection import detect_hands


def main():
    # Asegúrate de que la cámara esté correctamente inicializada
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('Error: No se pudo abrir la cámara.')
        return

    while True:
        ret, frame = cap.read()  # Lee un cuadro de la cámara
        if not ret:
            print('Error: No se pudo leer el cuadro de la cámara.')
            break

        # Procesa el cuadro para detectar las manos
        frame = detect_hands(frame)

        cv2.imshow('Hand Detection', frame)  # Muestra el cuadro procesado

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Espera la tecla 'q' para salir
            break

    cap.release()  # Libera la cámara
    cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas


if __name__ == '__main__':
    main()
