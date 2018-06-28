from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, Activation, AveragePooling2D
from keras.models import Sequential
from keras.optimizers import SGD


def get_cnn_model(img_width, img_height, num_color_channels):
    model = Sequential()
    model.add(
        Conv2D(
            32,
            kernel_size=(3, 3),
            activation='relu',
            input_shape=(img_height, img_width, num_color_channels),
        )
    )
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(3))
    model.add(Activation('sigmoid'))

    model.compile(
        loss='mean_squared_error',
        optimizer=SGD(lr=0.1, momentum=0.9),
        metrics=['mean_absolute_error']
    )
    return model


def get_ann_model(img_width, img_height, num_color_channels):
    model = Sequential()
    model.add(Flatten(input_shape=(img_width, img_height, num_color_channels)))

    model.add(Dense(3))
    model.add(Activation('sigmoid'))

    model.compile(
        loss='mean_squared_error',
        optimizer=SGD(lr=0.1, momentum=0.9),
        metrics=['mean_absolute_error']
    )
    return model
