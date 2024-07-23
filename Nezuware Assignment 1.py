#!/usr/bin/env python
# coding: utf-8

# # Rock,paper,scissor program
# 

# In[30]:


import random
user_choice=int(input("enter your choice: Type 0 for Rock , 1 for Paper, 2 for Scissors ."))
computer_choice =random.randint(0,2)
if user_choice >=3 or user_choice < 0:
    print("you have entered invalid number,you loose")
else:
    print("computer choice :")
    print(computer_choice)
    if computer_choice == user_choice:
        print("It's a draw.")
    elif computer_choice == 0  and user_choice == 2:
        print("you loose")
    elif user_choice == 0 and computer_choice == 2:
        print("you win")
    elif computer_choice > user_choice:
        print("you loose")
    elif user_choice > computer_choice:
        print("you win")

    

    
    

    




# 

# In[ ]:





# 

# In[ ]:





# In[ ]:




