# zenodoclient

[![Build Status](https://github.com/shh-dlce/zenodoclient/workflows/tests/badge.svg)](https://github.com/shh-dlce/zenodoclient/actions?query=workflow%3Atests)
[![PyPI](https://img.shields.io/pypi/v/zenodoclient.svg)](https://pypi.org/project/zenodoclient)

# Usage

Install this package either from the repository (run, after cloning the repository, `python setup.py install`) or using `pip`. Then create an API access token [here](https://zenodo.org/account/settings/applications/tokens/new/). Then:
```
zenodo --access-token $YOURTOKEN ls
```
