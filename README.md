# valo_api

<div align="center">

[![Build status](https://github.com/raimannma/ValorantAPI/workflows/build/badge.svg?branch=master&event=push)](https://github.com/raimannma/ValorantAPI/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/valo_api.svg)](https://pypi.org/project/valo_api/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/raimannma/ValorantAPI/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/raimannma/ValorantAPI/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/raimannma/ValorantAPI/releases)
[![License](https://img.shields.io/github/license/raimannma/ValorantAPI)](https://github.com/raimannma/ValorantAPI/blob/master/LICENSE)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/3b23d2a3b1694356bc95255a2edb83e6)](https://www.codacy.com/gh/raimannma/ValorantAPI/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=raimannma/ValorantAPI&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/3b23d2a3b1694356bc95255a2edb83e6)](https://www.codacy.com/gh/raimannma/ValorantAPI/dashboard?utm_source=github.com&utm_medium=referral&utm_content=raimannma/ValorantAPI&utm_campaign=Badge_Coverage)
[![Downloads](https://pepy.tech/badge/valo-api)](https://pepy.tech/project/valo-api)

Valorant API Wrapper for https://github.com/Henrik-3/unofficial-valorant-api

</div>

## Installation

    pip install valo-api

If you want to use the async functions, you need to install the `aiohttp` package.

    pip install valo-api[async]

## Documentation

### Hosted

The documentation is hosted here: https://raimannma.github.io/ValorantAPI/

### From Source

After installing the package dependencies `pip install -r requirements.txt`, you can use the following commands to get the documentation:

    cd docs/ && make html

Open the index.html file in the docs/_build/html/ directory.
