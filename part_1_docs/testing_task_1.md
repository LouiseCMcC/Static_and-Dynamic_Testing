### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      # should be ==1 not =1
      return True
    else
    # missing colon for else condition 
      return False
   

  dif highest_card(self, card1 card2):
  # should say def instead of dif
  # missing comma in parameters
  if card1.value > card2.value:
    # function content needs to be tabbed in
    return card
    # should say card1 instead of card
  else:
    return card2
  


def cards_total(self, cards):
  # function needs to be tabbed in
  total
  # total counter should be set to 0
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # need to put space after of for string to be formatted properly
    # total number needs converted to integer to concatonate with string.
  
```
