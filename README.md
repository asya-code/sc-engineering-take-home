<h1 align="center">
  <a href="https://github.com/asya-code/sc-engineering-take-home.git">
    <!-- Please provide path to your logo here -->
    <div style="font-family: 'Shadows Into Light', cursive; font-size: x-large; color: Black">Standard Crypto Engineering Take-Home Challenge</div>
  </a>
</h1>

<div align="center">
<br />

[![code with love by asya_code](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-asya_code-ff1414.svg?style=flat-square)](https://github.com/asya-code)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Launch your server](#launch-your-server)

</details>

---

## About
<p>
<a href=https://standardcrypto.notion.site/Standard-Crypto-Engineering-Take-Home-Challenge-0b1607b9f5e94252bba050a3f0587260>
<div style="font-family: 'Shadows Into Light', cursive; color: Black">Exercise requirements</div>
</a>
</p>
# Standard Crypto Engineering Take-Home Challenge

The task is to answer several questions about rates of voter turnout for the community-run governance process of the [Aave](https://aave.com/) protocol. It isn’t expected that you’ll be immediately familiar with all components involved in this question. This exercise is meant to assess both technical ability and ability to develop an introductory level of understanding of new concepts.

The questions we want to answer are as follows:

1. Which are the top 20 addresses with the highest rates of participation for Aave governance proposals on Snapshot.org, and what are each of their participation rates?
2. What rate of Snapshot participation for Aave does the University of Pennsylvania blockchain student organization have? (UPenn’s address used for voting is `0x070341aA5Ed571f0FB2c4a5641409B1A46b4961b`)

For anything with which you are not familiar, the following high-level glossary is provided:

**Snapshot.org:** A webapp for communities to submit and vote on proposals. Primarily used as a lightweight system of governance for crypto projects that choose to be community-run. Hosts a free and public API for issuing queries against its vote and proposal data.

**Address:** An identifier for each of the actors within a blockchain ecosystem. Typically a long and hexadecimal-formatted string, such as `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`.

**Aave**: A notable project within the Ethereum blockchain ecosystem, used by people seeking to lend or to borrow crypto assets. Aave is one of many projects that has elected for a decentralized system of governance, meaning its evolution is partially governed by its Snapshot space, hosted here: [https://snapshot.org/#/aave.eth](https://snapshot.org/#/aave.eth)

# Submission

Please provide either an archive folder or a link to a repository with at least the following:

- A README with the answers to the questions posed by this challenge
- Your code used in deriving answers to these questions
- Instructions in README for rerunning your scripts and arriving to your answers

# Notes and Tips

- If searching for a starting point, try clicking through a few Snapshot proposals in the browser and try to find the same data via queries to the Snapshot API.
- You may use any languages, libraries, and editors you choose.
- You should not need to use the `snapshot.js` library nor the webhooks functionality provided by Snapshot.
- Be mindful of the default pagination used by Snapshot’s API, so as to not miss any data.
- Be sure to filter on the correct Snapshot ‘space’ for Aave when fetching proposals.
- Aim for proof-of-concept quality of code. You need not optimize for production readiness. A quick pass for legibility, a few organizational comments for the reader, and a removal of scratch work and unused code is plenty.
- Although Snapshot provides a system for weighted voting, for these questions the voting power of each voter is irrelevant — we care only about each voter’s rate of turnout.
- If anything is confusing or unclear, please don’t hesitate to reach out. Parts of this problem are deliberately under-specified, but never meant to leave you stuck.

<br>

## Getting Started

### Installation

Retrieve an entire repository from a hosted location via URL
<br>
<p> &nbsp <b> git clone https://github.com/asya-code/sc-engineering-take-home.git </b> </p>

You’d then create a virtual environment:

<p> &nbsp <b> virtualenv env </b> </p>

Next, you’d activate that environment:
<br>

<p> &nbsp <b> source env/bin/activate </b> </p>

Finally, you’d use pip3 to install all of the requirements:
<br>

<p> &nbsp <b> (env) $ pip3 install -r requirements.txt </b> </p>
The -r option lets you supply a text file in the format pip3 freeze produces. This command should install all of the listed libraries.

To confirm that the correct packages are installed, you’d just run:
<br>

<p> &nbsp <b> pip3 freeze </b> </p>

### Run the app

Once you’ve set up your virtual environment, activated it, and installed Libraries, you should just be able to type:
<br>
<p> &nbsp <b> python3 app.py </b> </p>

