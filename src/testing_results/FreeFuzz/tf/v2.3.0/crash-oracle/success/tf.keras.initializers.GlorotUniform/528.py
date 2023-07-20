import tensorflow as tf
try:
  results["res"] = tf.keras.initializers.GlorotUniform()
except Exception as e:
  results["err"] = "Error:"+str(e)
