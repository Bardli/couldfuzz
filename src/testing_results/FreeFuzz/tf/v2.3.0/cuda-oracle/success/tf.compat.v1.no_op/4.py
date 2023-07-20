results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      name = "Addons>SkipGramGenerateCandidates"
      results["res_cpu"] = tf.compat.v1.no_op(name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      results["res_gpu"] = tf.compat.v1.no_op(name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
