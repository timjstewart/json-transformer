import sys
import jinja2
import json
from typing import Union, Dict, Any, Type, List

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]

_DATA = {}


def load_json(fname: str) -> JSON:
    try:
        with open(fname, "r") as data_in:
            return json.loads(data_in.read())
    except json.JSONDecodeError as ex:
        raise Exception(f"invalid JSON in file: {fname} - {ex}")


def render_template(fname: str, data) -> str:
    try:
        with open(fname, "r") as template_in:
            template = jinja2.Template(
                template_in.read(), trim_blocks=True, lstrip_blocks=True
            )
            return template.render(d=_DATA)
    except IOError as ex:
        raise Exception(f"could not open template file: {fname} - {ex}")
    except jinja2.TemplateError as ex:
        raise Exception(f"rendering template from file: {fname} {data} - {ex}")


def main():
    try:
        for arg in sys.argv[1:]:
            if "=" in arg:
                arg_name, arg_value = arg.split("=")
                if arg_name == "--data":
                    alias, fname = arg_value.split(":")
                    _DATA[alias] = load_json(fname)
                elif arg_name == "--template":
                    print(render_template(arg_value, _DATA), end="")
                else:
                    raise Exception(f"unexpected flag: {arg}")
            else:
                raise Exception(f"unexpected arg: {arg}")
    except Exception as ex:
        print(f"error: {ex}")


if __name__ == "__main__":
    main()
