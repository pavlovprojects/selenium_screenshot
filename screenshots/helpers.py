from PIL import Image
from PIL import ImageChops


def compare_images_light(master_screenshot, develop_screenshot):
    """ Simple image comparison function
    :param master_screenshot:
    :param develop_screenshot:
    :return:
    """
    master_screenshot = Image.open(master_screenshot).convert('RGB')
    develop_screenshot = Image.open(develop_screenshot).convert('RGB')

    # Returning the diff for images
    return ImageChops.difference(master_screenshot, develop_screenshot)


def compare_images_hard(master_screenshot, develop_screenshot):
    pass
