import ast
from numpy import array, int64
from sklearn.tree import DecisionTreeClassifier


class modelLoaderSaver:
    """
    Class used to save and load models. Before model is loaded all necessary dependencies have to be imported. E.g. sklearn, numpy.
    This can be used to first saved already trained model and then to restore it from a file.
    """
    def __init__(self, class_object=None):
        self.class_object = class_object

    def save(self, filename):
        try:
            with open(filename, 'w') as file:
                file.write(str(self.class_object.__dict__))
            print(f'Class instance {self.class_object} saved into {filename}.')
        except Exception as e:
            raise e

    def load(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    self.class_object.__dict__ = eval(line)
            print(f'Class instance {self.class_object} loaded.')
        except Exception as e:
            raise e

            