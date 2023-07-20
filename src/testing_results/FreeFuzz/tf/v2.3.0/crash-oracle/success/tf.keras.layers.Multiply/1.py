import tensorflow as tf
try:
  results["res"] = tf.keras.layers.Multiply()
except Exception as e:
  results["err"] = "Error:"+str(e)
