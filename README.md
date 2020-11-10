[![Github Actions Status](https://github.com/n8creator/python-project-lvl2/workflows/Python%20CI/badge.svg)](https://github.com/n8creator/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/1377ea5314f87c02aa00/maintainability)](https://codeclimate.com/github/n8creator/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1377ea5314f87c02aa00/test_coverage)](https://codeclimate.com/github/n8creator/python-project-lvl2/test_coverage)
![Actions Status](https://github.com/n8creator/python-project-lvl2/workflows/hexlet-check/badge.svg)

# Generate Difference CLI
Generate Difference Script allows you find the difference between two files in ```.json``` or ```.yaml/.yml``` formats. 

The output may be given in formats:
1. Standard - the output shown as a tree with a difference between nodes. Standard output used as default.
2. Plain - output shown as a multiple strings. Use key ```-f plain``` or ```--format plain``` in CLI to display in plain format.
3. JSON - output shown in ```.json``` format. Use key ```-f json``` or ```--format json``` in CLI to display in plain format.

## Installation
Run following command in Bash to install the script:
```
pip install --no-cache-dir --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple n8creator-gendiff
```


## Examples of usage
### 1. Plain files with **Standard format** output (as a Tree)
[![asciicast](https://asciinema.org/a/OrWS1wJmte1xW8OEru2ZZd8QJ.svg)](https://asciinema.org/a/OrWS1wJmte1xW8OEru2ZZd8QJ)

### 2. Nested files with **Standard format** output (as a Tree)
[![asciicast](https://asciinema.org/a/fWbpN3CTOdsregXo7Ks7a3fCG.svg)](https://asciinema.org/a/fWbpN3CTOdsregXo7Ks7a3fCG)

### 3. Nested files with **Plain format** output (as a multiple strings)
[![asciicast](https://asciinema.org/a/mxVigkK0WQzAIaUnusyUnJg2w.svg)](https://asciinema.org/a/mxVigkK0WQzAIaUnusyUnJg2w)


### 4. Nested files with **JSON format** output (standard JSON file)
[![asciicast](https://asciinema.org/a/69tyczf9uMbzHtGnfnu3IoeQO.svg)](https://asciinema.org/a/69tyczf9uMbzHtGnfnu3IoeQO)