import os
import requests
import time
from image import generate_image
from video import generate_video
from voice import generate_voice

# Configura tu API KEY aquí o en las variables de entorno
os.environ["REPLICATE_API_TOKEN"] = "r8_E75......"

def save_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"💾 Guardado en disco: {filename}")

def main():
    print("🚀 Iniciando Demo de Replicate...")
    
    # 1. IMAGEN
    prompt_img = "Cinematic grandiose shot of a charismatic High Elf leader welcoming the guests at a massive futuristic forest banquet, bioluminescent ancient trees, thousands of happy elves celebrating in the background with golden goblets, magical feast, hyper-realistic, 8k, vibrant colors, soft volumetric lighting, masterpiece, welcoming gesture, extreme detail"
    img_url = generate_image(prompt_img)
    save_file(img_url, "resultado_imagen.webp")

# 2. VÍDEO
    # Prompt diseñado para dar vida a la imagen estática coincidiendo con el discurso
    prompt_vid = "High Elf leader speaking directly to the camera with a warm and charismatic expression, natural mouth movement, gentle hand gestures welcoming the crowd, bioluminescent particles floating in the air, soft wind moving the leaves of the ancient trees, cinematic lighting, 8k, photorealistic, slow subtle zoom in"
    
    # Pasamos la URL de la imagen generada anteriormente para mantener consistencia
    vid_url = generate_video(prompt_vid, img_url)
    save_file(vid_url, "resultado_video.mp4")

    # 3. VOZ
    # texto_voz = "Bienvenido al futuro. Estoy súper contento de tenerte aquí es todo una oportunidad para la comunidad de elfos del bosque y sin duda este día será recordado por los próximos milenios y celebrado anualmente con un gran banquete"
    # audio_url = generate_voice(texto_voz)
    # save_file(audio_url, "resultado_audio.wav")
    
    print("\n✨ ¡Todo completado! Revisa tu carpeta.")

if __name__ == "__main__":
    main()
