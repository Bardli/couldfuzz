results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      data_format = "1"
      results["res_cpu"] = tf.keras.layers.GlobalAveragePooling2D(data_format=data_format,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      results["res_gpu"] = tf.keras.layers.GlobalAveragePooling2D(data_format=data_format,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
