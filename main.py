import logging
from train.train import Train
from display.manual_control import ManualController
from exc.exceptions import TrainSimInvalidInputError


if __name__=='__main__':

    # Set up logging here, all other modules will use it
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    # Create a new train
    train_one = Train()

    # Create the manual controller and pass it the train
    manual_controller = ManualController(train=train_one)

    # Start the controller
    manual_controller.mainloop()
    
