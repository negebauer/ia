import itertools
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


class Log:

    def __init__(self, name):
        self.name = name
        self.log_name = name + '.log'
        self.clear()

    def clear(self):
        open(self.log_name, 'w').close()

    def log(self, line):
        with open(self.log_name, 'a') as file:
            file.write('{}\n'.format(line))

    def plot_confusion_matrix(self, cm, classes, imagename,
                              title='Confusion matrix',
                              normalize=False,
                              cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        plt.figure(figsize=(5, 5))
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i, j],
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

        open(imagename, 'w').close()
        plt.savefig(imagename)
        plt.close()
