import os
import imageio.v2 as iio


def create_animation(
    image_folder,
    filename_prefix="animation",
    duration=2,
    restart_delay=1000,
):

    # ASSEMBLE LIST OF IMAGES FILENAMES TO ANIMATE
    images = []
    image_filenames = os.listdir(image_folder)
    image_filenames = [img for img in image_filenames if img.endswith(".png")]
    
    # APPEND IMAGES TO AN IMAGES ARRAY
    for filename in image_filenames:
        try:
            image = iio.imread(f"./assets/plots/{filename}")
            images.append(image)
        except FileNotFoundError:
            print(f"Error: Image file not found: ./assets/plots/{filename}")
            return

    # BUILD THE GIF
    if images:
        duration = [duration] * (len(images) - 1) + [restart_delay]
        iio.mimsave(
            f"./assets/plots/{filename_prefix}.gif", images, duration=duration, loop=0
        )
        print(f"Animation saved to ./assets/plots/{filename_prefix}.gif")

    # CLEAN UP INDIVIDUAL IMAGES FILES (OPTIONAL)
    for filename in image_filenames:
        os.remove(f"./assets/plots/{filename}")