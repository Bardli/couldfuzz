import tensorflow as tf
try:
  arg_0 = 2
  arg_1 = 4
  results["res"] = tf.ones(arg_0,arg_1,)
except Exception as e:
  results["err"] = "Error:"+str(e)
