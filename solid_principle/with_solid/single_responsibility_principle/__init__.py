from trainer import Trainer
from schedual_sender import SchedualSender
from diet_sender import DietSender
from reward_calculator import RewardCalculator

if __name__ == '__main__':

    print("This module use the Single Responsibility Principle to design the feature.")
    trainer = Trainer('ujesh', 25)
    schedual_sender = SchedualSender()
    schedual_sender.send_schedual(trainer)

    diet_sender = DietSender()
    diet_sender.diet_sender(trainer)

    reward_calculator = RewardCalculator()
    reward_calculator.calculate_reward(trainer)
    """
    Now, we can add N number of functionality for trainer and each functionality is independent to each
    other low coupling can also be achieved.
    """




