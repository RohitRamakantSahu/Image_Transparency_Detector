from PIL import Image
import numpy as np

def has_transparency(pil_img, threshold=0):
    """Returns True if the image has transparent pixels."""
    img = pil_img.convert("RGBA")
    alpha = np.array(img)[:,:,3]
    transparent_pixels = np.sum(alpha <= threshold)
    total_pixels = alpha.size
    has_trans = transparent_pixels > 0
    return has_trans, transparent_pixels, total_pixels, alpha

def show_transparent_mask(alpha):
    """Returns a PIL Image highlighting transparent areas in red."""
    mask = (alpha == 0)
    rgb_mask = np.zeros((*mask.shape, 4), dtype=np.uint8)
    rgb_mask[mask] = [255, 0, 0, 128]  # Red with half transparency
    return Image.fromarray(rgb_mask, "RGBA")

def process_image(image):
    """Process an image and return transparency information."""
    pil_img = Image.open(image)
    has_trans, num_trans, total, alpha = has_transparency(pil_img)
    return {
        'image': pil_img,
        'has_transparency': has_trans,
        'transparent_pixels': num_trans,
        'total_pixels': total,
        'alpha': alpha
    } 