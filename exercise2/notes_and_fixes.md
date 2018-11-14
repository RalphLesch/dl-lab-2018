# General
## Links
- [TensorFlow / Keras tutorial @github](https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/03C_Keras_API.ipynb)
- [Keras API documentation](https://www.tensorflow.org/api_docs/python/tf/keras)
- [Visualize Model Training History in Keras](https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/)


## SSH connection
### SSH key config
- create ssh key: `ssh-keygen -t rsa -b 4096 -C "comment or email" [-f file]`
- config multiple keys in `~/.ssh/config`:
```
Host <shortname>
    HostName <address>
    User <username>
    IdentityFile <ssh-file-path>
```

### SSH session
- password only once per session:
  ```Shell
  ssh-agent $SHELL # Run the shell with ssh agent 
  ssh-add -l       # List keys
  ssd-add [file]   # Add key (id_rsa by default)
  ```
- copy files (sync with remote): `scp file username@login.informatik.uni-freiburg.de:~/folder/`
- remote shell:
    ```Shell
    ssh username@login.informatik.uni-freiburg.de  # Login
    ssh tfpoolxx  # Change from main server to pool pc
    ```
- start configured virtualenv: `source /project/ml_ws1819/$USER/venv3/bin/activate`
- run commands, run python file with `python3 file`
- exit venv: `deactivate`


# Excercise 2

## Setup
1. Connect to the main server
      ```Shell
      ssh username@login.infor...freiburg.de
      ssh tfpool54
      ```
2. Login, and check if you can do, note that autocompletion might not work
      ```Shell
      cd /project/ml_ws1819/username
      ```
If not, contact poolmgr@infor...
Subject: deep learning lab 2018 account, username and matrikelnr

3. Create a python3 virtual env and install libraries
      ```Shell
      virtualenv --system-site-packages -p python3 venv3
      source venv3/bin/activate
      pip install tensorflow-gpu # Optional: You can also use the pre-installed 1.3 version
      pip install tensorflow     # Optional: You can also use the pre-installed 1.3 version
      pip install hpbandster
      ```

## Fixes for errors
- `virtualenv` installation fails:
    ```Shell
    virtualenv --no-site-packages -p python3 venv3
    source venv3/bin/activate
    # Current tensorflow-gpu uses cuDNN v1.7.2. On pool PCs is probably a lower version 1.7.0 (or similar) installed.
    pip install tensorflow-gpu==1.6.0  # Uses Current tensorflow-gpu uses cuDNN 1.7
    pip install hpbandster
    ```

    Do NOT install `tensorflow` if you want to use GPU (it for CPU ONLY)!

    Check GPU support with:
    ```Python
    from tensorflow.python.client import device_lib
    print(device_lib.list_local_devices())
    ```

- pip install fails with `AttributeError: '_NamespacePath' object has no attribute 'sort'`: apply patch from https://stackoverflow.com/a/48126778 :
    - Open the `__init__.py` file from the error with vim
    - jump to line (from error) with `:<line number>`
    - change the lines:
    ```Python
    #orig_path.sort(key=position_in_sys_path)
    #module.__path__[:] = [_normalize_cached(p) for p in orig_path]
    orig_path_t = list(orig_path)
    orig_path_t.sort(key=position_in_sys_path)
    module.__path__[:] = [_normalize_cached(p) for p in orig_path_t]
    ```
    - save with `:wq`

  Then run the command again: `pip install tensorflow-gpu==1.6.0 hpbandster`


## Other commands   
- check GPU usage: `nvidia-smi -q -g 0 -d UTILIZATION -l`
