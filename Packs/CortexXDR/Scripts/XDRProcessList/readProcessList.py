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


def read_xdr_context():
    CONTEXT_PATH_TO_READ_PROCESS_FILE_NAME_FROM_XDR_Data = "PaloAltoNetworksXDR.ScriptResult"
    # can be a dict if we have only one scriptResult
    script_results = demisto.get(demisto.context(), CONTEXT_PATH_TO_READ_PROCESS_FILE_NAME_FROM_XDR_Data)
    if not isinstance(script_results, list):
        script_results = [script_results]


    last_executed_script = script_results[-1]
    results = last_executed_script.get('results', [])
    demisto.info(f'\n\n{script_results}\n {os.getcwd()}\n')
    # if command_results:
    #     return('\n'.join(map(str,command_results)))
    # else:
    return ""

def main():
    print('hello')


if __name__ == '__main__':
    main()
