from model.trainer import Trainer
from model.verifier import model_verifier

trainer = Trainer(sensor_name='amorphous applicator',
                  data_path='resources/data/cDAQ1Mod1_ai0')

trainer.data_plot()
trainer.train()

model_verifier(model_path='amorphous applicator.h5',
               data_path='resources/data/test')
