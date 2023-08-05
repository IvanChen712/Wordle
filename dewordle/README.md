# Dewordle

Help you solve the wordle game.

## Version1

This version can only filter the words that have or don't have certain letters.

**Usage**: Type +/- the letter(s) you want to add or remove.

## Version 2

**Usage**: Input your guessed word and corresponding results.

**Example input**:  crane 00012

* 0: not exist
* 1: exist, but wrong position
* 2: exist, and right position


    Input your guesses word and corresponding results.
    The word should have five letters and the results should have five numbers. 
    Attempt 1:irate 00000
    
    1179 words left in total.
    
    Attempt 2:husky 00001
    zygon  nonyl  nylon  xylyl  gyppo  womyn  cymol  cyclo  pylon  polyp  xylol  yobbo  
    ycond  
    13 words left in total.
    
    Attempt 3:nylon 01210
    polyp  
    Only one word left.
    
    Attempt 4:polyp 22222
    Congratulations! You solved the wordle in 4 steps.

