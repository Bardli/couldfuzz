from utils.skip import need_skip_torch
import configparser
from os.path import join
import subprocess
from utils.printer import dump_data
import argparse
import pandas as pd
import os
import csv
import random
from classes.tf_api import TFAPI
from classes.torch_api import TorchAPI
from classes.tf_library import TFLibrary
import pymongo
from classes.torch_api import TorchArgument
from classes.tf_api import TFArgument


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


def search_in_dataset(api_name, lib):
    flag = False
    if lib == "torch":
        data = pd.read_csv(
            "fuzzers/FreeFuzz/data/torch_data.csv"
        )
    else:
        data = pd.read_csv(
            "fuzzers/FreeFuzz/data/tf_data.csv"
        )
    for idx, row in data.iterrows():
        if api_name == row["Buggy API"]:
            flag = True
    return flag


def write_to_list(data, fname):
    #with open(f'/media/nimashiri/DATA/vsprojects/benchmarkingDLFuzzers/dataset/{fname}.txt', 'w') as file:
    with open(f'/benchmarkingDLFuzzers/dataset/{fname}.txt', 'w') as file:
        # Write each element of the list to the file
        for item in data:
            file.write(str(item) + '\n')


def convert_arg_to_code(api):
    prefix = "arg"
    args = []
    kwargs = {}
    for key in api.args.keys():
        if "parameter:" in key:
            args.append(api.args[key])
        elif key != "output_signature" and key != "input_signature":
            kwargs[key] = api.args[key]

    arg_code = ""
    arg_str = ""
    index = 0
    for arg in args:
        arg_code += arg.to_code(f"{prefix}_{index}")
        arg_str += f"{prefix}_{index},"
        index += 1
    for key, arg in kwargs.items():
        arg_code += arg.to_code(key)
        arg_str += "%s=%s," % (key, key)
    return arg_code, arg_str


