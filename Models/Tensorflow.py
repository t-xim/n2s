import tensorflow as tf

# Create the model type
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=[28,28]),
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)]);
                                    
# Choose the optimizer
model.compile(optimizer = tf.train.AdamOptimizer(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

# The predictions(?) named H
H=model.fit(X_train, y_train, epochs = 10, validation_data =(X_valid, y_valid))

# Plotting loss curve
pd.DataFrame(H.history).plot(figsize = (8,5))
plt.grid(True)
plt.gca().set_ylim(0,2)
plt.show()

plt.plot(H.history['loss'])
plt.ylabel('cost')
plt.xlabel('Epochs')
plt.title('Cost/Loss curve')
plt.show()

# Prediction
prediction = model.predict(X_test)
