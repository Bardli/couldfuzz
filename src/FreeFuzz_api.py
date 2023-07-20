import sys
from constants.enum import OracleType
import configparser
from os.path import join
from utils.converter import str_to_bool
import os
import pymongo
from classes.torch_api import TorchArgument
from classes.tf_api import TFArgument
from bson import ObjectId


def generate_args_from_record_tf(record: dict) -> dict:
    args = {}
    for key in record.keys():
        if key != "output_signature":
            args[key] = TFArgument.generate_arg_from_signature(
                record[key])
    return args


def generate_args_from_record_torch(record: dict) -> dict:
    args = {}
    for key in record.keys():
        if key != "output_signature":
            args[key] = TorchArgument.generate_arg_from_signature(
                record[key])
    return args


if __name__ == "__main__":
    config_name = sys.argv[1]
    library = sys.argv[2]
    api_name = sys.argv[3]
    release = sys.argv[4]
    seed_id = sys.argv[5]
    freefuzz_cfg = configparser.ConfigParser()
    freefuzz_cfg.read(join(__file__.replace(
        "FreeFuzz_api.py", "config"), config_name))

    # database configuration
    mongo_cfg = freefuzz_cfg["mongodb"]
    host = mongo_cfg["host"]
    port = int(mongo_cfg["port"])

    # oracle configuration
    oracle_cfg = freefuzz_cfg["oracle"]
    crash_oracle = str_to_bool(oracle_cfg["enable_crash"])
    cuda_oracle = str_to_bool(oracle_cfg["enable_cuda"])
    precision_oracle = str_to_bool(oracle_cfg["enable_precision"])

    diff_bound = float(oracle_cfg["float_difference_bound"])
    time_bound = float(oracle_cfg["max_time_bound"])
    time_thresold = float(oracle_cfg["time_thresold"])

    # output configuration
    output_cfg = freefuzz_cfg["output"]
    # torch_output_dir = output_cfg["torch_output"]
    # tf_output_dir = output_cfg["tf_output"]

    tf_output_dir = f"testing_results/FreeFuzz/{library}/{release}"
    torch_output_dir = f"testing_results/FreeFuzz/{library}/{release}"

    # mutation configuration
    mutation_cfg = freefuzz_cfg["mutation"]
    enable_value = str_to_bool(mutation_cfg["enable_value_mutation"])
    enable_type = str_to_bool(mutation_cfg["enable_type_mutation"])
    enable_db = str_to_bool(mutation_cfg["enable_db_mutation"])
    each_api_run_times = int(mutation_cfg["each_api_run_times"])

    if library.lower() in ["pytorch", "torch"]:
        import torch
        from classes.torch_library import TorchLibrary
        from classes.torch_api import TorchAPI
        from classes.database import TorchDatabase
        from utils.skip import need_skip_torch

        DB = pymongo.MongoClient(host=host, port=port)[
            mongo_cfg["torch_database"]]

        TorchDatabase.database_config(host, port, mongo_cfg["torch_database"])

        if cuda_oracle and not torch.cuda.is_available():
            print("YOUR LOCAL DOES NOT SUPPORT CUDA")
            cuda_oracle = False
        # Pytorch TEST
        MyTorch = TorchLibrary(torch_output_dir, diff_bound, time_bound,
                               time_thresold)
        for _ in range(each_api_run_times):
            document_id = ObjectId(seed_id)
            record = DB[api_name].find_one({"_id": document_id})
            record.pop('_id')
            api = TorchAPI(api_name, record)
            api.mutate(enable_value, enable_type, enable_db)
            if crash_oracle:
                MyTorch.test_with_oracle(api, OracleType.CRASH)
            if cuda_oracle:
                MyTorch.test_with_oracle(api, OracleType.CUDA)
            if precision_oracle:
                MyTorch.test_with_oracle(api, OracleType.PRECISION)
    elif library.lower() in ["tensorflow", "tf"]:

        import tensorflow as tf
        from classes.tf_library import TFLibrary
        from classes.tf_api import TFAPI
        from classes.database import TFDatabase
        from utils.skip import need_skip_tf


        DB = pymongo.MongoClient(host=host, port=port)[
            mongo_cfg["tf_database"]]

        TFDatabase.database_config(host, port, mongo_cfg["tf_database"])

        #if cuda_oracle and not tf.test.is_gpu_available():
        if cuda_oracle and tf.config.list_physical_devices('GPU')==[]:
            print("YOUR LOCAL DOES NOT SUPPORT CUDA")
            cuda_oracle = False

        MyTF = TFLibrary(tf_output_dir, diff_bound, time_bound,
                         time_thresold)
        print(api_name)
        if need_skip_tf(api_name):
            pass
        else:
            for _ in range(each_api_run_times):

                document_id = ObjectId(seed_id)
                record = DB[api_name].find_one({"_id": document_id})
                record.pop('_id')
                api = TFAPI(record)
                api.api = api_name

                api.mutate(enable_value, enable_type, enable_db)
                if crash_oracle:

                    MyTF.test_with_oracle(api, OracleType.CRASH)
                if cuda_oracle:

                    MyTF.test_with_oracle(api, OracleType.CUDA)
                if precision_oracle:

                    MyTF.test_with_oracle(api, OracleType.PRECISION)
    else:
        print(f"WE DO NOT SUPPORT SUCH DL LIBRARY: {library}!")
