from keras.callbacks import ReduceLROnPlateau

import models
from utils import get_images

train_dir = 'data'
x_train, y_train = get_images(train_dir)

num_train_samples = len(x_train)

img_width = img_height = 32
num_color_channels = 3

print('Number of examples: {}'.format(num_train_samples))
assert num_train_samples > 32


model = models.get_cnn_model(img_width, img_height, num_color_channels)
print(model.summary())

reduce_lr = ReduceLROnPlateau(
    monitor='mean_absolute_error', factor=0.5,
    patience=5, min_lr=0.001, verbose=1
)

model.fit(
    x_train,
    y_train,
    batch_size=32,
    epochs=80,
    callbacks=[reduce_lr]
)

model.save('model.h5')

