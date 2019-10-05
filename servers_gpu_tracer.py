import argparse
import spur
from pprint import pprint
import re


def get_args():
    """! Command line parser """
    parser = argparse.ArgumentParser(
        description='Tracing GPU utilization in specified servers')
    parser.add_argument("--servers_list", "-sl", type=str, nargs='+',
                        help="List of servers you wish to trace their "
                             " GPU utilization",
                        required=True)
    parser.add_argument("--username", "-u", type=str,
                        help="Your username on these servers.",
                        required=True)
    parser.add_argument("--password", "-p", type=str,
                        help="Your password on these servers.",
                        required=True)
    parser.add_argument("--verbosity", "-v", type=int,
                        help="Select how verbose you want the output. "
                             "The highest verbosity would output all "
                             "nvidia-smi outputs for all specified "
                             "servers.",
                        choices=[0, 1], default=0)
    return parser.parse_args()


def trace_server(server, username, password, verbosity):
    try:
        print('\n' + 'GPUs on: {}'.format(server))
        print('='*50 + '\n')
        shell = spur.SshShell(hostname=server, username=username,
                              password=password)
        result = shell.run(["nvidia-smi"])
        lines = ''.join(result.output.decode('utf-8'))
        if verbosity > 0:
            print(lines)
        else:
            k = 0
            broken_lines = lines.split('\n')
            for i, line in enumerate(broken_lines):
                utils = re.findall('[0-9]+\%', line)
                if len(utils) > 0:
                    gpu_util = utils[-1]
                    mem_util = re.findall(
                        '[0-9]+MiB / [0-9]+MiB', line)[-1]
                    print('CUDA{} -- UTILIZATION: {} MEMORY '
                          'CONSUMPTION: {}'.format(k, gpu_util, mem_util))
                    k += 1

    except Exception as e:
        print('Failed to trace GPU utilization for server: {}'
              '.'.format(server))
        print(e)

if __name__ == "__main__":
    args = get_args()
    for server in args.servers_list:
        trace_server(server, args.username, args.password, args.verbosity)
