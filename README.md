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

The tool was created as a means to quickly and easily experiment with a local instance of the EOS
blockchain. PLEASE do not use this for production! Private keys are freely copied and stored unencrypted
in files. This works great for this tool, not so great for security.
Tutorial here: https://youtu.be/u6l5eRRJqC0

The main functions you will find are:
1. Start/stop/flush EOS blockchains
2. Create wallets
3. Create tokens (VTX in our case)
4. Transfer the tokens to another wallet

## Install

This has been tested on Ubuntu, unsure how it will work on other platforms.

1. Install EOSIO (dawn_v4.0.0) in the `~/eos` directory
2. Python
3. PyQt4
4. Intelligent configuration of `nodeos`

## Usage

At the root of this project:

```
cd src
```

Run:
```
python EZTokenCreator.py
```

Happy hacking!

## Maintainers

[@sylvaincormier](https://github.com/sylvaincormier)

## Contribute

If you are intereted in contributing, please read [the code of conduct file](code-of-conduct.md).

PRs are accepted, but be aware that the tool currently meets our very limited needs and so our time to review is limited. We decided to share it with the open source community in the hopes that it would be as useful for others as it has been for us. You are encouraged to fork it and make a go of it on your own. Having said that, we would love to hear from you aboout your efforts! If we can help we will!

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2018 VolentixLabs
