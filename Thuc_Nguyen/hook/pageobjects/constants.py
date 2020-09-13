from selenium.webdriver.common.by import By

BASE_URL = "https://unsplash.com/"
URL = {
    'LOGIN_USER': BASE_URL + 'login',
    'VIEW_LIST_COLLECTION_OF_USER': BASE_URL + '@{username}/collections',
    'VIEW_LIST_PHOTO_OF_USER': BASE_URL + '@{username}',
    'VIEW_LIST_LIKED_PHOTO_OF_USER': BASE_URL + '@{username}/likes',
    'COLLECTION': BASE_URL + 'collections/{collection_id}/{collection_title}',
    'PHOTO': BASE_URL + 'photos/{photo_id}'
}
LOGIN_PAGE = {
    'EMAIL_TEXTBOX': (By.ID, 'user_email'),
    'PASSWORD_TEXTBOX': (By.ID, 'user_password'),
    'LOGIN_BUTTON': (By.NAME, 'commit')
}

HOME_PAGE = {
    'LOGIN_BUTTON': (By.XPATH, '//a[@href="/login"]'),
    'MENU_BUTTON': (By.XPATH, '//button[@class="SS3S4 _3d86A"]'),
    'MENU_ITEM': '//a[@role="link" and text() = "{item}"]'
}

VIEW_PROFILE_PAGE = {
    'PROFILE_NAME': (By.XPATH, '//div[@class="XmcS-"][1]/div/div[1]'),
    'EDIT_PROFILE_BUTTON': (By.XPATH, '//div[@class="XmcS-"][1]//a[@href="/account"]')
}

EDIT_PROFILE_PAGE = {
    'PROFILE_LOCATION': (By.ID, 'user_location')
}

PHOTO_PAGE = {
    'LIKE_BUTTON': (By.XPATH, '//button[@title="Like photo"]'),
    'INFO_BUTTON': (By.XPATH, '//button//span[normalize-space(text())="Info"]'),
    'CAMERA_MODEL_VALUE': (By.XPATH, '//dt[text() = "Camera Model"]/following-sibling::dd'),
    'FOCAL_LENGTH_VALUE': (By.XPATH, '//dt[text() = "Focal Length"]/following-sibling::dd')
}

COLLECTION_PAGE = {
    'PHOTO_IN_COLLECTION':
        '//div[@data-test ="masonry-grid-count-three"]/div[{column_pos}]/div[{row_pos}]/figure',
    'LIST_PHOTO_IN_COLLECTION':
        (By.XPATH, '//div[@data-test ="masonry-grid-count-three"]/div/div/figure/div/div/a')
}

PHOTO_LIST_PAGE = {
    'PHOTO_IN_LIST':
        (By.XPATH, '//div[@data-test ="masonry-grid-count-three"]//figure')
}

COLLECTION_LIST_PAGE = {
    'COLLECTION_IN_LIST': '//div[{collection_pos}]/div[@data-test= "collection-feed-card"]'
}

LIKES_PAGE = {
    'PHOTO_IN_LIKES':
        (By.XPATH, '//div[@data-test ="masonry-grid-count-three"]//figure')
}
