import cv2
import threading
import mediapipe as mp
import streamlit as st
import numpy as np
import time

# Variables globales
frame = None
posture = "Desconocido"
stop_flag = False
lock = threading.Lock()

# Hilo de captura de video
def capture_thread():
    global frame, stop_flag
    cap = cv2.VideoCapture(0)
    while not stop_flag:
        ret, f = cap.read()
        if ret:
            with lock:
                frame = f.copy()
    cap.release()

# Hilo de procesamiento de postura
def processing_thread():
    global frame, posture, stop_flag
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    while not stop_flag:
        with lock:
            if frame is None:
                continue
            f = frame.copy()
        rgb = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            hip_y = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
            knee_y = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y
            posture = "Sentado" if (knee_y - hip_y) > 0.2 else "Parado"

# Interfaz Streamlit
def main():
    global stop_flag
    st.title("🧍‍♀️ Detección de Postura con MediaPipe 💺")
    st.write("Detecta si la persona está parada o sentada en tiempo real.")
    frame_placeholder = st.empty()
    label_placeholder = st.empty()

    # Iniciar los hilos
    t1 = threading.Thread(target=capture_thread)
    t2 = threading.Thread(target=processing_thread)
    t1.start()
    t2.start()

    try:
        while True:
            with lock:
                if frame is None:
                    continue
                f = frame.copy()
            _, buffer = cv2.imencode('.jpg', f)
            frame_placeholder.image(buffer.tobytes(), channels="BGR")
            label_placeholder.markdown(f"### 🪑 Postura detectada: **{posture}**")
            time.sleep(0.05)
    except KeyboardInterrupt:
        stop_flag = True
        st.write("Finalizando...")
    finally:
        stop_flag = True
        t1.join()
        t2.join()

if __name__ == "__main__":
    main()
