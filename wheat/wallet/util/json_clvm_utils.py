from typing import Any

from wheat.types.blockchain_format.program import Program


def json_to_wheatlisp(json_data: Any) -> Any:
    list_for_wheatlisp = []
    if isinstance(json_data, list):
        for value in json_data:
            list_for_wheatlisp.append(json_to_wheatlisp(value))
    else:
        if isinstance(json_data, dict):
            for key, value in json_data:
                list_for_wheatlisp.append((key, json_to_wheatlisp(value)))
        else:
            list_for_wheatlisp = json_data
    return Program.to(list_for_wheatlisp)
