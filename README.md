# ezeos

![banner](logo.png)
<img src="logo.png" alt="banner" height="5">

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![Semver](http://img.shields.io/SemVer/2.0.0.png)](http://semver.org/spec/v2.0.0.html)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![GitHub version](https://badge.fury.io/gh/boennemann%2Fbadges.svg)](http://badge.fury.io/gh/boennemann%2Fbadges)

> A simple and easy to use testing/learning tool for EOS.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Setting Expectations](#setting-expectations)
- [Maintainers](#maintainers)
- [Contribute](#contribute)
- [License](#license)

## Background

**WARNING!!!**
```
 This tool was written over just an hour or two. It is not intended for any other purpose than for people to play around with EOS. 
Additionally, we are all pretty heads down working towards our products release schedules as well as those of our partners. As a result, unless we have the time, we will not be updating/maintaining/elaborating the tooling with any frequency or cadance. That being said, we will peek in on it from time to time to see whats happening with it.

If you are someone who is vested in making this tool better please fork it and let us know.
```

The tool was created as a means to quickly and easily experiment with a local instance of the EOS blockchain. Basically, the command line was killing our time. With this in mind, we took an hour or two to create the tool that would allow us to iterate on testing our particular usecase quickly and painlessly. 

To be clear, we feel that this is a basic testing tool others can use to explore and learn the EOS commandline quickly.

The main functions you will find are:
1. Start/stop/flush EOS
2. Create wallets
3. Add tokens (VTX in our case) to a wallet
4. Transfer the tokens to another wallet


The things we wish we had the time to do are:
1. Use the API rather than the CLI.
2. Build it as a web based UI rather that the QT based one.
3. Dynamic UI based on different contract scenarios. The current one is bound to the token creation contract.

The things we don't think we would ever use it for:
1. Production

- Install Ubuntu 
- Install EOSIO (dawn_v4.0.0)
- Install python
- install PyQt4
- Configure nodeos config file

EOSIO installation must be ~/eos

## Install

In order to use this tool, you will need the following tools installed.

1. Recommended Ubuntu
2. Install EOSIO (dawn_v4.0.0) in the `~/eos` directory
3. Python
4. PyQt4
5. Intelligent configuration of `nodeos`

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

## Setting Expectations

In order to set the right expectations for the community, we, regrettably, will not be reacting quickly to requested changes. This is a one and done type tool that we felt certain could benefit others. If you are interested in its improvement we recommend forking it and making a go of it on your own. Having said that, we would love to hear from you aboout your efforts! If we can help we will!

## Maintainers

[@sylvaincormier](https://github.com/sylvaincormier)

## Contribute

If you are intereted in contributing, please read [the code of conduct file.](code-of-conduct.md)!

PRs accepted.

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2018 VolentixLabs
