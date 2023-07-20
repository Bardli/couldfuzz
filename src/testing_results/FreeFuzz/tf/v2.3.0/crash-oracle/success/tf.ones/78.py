import tensorflow as tf
try:
  arg_0_0 = 3
  arg_0 = [arg_0_0,]
  results["res"] = tf.ones(arg_0,)
except Exception as e:
  results["err"] = "Error:"+str(e)
