from hamcrest import assert_that, equal_to

STATUS_CODE_SUCCESS = 200
STATUS_CODE_CREATED = 201


def assert_response_code_success(status_code):
    assert_that(status_code, equal_to(STATUS_CODE_SUCCESS), 'Verify status code')


def assert_response_code_created(status_code):
    assert_that(status_code, equal_to(STATUS_CODE_CREATED), 'Verify status code')
