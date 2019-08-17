# EZEOS

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2F4ban%2Fezeos.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2F4ban%2Fezeos?ref=badge_shield)

#### _A simple testing/learning tool for EOS._

## Table of Contents
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contribute](#contribute)
- [License](#license)

## Background

The tool was created as a means to quickly and easily experiment with EOSIO on mac or linux on the main or test net.
This version does not create a local node for you, but you can connect to it if you run it separately.
You can explore the EOSIO blockchain, create wallets and import keys, create accounts, view account balance,
get tables and use a contract to transfer funds to a ledger. 

## Install

> Requirements: EOS, EOS.CDT, Python3

* For installing EOS and EOS.CDT visit the [wiki](https://github.com/4ban/ezeos/wiki)
* install python>=3.6

if you want to use more than 4 default themes, install `ttkthemes` (optional, recommended)
* pip3 install ttkthemes

There is a possibility that you have to install additional libraries:
* pip3 install beautifulsoup4
* pip3 install moneywagon
* pip3 install requests

For the further update:
> * pip3 install Pillow
> * pip3 install SocketIO-client
> * pip3 install pyte

## Usage

At the root of this project:

Run:
```
python3 ezeos.py
```

Happy hacking!

## Screenshots

<img width="980" alt="screen shot 2019-02-13 at 1 10 11 pm" src="https://user-images.githubusercontent.com/2269864/52733675-453e8780-2f91-11e9-92c4-3eaefd4c7c35.png">
<img width="978" alt="screen shot 2019-02-13 at 1 10 26 pm" src="https://user-images.githubusercontent.com/2269864/52733676-453e8780-2f91-11e9-84b8-e28f1767507d.png">
<img width="979" alt="screen shot 2019-02-13 at 1 10 49 pm" src="https://user-images.githubusercontent.com/2269864/52733677-453e8780-2f91-11e9-8fc3-8eef87e098cb.png">
<img width="981" alt="screen shot 2019-02-13 at 1 10 57 pm" src="https://user-images.githubusercontent.com/2269864/52733678-453e8780-2f91-11e9-99ad-e4509c7014f0.png">
<img width="979" alt="screen shot 2019-02-13 at 1 11 14 pm" src="https://user-images.githubusercontent.com/2269864/52733679-466fb480-2f91-11e9-93ab-49eee41ef516.png">


## Contribute

If you are interested in contributing, please read [the code of conduct file](code-of-conduct.md).

PRs are accepted, but be aware that the tool currently meets our very limited needs and so our time to review is limited. We decided to share it with the open source community in the hopes that it would be as useful for others as it has been for us. You are encouraged to fork it and make a go of it on your own. Having said that, we would love to hear from you about your efforts! If we can help we will!

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2018 VolentixLabs

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2F4ban%2Fezeos.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2F4ban%2Fezeos?ref=badge_large)

## Cross repo
[Volentix ezeos](https://github.com/Volentix/ezeos2)
