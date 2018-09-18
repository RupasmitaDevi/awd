# AWD - The awesome AWS resource descriptor

AWD is an utility tool that helps you list down AWS resources in a pretty print.

### Technology

AWD is a python based tool and expects the below to be available in the machine.
*   python3<br>
    Please refer [python installation docs](https://wiki.python.org/moin/BeginnersGuide/Download) for more details
*   [pip3](https://en.wikipedia.org/wiki/Pip_(package_manager)

## Installation
We strongly recommend the use of virtual environments for python based libraries.<br>
Since, AWD is built on top of python3 and the default installation of python on any OS is still python2, it is all the more important.<br>
There are many ways to set up virtual environment, we recommend using the **[virtualenv wrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)**

To Set up a virtual environment follow the below:

*   Install `virtualenvwrapper` if you haven't already. Remember to install it using python3
*   Execute the below commands :
    *   Create a new virtual environment</br>
        ```bash
        mkvirtualenv dosa
        ```
    *   If you already have set up the virtual env, switch to the created virtual environment
        ```
        workon dosa
        ```
*   You can jump out of the virtual environment anytime, by executing the below when you are within the virtual environment
    ```bash
    deactivate
    ```
#### Why virtual environments

    We had previously touched up on this saying virtual environment is necessary when you are working on python3, when the majority of the industry is still @ python2. But there is more to this than just that.

    Python applications will often use packages and modules that don’t come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library’s interface.

    This means it may not be possible for one Python installation to meet the requirements of every application. Soon requirements of multiple python libraries installed can get into conflicts.<br>
    The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.<br>
    Different applications can then use different virtual environments.
### Installing

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
