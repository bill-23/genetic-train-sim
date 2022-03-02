import logging
from train.train import Train
from display.manual_control import ManualController


if __name__=='__main__':

    logging.basicConfig(level=logging.NOTSET)

    log = logging.getLogger(__name__)

    train_one = Train()

    manual_controller = ManualController(train=train_one)

    manual_controller.mainloop()
    
