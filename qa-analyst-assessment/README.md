QA Analyst Technical Assessment

Candidate: Colin O'Toole
Language Used: Python
Completion Date: 10/15/2025

Part 1: Functional Programming
- Time Spent: ~30 minutes
- Approach: First, I created a python set that stores list elements that have already been seen before. Then, I iterated through the list input and created a new empty list. If a list element is not present in the set, then the list element is added to the set and the new list.

Part 2: API Testing  
- Time Spent: ~30 minutes
- Approach: The first test sends a get request and asserts that the response received contains an id, name, email, and a status code of 200. The second test sends a post request containing json data and asserts that the response received has a status code between 200 and 299. The third test sends a get request and asserts that the response received has a status code of 404.

How to Run
Part 1
Use "py solution.py" to run the file.

Part 2
Use "py -m pip install pytest" and "py -m pip install requests" to install the dependencies. Use "py -m pytest solution.py" to run the tests.
