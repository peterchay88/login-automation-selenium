# Login Automation Framework

This framework uses Pytest and Selenium validate the properties and different states
of [Practice Automation Website](https://practicetestautomation.com/). 

The following pages are tested by this automation framework: \
[Login page ](https://practicetestautomation.com/practice-test-login/)\
[Exceptions page](https://practicetestautomation.com/practice-test-exceptions/)

The login page provides realworld scenarios for log in pages and the tests go over
standard use cases of  a login page.
- Correct username & password
- Incorrect username
- Incorrect password

The exceptions page provides tests that handle different web ui states that would normally
throw an exception unless the test accounts on how to handle these scenarios. 
- NoSuchElementException
- ElementNotInteractableException
- InvalidElementStateException
- StaleElementReferenceException
- TimeoutException

## Requirements
- Python
- Pytest
- Selenium

In order to run this framework please run the following commands to install the 
necessary packages.
```commandline
pip install requirements.txt
```

You will also need the required web drivers for Chrome and Firefox in your PATH. For more information on 
how to do so please see the [selenium documentation](https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/#download-the-driver)

### How To Run tests
When running the tests you can specify which browser to run the tests on by using the `browser` argument. For example:
```commandline
pytest --browser firefox
pytest --browser chrome
```
If you do not specify the browser the default is chrome. You may also run specific tests by
targeting the test tag id.
```commandline
pytest -m exception_tc01
```