from trainer import Trainer

class RewardCalculator:
    """This class will calculate the reward for the trainer."""
    def calculate_reward(self, trainer: Trainer):
        print(f'calculating reward for {trainer.name}')

