#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_size():
    res = input("what size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>")
    
    if res == 'a':
        return('Small')
    elif res =='b':
        return 'Medium'
    elif res =='c':
        return 'Large'
    else:
        print_message()
        return get_size()
    
    
    return res


# In[3]:


def print_message():
    print("I'm sorry, I didn't understnad your selection. Please enter the corresponding letter for your response.")


# In[4]:


def get_drink_type():
    res = input("what type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>")
    
    if res == 'a':
        return ("Brewed Coffee")
    elif res =='b':
        return 'Mocha'
    elif res =='c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()
    
    return res


# In[5]:


def order_iceorhot():
    res = input("and would you like an iced or hot drink?  \n[a] Ice \n[b] Hot \n>")
    
    if res == 'a':
        return 'Ice'
    elif res =='b':
        return 'Hot'
    else:
        print_message()
        return order_iceorhot()

    return res


# In[6]:


def order_latte():
    res = input("and What kind of milk for your latte?  \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>")

    if res == 'a':
        return '2% milk'
    elif res =='b':
        return 'Non-fat milk'
    elif res =='c':
        return 'Soy milk'
    else:
        print_message()
        return order_latte()

    return res


# In[7]:


#def extra_options():
#  res = input('Would you like a plastic cup or did you bring your own reusable cup? \n[a] I\'ll need a cup. \n[b] Brought my own! \n> ')
 
#  if res == 'a':
#    print('Okay, no problem! We\'ll get you a plastic cup.')
#  elif res == 'b':
#    print('Great! We\'ll fill up your reusable cup.')
#  else:
#    print_message()
#    return extra_options()


# In[8]:


def coffee_bot():
    print("Welcome to this cafe!")
  
    size = get_size()
    drink_type = get_drink_type()
    iceorhot = order_iceorhot()
    print('Alright, that\'s a {} {} {} !'.format(iceorhot, size, drink_type))
    
    
    name = input("Can I get you name please? \n> ")
    print('Thanks, {}! Your drink will be ready shortly.'.format(name))


# In[9]:


#coffee_bot()


# In[ ]:




