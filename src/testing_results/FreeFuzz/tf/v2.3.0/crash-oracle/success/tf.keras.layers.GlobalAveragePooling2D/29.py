import tensorflow as tf
try:
  results["res"] = tf.keras.layers.GlobalAveragePooling2D()
except Exception as e:
  results["err"] = "Error:"+str(e)
