# Lottery-Challenge-EOMP FEEDBACK
 Dear Gideon

Why would you enter ID number then go on to enter gender , DOB. SA ID number provides all these. What is needed is to manipulate it. And I mentioned that you could use rsaidnumber.

------------------------Interface design--------------------

The screen is very unique.

-----------------Age validation/Validation of entries----------------

Works well

--------------------Variable Naming---------------------

Good

https://www.python.org/dev/peps/pep-0008/#naming-conventions



---------------------Lotto Generation--------------------

Why let your app allow duplicates to be selected. What I also pick up is a number selected in set one can not be selected in set 2. This a glitch. Sets should be independent of each other.

------EXAMPLE------

import random

my_lotto_number=[]
my_lotto_number=random.sample(range(1, 49),6)

my_lotto_number.sort()

print(my_lotto_number)

---------Sound Implementation----- 

works well

Currency converter-You convert to and convert from seem to be the opposite. Try convert ZAR amount and you will see this.

Claim Prize -Why is the default bank set to standard bank Also, the app shouldn’t allow user to type in is/her winnings



Text Files- Info not being appended to the text file. I see an attempt to create text files but they are not used as they are supposed to be.

Challenges-Testing

Complexity-Intermediate

Documentation-Fair



See how you can shorten UUID

import uuid
x = uuid.uuid4()
print(str(x)[:8])



I suspect you spend a lot of time on planning and did not have time to do thorough testing of your code.



Please remove these from your code- they are not doing anything

def clear(self):
pass

def play_again(self):
pass



You have the potential to surpass this standard

Best



Godwin

Feedback given- 07/07/2021