from selenium.webdriver.common.by import By
from pytest_check import check
import requests

def test_brok_img(driver):

    driver.get('https://the-internet.herokuapp.com/broken_images')
    img_set = driver.find_elements(By.TAG_NAME, 'img')

    # Create an empty list to store broken images
    broken_images = []
    work_images = []

    # Iterate through the image elements
    for image in img_set:
        image_attr = image.get_attribute('src')
        # print(image_attr)
        response = requests.head(image_attr)
        # print(response)
        if response.status_code != 200:
            broken_images.append(image_attr)
        else:
            work_images.append(image_attr)

    # Use pytest-check's equal to check for no broken images
    assert len(img_set) == 4
    assert broken_images not in work_images, f'Broken image URLs: {", ".join(broken_images)} \n and working images {", ".join(work_images)}'
    # Use pytest-check's check then broken_images not in work_images
    check.is_not_in(broken_images, work_images, 'Check the broken_images has error')

    # Print the broken image URLs
    # if broken_images:
    #     print(f'Broken image URLs: {", ".join(broken_images)} \n and working images {", ".join(work_images)}')
    # else:
    #     print('No broken images found.')

    ### reminder ###
        # check.equal - a == b
        # check.not_equal - a != b
        # check.is_ - a is b
        # check.is_not - a is not b
        # check.is_true - bool(x) is True
        # check.is_false - bool(x) is False
        # check.is_none - x is None
        # check.is_not_none - x is not None
        # check.is_in - a in b
        # check.is_not_in - a not in b
        # check.is_instance - isinstance(a, b)
        # check.is_not_instance -
        # not isinstance(a, b)
        # check.almost_equal - a == pytest.approx(b, rel, abs)
        # see
        # at: pytest.approx
        # check.not_almost_equal - a != pytest.approx(b, rel, abs)
        # see
        # at: pytest.approx
        # check.greater - a > b
        # check.greater_equal - a >= b
        # check.less - a < b
        # check.less_equal - a <= b
        # check.between - a < b < c
        # check.raises - func
        # raises
        # given
        # exception
        # similar
        # to
        # pytest.raises ###

    