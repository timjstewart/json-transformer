# json-transformer

Transforms one or more JSON documents into a text file using templates.

## Installation

_Note: tested with python version 3.10_

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Example

Run:
```
python transform.py --data=foo:examples/one.json --data=bar:examples/two.json --template=examples/simple.template 
```

Output:
```
<people>
  <person>
    <name>Tim</name>
  </person>
  <person>
    <name>Maxwell</name>
  </person>
</people>
```

## Templates

See the [Jinja2 Documentation](https://jinja.palletsprojects.com/en/3.1.x/templates) for template syntax.

Templates can access a single top-level attribute named `d`.

When a JSON file is specified on the command line, it is prefixed by its alias.
For example, in `--data=foo:examples/one.json`, data is the alias that will be
used to access data loaded from `examples/one.json`. Data loaded from
`examples/one.json` will be accessible in the template via `d.foo`.
