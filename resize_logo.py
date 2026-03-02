from PIL import Image
import os

input_path = "/Users/dariuslukosius/Desktop/kurtas-service-mercedes-benz-logo-BGE7AkD6.png"
landscape_output = "/Users/dariuslukosius/Desktop/kurtas-ads-landscape.png"
square_output = "/Users/dariuslukosius/Desktop/kurtas-ads-square.png"

def resize_with_padding(img, target_size):
    # Calculate aspect ratios
    img_ratio = img.width / img.height
    target_ratio = target_size[0] / target_size[1]
    
    if img_ratio > target_ratio:
        # Image is wider than target
        new_width = target_size[0]
        new_height = int(new_width / img_ratio)
    else:
        # Image is taller than target
        new_height = target_size[1]
        new_width = int(new_height * img_ratio)
        
    # Resize image with high quality
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Create new transparent background
    new_img = Image.new("RGBA", target_size, (255, 255, 255, 0))
    
    # Center the resized image
    offset = ((target_size[0] - new_width) // 2, (target_size[1] - new_height) // 2)
    new_img.paste(resized_img, offset)
    
    return new_img

try:
    with Image.open(input_path) as img:
        img = img.convert("RGBA")
        
        # 1. Landscape Logo (4:1)
        # Recommended: 1200 x 300
        landscape = resize_with_padding(img, (1200, 300))
        landscape.save(landscape_output, "PNG")
        print(f"Saved landscape logo to: {landscape_output}")
        
        # 2. Square Logo (1:1)
        # Recommended: 1200 x 1200
        square = resize_with_padding(img, (1200, 1200))
        square.save(square_output, "PNG")
        print(f"Saved square logo to: {square_output}")

except Exception as e:
    print(f"Error: {e}")
