import pandas as pd
import matplotlib.pyplot as plt
from log import logging

class BigMacStats:
    @logging
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)

    @logging
    def preprocess_data(self):

        self.data = self.data[['name', 'dollar_price']].dropna()

    @logging
    def histogram(self):
        grouped_data = self.data.groupby('name')['dollar_price'].mean().sort_values()

        # Настройка графика
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor('blue')
        ax.set_facecolor('blue')
        bars = ax.barh(grouped_data.index, grouped_data.values, color='white', edgecolor='black', hatch='//////', height=0.5)

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.set_title('Стоимость бигмака', color='white')
        ax.set_xlabel('Стоимость (USD)', color='white')
        ax.set_ylabel('Страны', color='white')

        plt.tight_layout()
        plt.show()

bg = BigMacStats('BigmacPrice.csv')
bg.preprocess_data()
bg.histogram()
