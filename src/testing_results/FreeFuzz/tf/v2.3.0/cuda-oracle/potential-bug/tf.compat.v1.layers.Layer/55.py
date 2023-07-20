results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      trainable = True
      name = tf.complex64
      dtype = None
      results["res_cpu"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      name = tf.complex64
      results["res_gpu"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)