import tensorflow as tf
try:
  name = "my_acc"
  results["res"] = tf.metrics.SparseCategoricalAccuracy(name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
