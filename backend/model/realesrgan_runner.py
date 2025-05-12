import os
from PIL import Image
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer
import numpy as np  # Import NumPy

# Init once
model_path = os.path.join('..', 'models', 'realesrgan', 'weights', 'RealESRGAN_x4plus_anime_6B.pth')

model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=6, num_grow_ch=32)
upscaler = RealESRGANer(
    scale=4,
    model_path=model_path,
    model=model,
    tile=0,
    tile_pad=10,
    pre_pad=0,
    half=False  # Set to False if on CPU
)

def upscale_image(input_path: str, output_path: str):
    img = Image.open(input_path).convert("RGB")
    
    # Convert the PIL image to a NumPy array
    img_np = np.array(img)
    
    # Enhance the image using RealESRGAN
    output, _ = upscaler.enhance(img_np, outscale=1)
    
    # Convert the output back to a PIL Image and save it
    output_img = Image.fromarray(output)
    output_img.save(output_path)
    
    return output_path
