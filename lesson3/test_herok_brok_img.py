from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
        # print(resource)
        if response.status_code != 200:
            broken_images.append(image_attr)
        else:
            work_images.append(image_attr)


    # Print the broken image URLs
    if broken_images != work_images:
        print(f'Broken image URLs: {", ".join(broken_images)} \n and working images {", ".join(work_images)}')
    else:
        print('No broken images found.')



    