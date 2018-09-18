# AWD - The awesome AWS resource descriptor

AWD is an utility tool that helps you list down AWS resources in a pretty print.

### Technology

AWD is a python based tool and expects the below to be available in the machine.
*   python3<br>
    Please refer [python installation docs](https://wiki.python.org/moin/BeginnersGuide/Download) for more details
*   [pip3](https://en.wikipedia.org/wiki/Pip_(package_manager))

## Installation
We strongly recommend the use of virtual environments for python based libraries.

Follow the below steps

*   Ensure that a python3 based virtual environment is already set up
*   Download the project source
*   Navigate to the project root (the place where the .git folder is, yeah)
*   `pip install --editable .`<br>
    (you do not need to say pip3 install since you are in the python3 virtualenv)<br>
    **NOTE:** The '.' in the above command refers to the current working directory

### Installation Verification

Execute
```bash
awd --version
```

Expect
```bash
awd, version 0.1
```
## Hop on !
Try the following command to list down the commands available to You

```bash
awd --help
```
