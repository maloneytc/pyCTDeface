import sys
from pathlib import Path
import ants


def deface(input_file):
    pass

def create_template(file_list, outpath, low_thresh=400, high_thresh=2000, iterations=5):
    """
    Creates a template file of the imaging files in file_list. The images are first thresholded between low_thresh and high_thresh.

    file_list: list of string or Paths

    outpath: str or Path

    low_thresh: int or float

    high_thresh: int or float

    iterations: int
    """
    outpath = Path(outpath)

    template_img_list = [
        ants.threshold_image(
        ants.reorient_image2(this_image), low_thresh, high_thresh)
        for this_image in file_list]

    template_img = ants.build_template(image_list=template_img_list, iterations=iterations)

    template_img.to_file(outpath)

def recon_image():
    """
    Create a jpg/png image of the 3D reconstructed image.
    """
    pass


if __name__ == "__main__":
    ## TODO: Use argparse
    if len(sys.argv) == 2:
        input_file = Path(sys.argv[1])
        if input_file.exists():
            deface(input_file)
        else:
            print(f'Error: The file {input_file} does not exist!')
