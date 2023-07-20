import tensorflow as tf
try:
  arg_0 = "Addons>ResamplerGrad"
  results["res"] = tf.no_gradient(arg_0,)
except Exception as e:
  results["err"] = "Error:"+str(e)
