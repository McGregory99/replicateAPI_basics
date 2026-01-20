import replicate

def generate_video(prompt_text, image_url=None):
    print(f"🎬 Generando vídeo con Kling v1.6 para: '{prompt_text}'...")
    
    input_data = {
        "prompt": prompt_text,
        "cfg_scale": 0.5
    }
    
    # Si tenemos imagen, la usamos como punto de partida (start_image)
    if image_url:
        print(f"   Using start image: {image_url}")
        input_data["start_image"] = image_url
        
    # Modelo: Kling v1.6 Pro (Excelente para Image-to-Video)
    output = replicate.run(
        "kwaivgi/kling-v1.6-pro",
        input=input_data
    )
    
    # Devuelve la URL directa del mp4
    # La salida de Kling a veces es una lista o string, estandarizamos:
    video_url = output[0] if isinstance(output, list) else output
    print(f"✅ Vídeo listo: {video_url}")
    return video_url