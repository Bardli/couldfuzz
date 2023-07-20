import tensorflow as tf
try:
  bin_boundaries = None
  num_bins = 1024
  epsilon = None
  results["res"] = tf.compat.v1.keras.layers.Discretization(bin_boundaries=bin_boundaries,num_bins=num_bins,epsilon=epsilon,)
except Exception as e:
  results["err"] = "Error:"+str(e)
