import replicate

def generate_voice(text):
    print(f"🎙️ Generando voz para: '{text}'...")
    
    # Modelo: Minimax Speech-02 Turbo
    # Docs: https://replicate.com/minimax/speech-02-turbo/api/schema
    output = replicate.run(
        "minimax/speech-02-turbo",
        input={
            "text": text,
            "emotion": "happy",           # Forzamos emoción feliz
            "language_boost": "Spanish",   # Ayuda al modelo a detectar español
            "voice_id": "Deep_Voice_Man"    # (Opcional) Esta es la default si no pones nada
        }
    )
    
    # Devuelve la URL del archivo de audio
    audio_url = output
    print(f"✅ Audio listo: {audio_url}")
    return audio_url