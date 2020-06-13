import math

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


class Generator:
    """Class to generate 'fly straight dammit' graph"""

    @staticmethod
    def _generate_sequence(x_lim):
        x, y = range(x_lim + 1), [1, 1]
        for x_i in x[2:]:
            if int(math.gcd(x_i, y[-1])) == 1:
                y.append(y[-1] + x_i + 1)
            else:
                y.append(int(y[-1] / math.gcd(x_i, y[-1])))
        return np.array(x), np.array(y)

    def generate_plot_and_save(self, x_lim, path):
        # sns.set(style="ticks", context="talk")
        # plt.style.use("dark_background")
        x, y = self._generate_sequence(x_lim)
        ax = sns.scatterplot(x, y, alpha=0.6)
        figure = ax.get_figure()
        figure.savefig(path, transparent=True)


if __name__ == "__main__":
    plot_generator = Generator()
    plot_generator.generate_plot_and_save(1600, 'plot.png')
