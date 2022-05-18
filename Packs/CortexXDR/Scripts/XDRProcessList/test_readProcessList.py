import json
import pytest


@pytest.mark.parametrize('_return_value , res', [('process_list.json', 'process_list.md')])
def test_entries_to_markdown(_return_value, res):
    from readProcessList import entries_to_markdown
    with open(_return_value, 'r') as process_list_from_xdr:
        # Reading from json file
        proces_list = json.load(process_list_from_xdr)
    entries_as_md = entries_to_markdown(proces_list)
    with open(res, 'r') as res_md:
        res_md = res_md.read()
    assert res_md == entries_as_md
