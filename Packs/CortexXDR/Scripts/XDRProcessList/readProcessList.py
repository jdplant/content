import json
from typing import List
from CommonServerPython import *


def entries_to_markdown(entry_list: List[str]):
    """
       Args:
        entry_list (List[str]): the _return_value array from demisto context

    Returns:
        str: a markdown table to be displayed on the layout.

    """
    process_list = []
    for entry in entry_list:
        start_cpu = entry.find('CPU')
        end_cpu = start_cpu + 5
        start_memory = entry.find('Memory')
        end_memory = start_memory + 8
        process_list.append({
            'Name': entry[6:start_cpu-2],
            'CPU': entry[end_cpu:start_memory-2],
            'Memory': entry[end_memory: len(entry)]
        })
    md = tableToMarkdown('Process list', process_list, ['Name', 'CPU', 'Memory'])
    return md



def main():
    print('hello')


if __name__ == '__main__':
    main()
