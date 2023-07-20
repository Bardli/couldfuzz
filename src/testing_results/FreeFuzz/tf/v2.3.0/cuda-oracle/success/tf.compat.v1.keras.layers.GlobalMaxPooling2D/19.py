results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      data_format = "sum"
      keepdims = False
      results["res_cpu"] = tf.compat.v1.keras.layers.GlobalMaxPooling2D(data_format=data_format,keepdims=keepdims,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      results["res_gpu"] = tf.compat.v1.keras.layers.GlobalMaxPooling2D(data_format=data_format,keepdims=keepdims,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
