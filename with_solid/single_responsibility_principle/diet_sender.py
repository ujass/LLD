from trainer import Trainer

class DietSender:
    """
    This class is responsible to send the diet only.
    This does not care who the trainer is.
    """

    def diet_sender(self, trainer: Trainer):
        print(f'diet is sent by trainer {trainer.name}')