def split_apis(apis_):
    # Determine the lengths of the two portions
    total_length = len(apis_)
    portion_80_percent = int(total_length * 0.8)
    portion_20_percent = total_length - portion_80_percent

    # Randomly select elements for the 80% portion
    portion_80 = random.sample(apis_, portion_80_percent)

    # Create the remaining 20% portion by excluding elements already in the 80% portion
    portion_20 = [item for item in apis_ if item not in portion_80]
    return portion_80, portion_20


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="FreeFuzz: a fuzzing frameword for deep learning library"
    )
    parser.add_argument(
        "--conf", type=str, default="expr.conf", help="configuration file"
    )
    #the version param should be changed
    parser.add_argument("--release", type=str, default="v2.3.0",
                        help="Current release under test")
    parser.add_argument("--library", type=str, default="tf",
                        help="Current library under test")
    args = parser.parse_args()

    library = 'tf'
    release = 'v2.3.0'
    #to be changed
    config_name = "demo_tf.conf"
    freefuzz_cfg = configparser.ConfigParser()
    freefuzz_cfg.read(join(__file__.replace(
        "FreeFuzz.py", "config"), config_name))

    libs = freefuzz_cfg["general"]["libs"].split(",")
    print("Testing on ", libs)

    mongo_cfg = freefuzz_cfg["mongodb"]
    host = mongo_cfg["host"]
    port = int(mongo_cfg["port"])

    # output configuration
    output_cfg = freefuzz_cfg["output"]



    output_dir = (
        #f"/media/nimashiri/SSD/testing_results/FreeFuzz/{args.library}/{args.release}"
        f"testing_results/FreeFuzz/{args.library}/{args.release}"
    )

    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    if "torch" in args.library:

        # database configuration
        from classes.database import TorchDatabase

        TorchDatabase.database_config(host, port, mongo_cfg["torch_database"])
        DB = pymongo.MongoClient(host=host, port=port)[mongo_cfg["torch_database"]]
        apis_ = TorchDatabase.get_api_list()

        # [train_apis, test_apis] = split_apis(apis_)

        # write_to_list(train_apis, args.release+"_train")
        # write_to_list(test_apis, args.release+"_test")

        for api_name in apis_:
            # flag = search_in_dataset(api_name, "torch")
            records = DB[api_name].find()
            for record in records:
                seed_id = str(record['_id'])
                record.pop("_id")
                api = TorchAPI(api_name, record)
                # arg_d = generate_args_from_record_tf(record)

                api_code = api.my_to_code()
                arg_code, arg_str = convert_arg_to_code(api)
                flag = True
                print(api_name)
                if need_skip_torch(api_name):
                    continue
                if flag:
                    try:
                        res = subprocess.run(
                            [
                                "python3",
                                #"/media/nimashiri/DATA/vsprojects/benchmarkingDLFuzzers/fuzzers/FreeFuzz/src/FreeFuzz_api.py",
                                "FreeFuzz_api.py",
                                config_name,
                                "torch",
                                api_name,
                                args.release,
                                seed_id
                            ],
                            shell=False,
                            timeout=100,
                        )
                    except subprocess.TimeoutExpired:
                        dump_data(f"{api_name}\n", join(
                            output_dir, "timeout.txt"), "a")
                    except Exception as e:
                        dump_data(
                            f"{api_name}\n  {e}\n",
                            join(output_dir, "runerror.txt"),
                            "a",
                        )
                    else:
                        if res.returncode != 0:
                            dump_data(
                                f"{api_name}\n", join(
                                    output_dir, "runcrash.txt"), "a"
                            )

                            buggy_path = f"{output_dir}/FreeFuzz_bugs"

                            if not os.path.exists(buggy_path):
                                os.makedirs(buggy_path, exist_ok=True)

                            command_ = (
                                f"cp -r {output_dir}/temp.py {buggy_path}/{api_name}.py"
                            )
                            subprocess.call(command_, shell=True)

                            new_name = f"{buggy_path}/{api_name}.py"
                            data_ = [api.api, arg_code, arg_str,
                                     api_code, new_name, 'bug']
                            if not os.path.exists("benchmarkingDLFuzzers/dataset"):
                                os.makedirs("benchmarkingDLFuzzers/dataset", exist_ok=True)
                            #with open(f'/media/nimashiri/DATA/vsprojects/benchmarkingDLFuzzers/dataset/torch-{args.release}.csv', 'a', newline='\n') as fd:
                            with open(f'benchmarkingDLFuzzers/dataset/torch-{args.release}.csv', 'a', newline='\n') as fd:
                                writer_object = csv.writer(fd)
                                writer_object.writerow(data_)

    if "tf" in args.library:
        # database configuration
        from classes.database import TFDatabase

        TFDatabase.database_config(host, port, mongo_cfg["tf_database"])
        DB = pymongo.MongoClient(host=host, port=port)[
            mongo_cfg["tf_database"]]
        apis_ = TFDatabase.get_api_list()

        # [train_apis_tf, test_apis_tf] = split_apis(apis_)

        # write_to_list(train_apis_tf, args.release+"_train")
        # write_to_list(test_apis_tf, args.release+"_test")

        for api_name in apis_:
            #print(apis_)
            # flag = search_in_dataset(api_name, "torch")
            records = DB[api_name].find()
            for record in records:
                seed_id = str(record['_id'])
                record.pop("_id")
                # arg_d = generate_args_from_record_tf(record)
                api = TFAPI(record)
                api_code = api.my_to_code()
                arg_code, arg_str = convert_arg_to_code(api)
                flag = True
                # flag = search_in_dataset(api_name, "tf")
                #print(api_name)
                if flag:
                    try:
                        res = subprocess.run(
                            [
                                "python3",
                                #"/media/nimashiri/DATA/vsprojects/benchmarkingDLFuzzers/fuzzers/FreeFuzz/src/FreeFuzz_api.py",
                                "FreeFuzz_api.py",
                                config_name,
                                "tf",
                                api_name,
                                args.release,
                                seed_id
                            ],
                            shell=False,
                            timeout=100,
                        )
                    except subprocess.TimeoutExpired:
                        dump_data(f"{api_name}\n", join(
                            output_dir, "timeout.txt"), "a")
                    except Exception as e:
                        dump_data(
                            f"{api_name}\n  {e}\n", join(
                                output_dir, "runerror.txt"), "a"
                        )
                    else:
                        if res.returncode != 0:
                            dump_data(
                                f"{api_name}\n", join(
                                    output_dir, "runcrash.txt"), "a"
                            )

                            buggy_path = f"{output_dir}/FreeFuzz_bugs"

                            if not os.path.exists(buggy_path):
                                os.makedirs(buggy_path, exist_ok=True)

                            command_ = (
                                f"cp -r {output_dir}/temp.py {buggy_path}/{api_name}.py"
                            )
                            subprocess.call(command_, shell=True)

                            new_name = f"{buggy_path}/{api_name}.py"
                            data_ = [api.api, arg_code, arg_str,
                                     api_code, new_name, 'bug']
                            '''data_ = [api_name, arg_code, arg_str,
                                     api_code, new_name, 'bug']'''
                            #with open(f'/media/nimashiri/DATA/vsprojects/benchmarkingDLFuzzers/dataset/tf-{args.release}.csv', 'a', newline='\n') as fd:
                            with open(f'benchmarkingDLFuzzers/dataset/tf-{args.release}.csv', 'a', newline='\n') as fd:
                                writer_object = csv.writer(fd)
                                writer_object.writerow(data_)

    not_test = []
    for l in libs:
        if l not in ["tf", "torch"]:
            not_test.append(l)
    if len(not_test):
        print(f"WE DO NOT SUPPORT SUCH DL LIBRARY: {not_test}!")
