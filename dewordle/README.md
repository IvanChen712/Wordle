# dewordle

Help you solve the wordle game.

## Version1

**Usage**: Type +/- the letter(s) you want to add or remove.

    py dewordle.py
    +crane
    crena  crane  nacre  caner  rance
    5 words left in total.

    py dewordle.py
    -efgh

    4786 words left in total.

    -woadcz

    624 words left in total.

    -st

    141 words left in total.

    -in
    yukky  jumpy  purpy  yuppy  rumly  murky  urubu  puppy  rummy  bulky
    mummy  burly  rubby  burry  bully  pulpy  blurb  xylyl  plump  plumb
    buppy  bubby  lumpy  plumy  murry  lummy  lurry  luvvy  yummy  pully
    murly  jumby  bumpy  rumpy
    34 words left in total.

## Version 2

**Usage**: Input your guessed word and corresponding results.

**Example input**:  crane 00012

* 0: not exist
* 1: exist, but wrong position
* 2: exist, and right position
