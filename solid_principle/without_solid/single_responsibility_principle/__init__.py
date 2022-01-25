from srp import Trainer

if __name__ == "__main__":

    print("This example shows how one class is doing everything and not using Single Responsibility Principle")
    trainer = Trainer("ujesh" , 25)
    trainer.diet_sender()
    trainer.send_schedual()
    trainer.reward_calculator()