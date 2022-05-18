import json
import pytest


@pytest.mark.parametrize('_return_value , res', [('test_data/process_list.json', 'test_data/process_list.md')])
def test_entries_to_markdown(_return_value, res):
    """
    Given:
        - _return_values a process list
    When:
        - running the automation
    Then:
        - parse the _return_value string entries and return them in a markdown format
    """
    from readProcessList import entries_to_markdown
    with open(_return_value, 'r') as process_list_from_xdr:
        # Reading from json file
        proces_list = json.load(process_list_from_xdr)
    entries_as_md = entries_to_markdown(proces_list)
    with open(res, 'r') as res_md:
        res_md = res_md.read()
    assert res_md == entries_as_md


@pytest.mark.parametrize('script_results , res', [
    ('test_data/filter_script_results.json', 'test_data/script_results.json'),
    ('test_data/filter_script_results_one_obj.json', 'test_data/res_filter_script_results_one_obj.json')
])
def test_find_last_process_list_script(script_results, res):
    """
        Given:
            - script_results
        When:
            - after running a script on the XDRIR integration
        Then:
            - choose the last script that is related to the process list.
            (contains the Name,CPU,Memory in the entry).
        """
    from readProcessList import find_last_process_list_script
    with open('test_data/script_results.json') as f:
        script_results = json.load(f)
    script_result = find_last_process_list_script(script_results)
    with open('test_data/filter_script_results.json', 'r') as res:
        filter_res = json.load(res)
    assert filter_res == script_result
