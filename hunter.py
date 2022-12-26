import simfin as sf
import pandas as pd


class ZombieHunter:
    MARKETS = ['us', 'germany', 'canada', 'china']
    def __init__(self):
        key = 'p84KvYhpzCeiudDOdfK21aHA8IRx7sYC'
        sf.set_api_key(key)
        sf.set_data_dir('~/simfin_data/')


    @staticmethod
    def find_zombies(market):
        df = sf.load_income(variant='annual', market=market)
        df = df[df['Interest Expense, Net'] > 0]
        df['Interest Coveraga Ratio'] = df['Operating Income (Loss)'] / df['Interest Expense, Net']
        df = df[df['Interest Coveraga Ratio'] < 1]
        return df


    @staticmethod
    def rank_zombies(df):
        return df.sort_values(by='Interest Coveraga Ratio')


    def hunt_zombies(self, market):
        zombies = self.find_zombies(market)
        zombies.to_csv('zombies.csv')
        ranked_zombies = self.rank_zombies(zombies)
        ranked_zombies.to_csv('ranked_zombies.csv')


if __name__ == '__main__':
    hunter = ZombieHunter()
    hunter.hunt_zombies('us')


