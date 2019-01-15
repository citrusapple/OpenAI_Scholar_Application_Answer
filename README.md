# OpenAI_Scholar_Application_Answer


<img src="https://github.com/citrusapple/OpenAI_Scholar_Application_Answer/blob/master/openaiapplication.png" alt="openai logo" height = "200">

This is a response to a challenge code within the 2018 application for OpenAI's Scholar Program.  I was among the top 5% of applicants.

Task/ Prompt given:

given a function that calls up to 5 usernames (that matches user inputted prefix) in any given database, recall the entire database when you only have access to this function and not the database itself.


This is my logic for the code

    here's our recursive function, which will iterate through a-z progressively until all possibilities have been checked.
    it'll be easier to follow with examples.  We'll always start with the inputs (a,answer, 1, alpha)

    input a : to start with the simplest input for query(), "a"
    input answer: just to have an empty set to store our outputs as we progress
    input 1: to count the number of characters for prefix, in this case "a" is only 1 so we start with 1
    alpha: have the whole alphabet a-z for ease of iteration within the recursion

    overview of how the code progresses:
    1) look through query(a-z)
    2)whenever it returns 5 results, we look at the last result (in sample case "allen"
    3)from the last result we'll look at the next character. (in sample case "l")
    4)add that on to our original input ("a" + "l" = "al")
    5)if that yields 5 results, we keep going (5th item = "alter", look at "al" + "t" = "alt")
    6)if that yields 5, we keep going. If it doesn't, we go back to 2 characters and search for the next
      possibility ("al", next would be "am")
    7) rinse and repeat everything until we're at "z".
    8) if z results in 5, we repeat everything above, but when it comes back,
      we return our result in holder without going back into recursion.
    9) since we stored all of this in final, we'll return final
    10) then we check if extract(query) == database
    11)done!

    3 test cases:
    testcase 1: what was given with the assignment
    testcase 2: a list of many users with "username" + a-z to test how far the recursion can go
    testcase 3: empty list, in case there are no users.

