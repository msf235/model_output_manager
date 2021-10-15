# Model Output Manager (MOM)

This is a simple utility for keeping track of sets of parameters in a parameter table. This is useful for, say, running simulations with a large number of possible hyperparameters, where the models will be automatically saved and loaded based on the chosen hyperparameters.

This constitutes a particular implementation of memoization. As opposed to the memoization implementations of Joblib's Memory class or the Python Decorator Library's "memoized" utility https://wiki.python.org/moin/PythonDecoratorLibrary, Model Output Manager makes a log of parameters in a .csv file and leaves a bit more control to the user.

Run demonstrate_model_output_manager.ipynb with Jupyter for a tutorial.

Happy simulating,
Matt
