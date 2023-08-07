#!/usr/bin/env python3

import os
import rospkg
import yaml

if __name__ == '__main__':

    rospack = rospkg.RosPack()
    path = rospack.get_path('kuka_battery_setup_tests')
#    path = path + "/unscrewing/config/trees/unscrewing_trees"
    path = path + "/unscrewing/config/params/unscrewing_params"
    files_names = os.listdir(path)

    n = 000

    for file_name in files_names:
        if ("template" in file_name):
            with open(path + '/' + file_name, "r") as stream:
                file_str = stream.read()
#                print(file_str)

            param_file = file_name.replace('template', 'params')
            param_file = param_file.replace('xml', 'yaml')

            with open(path + '/' + param_file) as file:
                yaml_file = yaml.load(file, Loader=yaml.FullLoader)

            for n in range(len(yaml_file[list(yaml_file.keys())[0]])):
                for param in yaml_file.keys():
#                    print(yaml_file[param][n])
                    new_file_str = file_str.replace(param, yaml_file[param][n])
#                    print(new_file_str)

                    new_name = file_name.replace('template', str(format(n + 1, '03d')))
                    with open(path + '/' + new_name, 'w') as file:
                        file.write(new_file_str)

    exit()
