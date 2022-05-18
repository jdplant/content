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


def find_last_process_list_script(script_results):
    if not isinstance(script_results, list):
        [script_results]
    for script_result in reversed(script_results):
        if not (results := script_result.get('results', [])):
            continue
        result = results[-1]
        if not (_return_value := result.get('_return_value', [])):
            continue
        if 'Name' and 'Memoty' and 'CPU' in _return_value[0]:
            return _return_value
    return None


def main():
    _return_value = find_last_process_list_script([])
    entries_to_markdown(_return_value)

if __name__ == '__main__':
    main()
