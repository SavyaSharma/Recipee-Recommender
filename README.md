# Model
This is a large better model 
[Link](https://drive.google.com/file/d/1WVpDBxLiM1m0zm_G97Ps2X3aZHjeIlyW/view?usp=sharing)
Download the model to the recip-eeze-flask/recipeeze/model/ directory

# Problem Summary

What should I eat? This is a common problem, which many Canadians face daily. Even if they prefer to eat home cooked healthy meals many feel they have no option but to turn to restaurants or fast food due to lack of ideas or time . Around 54 % Canadians eat out once per week.  40 % eat out as they don’t know how to cook from available ingredients or have less time as per Statistics Canada [Wikipedia](https://www150.statcan.gc.ca/n1/pub/11-627-m/11-627-m2019003-eng.htm
). 

This has an adverse impact on their health and finances. We want to provide people with a way to make food at home easily and quickly by recommending recipes depending on their preferences and what ingredients they have available on hand.

# Approach

In order to solve this problem, we can gather data from user input and compare it to recipes listed on allrecipes.com. From this we can create an algorithm to provide meal recipe recommendations to the user.

The parameters we will be working with are; 

* the amount of time the recipe takes to prepare
* the cuisine desired by the user
* the ingredients available on hand

With this data we can build a recommender system in which the user inputs the amount of time they have available and the desired cuisine from any world region they desire. Based on these inputs we will generate a short list of recipes that fit their preferences.

# Problem Statement

Canadians today are strapped for time and money, but they want to eat healthy and have a variety of choices through convenience. With the seemingly unlimited options available out there, we propose making an assistant that can help them make the best choice possible.

## Ideal

The user tells the recommender program the cuisine they would ideally like to eat, what ingredients they have on hand, and how much time they have. The program then uses the input given to recommend the best meal recipes that best suit the user’s choices.

## Reality

People do not know what they can cook with the time they have available, and generally need new ideas for what they can make and eat. Currently, Canadians aren’t planning meals in advance and when they arrive at the point that they need to eat, they are frustrated by the decisions that need to be made in order to make a meal. They settle on the path of least resistance, choosing often to forego making meals at home, instead choosing to eat out.

## Limitations

[allrecipes.com](https://www.allrecipes.com/) does not in fact have all the recipes in the world. Some recipes people desire may not be in the database. The algorithm does not consider individual cooking skill level. Perhaps the user doesn’t have the best ingredients for the cuisine that they have chosen. Could they be instead recommended a choice from another country that has similar taste profiles?

## Proposal

If someone in Canada wants to eat Japanese food with the ingredients on hand, the user can input this information into the application, and will get an appropriate recommendation. Canadians today are strapped for time and money, but they want to eat healthy and have a variety of choices. With the seemingly unlimited options available out there, we propose making an assistant that can help them make the best choice possible.

# Rationale

We want to provide people with a way to figure out what they can eat based on the amount of time they have to cook and the desired global appeal of a recipe. People all over Canada could be saving money while simultaneously honing a skill everyone should have. That being the ability to cook food for one's self. Also, they will have an informed choice for eating healthy food. Anyone interested in saving money on eating out while simultaneously becoming more independent will benefit from this.
