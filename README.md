# Pytest-Framework

Pytest is a testing framework based on python. It is mainly used to write API test cases.
The advantages of Pytest are as follows −
•	Pytest can run multiple tests in parallel, which reduces the execution time of the test suite.
•	Pytest has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
•	Pytest allows us to skip a subset of the tests during execution.
•	Pytest allows us to run a subset of the entire test suite.
•	Pytest is free and open source.
•	Because of its simple syntax, pytest is very easy to start with.


Libraries needed for installation
python -m pip install pytest
allure-pytest	2.8.16	
allure-python-commons	2.8.16	
beautifulsoup4	4.9.1	
html-reports	0.1.0	
html-testRunner	1.2.1	
pytest-html	1.22.1	
selenium	3.141.0	


Creating html reports

pytest --html=report.html

Creating Allure reports
Terminal 1
pytest -v -s alluredir="D:\pythonWorkspace\PyTestProjectTemplate\reports"
Terminal 2
allure serve D:\pythonWorkspace\PyTestProjectTemplate\reports


Further can be deployed in Jenkins for automated process.
