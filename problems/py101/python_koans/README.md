For this exercise we will learn the Zen of Python using Test Driven Development.
Python Koans is a suite of broken tests, which are written against Python code that demonstrate how to Pythonic code.
Your job is to fix the broken tests by filling in the missing parts of the code.

* Download the zip of python_koans from [here](https://github.com/tathagata/python_koans/archive/chipy_mentorship_coding_dojo.zip). This is a fork of the original repository without some of the simpler examples.

* Unzip the archive. Change into the directory created and then depending on which version of Python you
would be using, change into python2 or python3 directory.

* Run `./run.sh` or `./run.bat` depending on if you are in a unix or windows environment.

* You'll see an output like
> Thinking AboutLists
>   test_creating_lists has damaged your karma.
>
> You have not yet reached enlightenment ...
>   AssertionError: '-=> FILL ME IN! <=-' != 0

> Please meditate on the following code:
>  File "/Users/t/Downloads/python_koans-chipy_mentorship_coding_dojo_2/python3/koans/about_lists.py", line 14, in test_creating_lists
>     self.assertEqual(__, len(empty_list))
>
>
> You have completed 0 koans and 1 lessons.
> You are now 206 koans and 36 lessons away from reaching enlightenment.
>
> Beautiful is better than ugly.

* Open the file that follows "Please meditate on the following code" in your text editor and put the appropriate fix.

* Run `./run.sh` or `./run.bat` depending on if you are in a unix or windows environment. If your fix is correct, you'll see the error message has been replaced with a new one. Great! you have fixed one test, so now move on to the next one by repeating the above steps.
