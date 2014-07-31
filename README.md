* Run the following commands to run the project's tests:
  * pip install -r requirements.txt
  * python manage.py test

This example illustrates unit testing arithmetic involving two models. These two models are leaves of a substantial 
dependency tree. Before we can instantiate the objects that we are interested in, we must first instantiate all of 
their dependencies. 

![Image of class hierarchy.](http://i.imgur.com/chiTuG2.png "Image of class hierarchy.")

Each instantiation is responsible for its dependencies. So, if the end goal is to instantiate a Warrior and a Wild Rat,
both objects must instantiate their immediate parents, which instantiate their parents. This continues until a base 
class with no parents other than models.Model is found. Once the base case is reached and instantiated, we work our way 
back down the call stack (and thus downward through the class hierarchy) until we reach the leaf (the derived class) 
that we were originally interested in.