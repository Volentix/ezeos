# EZEOS

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)

#### _A simple testing/learning tool for EOS._

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Contribute](#contribute)
- [License](#license)

## Background

The tool was created as a means to quickly and easily experiment with EOSIO on mac or linux on the main or test net.
This version does not create a local node for you, but you can connect to it if you run it separately.
You can explore the EOSIO blockchain, create wallets and import keys, create accounts, view account balance,
get tables and use a contract to transfer funds to a ledger. 


1. Install EOSIO (v1.4.1) in the `~/eos` directory
3. Python3
3. PyQt5
2. pip3 install pexpect
3. pip3 install requests
4. pip3 install pyte
5. pip3 install psutil

## Usage

At the root of this project:

```
cd src
```

Run:
```
python3 ezeos.py
```

Happy hacking!

## Maintainers

[@sylvaincormier](https://github.com/sylvaincormier)

## Contribute

If you are interested in contributing, please read [the code of conduct file](code-of-conduct.md).

PRs are accepted, but be aware that the tool currently meets our very limited needs and so our time to review is limited. We decided to share it with the open source community in the hopes that it would be as useful for others as it has been for us. You are encouraged to fork it and make a go of it on your own. Having said that, we would love to hear from you about your efforts! If we can help we will!

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2018 VolentixLabs
