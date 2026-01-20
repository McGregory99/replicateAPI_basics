# Replicate AI Demo - Elfos del Futuro 🧝✨

[**🎥 Ver Tutorial Paso a Paso en YouTube**](https://youtube.com/...) *(Link pendiente)*

Este proyecto es una demo simple y práctica de cómo integrar la API de **Replicate** con Python para generar contenido multimedia épico usando los modelos SOTA (State of the Art) del momento.

## 🚀 Modelos Utilizados

*   **Imagen**: `black-forest-labs/flux-schnell`
    *   Genera la imagen base del líder elfo y el banquete.
*   **Vídeo**: `kwaivgi/kling-v1.6-pro`
    *   Transforma la imagen estática en un vídeo con movimiento natural (Image-to-Video).
*   **Voz**: `minimax/speech-02-turbo`
    *   Genera el discurso de bienvenida con entonación natural y en español.

## 🛠️ Instalación

1.  Inicializa el entorno e instala las dependencias (uv detectará automáticamente el `pyproject.toml`):
    ```bash
    uv sync
    ```
    *Esto creará la carpeta `.venv` y descargará todo lo necesario.*



## ▶️ Uso

Ejecuta el script principal para generar todo el contenido de una vez:

```bash
uv run python main.py
```

Al finalizar, encontrarás en la carpeta:
*   `resultado_imagen.webp`
*   `resultado_video.mp4`
*   `resultado_audio.wav`

¡Disfruta del banquete élfico! 🍷🍃
