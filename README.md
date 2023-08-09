# SeleniumTesting
Final assignment on Stepik for the course "Test Automation with Selenium and Python"

To start this: <br/>
    &emsp;pytest 
    
Options: <br/>
    &emsp;file_name - specify file with tests <br/>
    &emsp;--language - interface language on the site <br/>
    &emsp;-m - run test with certain mark <br/>
    &emsp;-v - verbose report <br/>
    &emsp;-s - to see the text printed by the print() command <br/>
    &emsp;-tb=line - shorten the log with test results <br/>

Example: <br/>
    &emsp;pytest -v -s --tb=line --language=en -m "add_to_basket" test_product_page.py