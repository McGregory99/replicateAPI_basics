import replicate

def generate_image(prompt_text):
    print(f"🎨 Generando imagen para: '{prompt_text}'...")
    
    # Modelo: Flux Schnell (Rápido y alta calidad)
    output = replicate.run(
        "black-forest-labs/flux-schnell",
        input={
            "prompt": prompt_text,
            "go_fast": True,
            "megapixels": "1",
            "aspect_ratio": "16:9"
        }
    )
    
    # Flux devuelve una lista de streams, tomamos el primero
    image_url = str(output[0]) 
    
    print(f"✅ Imagen lista: {image_url}")
    return image_url
