# Creating python directories 
- created a vitual envirioment 
- activated it 
- installed flake8
- installed pytest #running py tests
- installed pytest-expect #for assertions
- created a requirements.txt file #to keep track of installed requirements (pip freeze > requirements.txt) run to update
- Run to install form list (pip install -r requirements.txt)
- created project directories app and test 
- created .gitignore directory to setup what to ignore when sending to git

# multiplication tests (test first)
- import os and sys to set path for app.mltiply to import 
- set first test in tests file using assert run pytest = fail no function set 
- set function in app just enough to pass run pytest = test pass retun 1 as required
- set the second test run py test : failed red 
- updated the code to pass both test run pytest : bingo green again 
- repeated the seqence for all the rest of the tests 

# factorial tests (test last)
- started with writing code for factorial 0! to return 1
- write test for 0! and pased sucessfuly; thias holds for 1!
- write the code for 2! folowing n * (n-1)  and write test and run pytest :  passes 
- wirte code for 4! and it holds for the rest.
