import os

from screenshots.helpers import compare_images_light

TMP_FOLDER = os.path.join("screenshots", "tmp")


def test_main_page(browser):
    b = browser  # just alias to keep code shorter
    master_path = os.path.join(TMP_FOLDER, "base.png")
    develop_path = os.path.join(TMP_FOLDER, "reference.png")
    difference = os.path.join(TMP_FOLDER, "difference.png")

    b.get(b.base_url)
    b.save_screenshot(master_path)
    b.get(b.reference_url)
    b.save_screenshot(develop_path)
    try:
        result = compare_images_light(master_path, develop_path)
        assert result is None
    except AssertionError:
        result.save(difference)
        raise AssertionError(
            "Found difference: {} for master: {} vs. develop: {}".format(result.getbbox(), b.base_url, b.reference_url)
        )
