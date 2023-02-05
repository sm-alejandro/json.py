<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/zilmosat/json_helper.py"> -->
    <!-- <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  <!-- </a> -->

<h3 align="center">json_helper.py</h3>

  <p align="center">
    Bulk edit tools for json files in python
    <br />
    <a href="https://github.com/zilmosat/json_helper.py"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/zilmosat/json_helper.py/issues">Report Bug</a>
    ·
    <a href="https://github.com/zilmosat/json_helper.py/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Prerequisites

All code runs on python using following native libraries

- pathlib
- json
- argparse (only for cli usage)
- unittest for testing purposes

### Installation

- Clone the repo
  - Call the individual files via the command line (add_field.py, delete_field.py and replace_field.py)
  - Use the functions directly in your code importing bulkjson.py

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

# Usage

## PACKAGE USAGE

import bulkjson

> bulkjson.add(data: dict, loc: str, key: str, val, rec: bool)

> bulkjson.delete(data: dict, loc: str, key: str, rec: bool):

> bulkjson.replace(data: dict, loc: str, key: dict, rec: bool):

<br />
<br />

## CONSOLE USAGE (operations on example.json)

### ADD

Simple additions (adding to every key in the root of the document):

> py ./add_field.py -data ./data/example.json -key "timestamp"

Recursive additions (adding to every possible dictionary)

> py ./add_field.py -data ./data/example.json -key "custom" -rec

Add to specific key

> py ./add_field.py -data ./data/example.json -key "direction" -loc "wind"

<br />

### DELETE

Simple deletions (deleting from every key in the root of the document):

> py ./delete_field.py -data ./data/example.json -key "wind"

Recursive deletions (deleting from every possible dictionary)

> py ./delete_field.py -data ./data/example.json -key "speed" -rec

Remove from certain key

> py ./delete_field.py -data ./data/example.json -key "speed" -loc "wind"

<br />

### REPLACE

Simple replacements (replacing from every key in the root of the document):

> py ./replace_field.py -data ./data/example.json -key "{'measurement_2': 'measurement_4'}"

Recursive replacements (replacing from every possible dictionary)

> py ./replace_field.py -data ./data/example.json -key {'wind': 'temperature'} -rec

Remove from certain key

> py ./replace_field.py -data ./data/example.json -key {'speed': 'quantity'} -loc "rain"

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Your Name - [@zilmosat](https://twitter.com/zilmosat) - zilmosat@gmail.com

Project Link: [https://github.com/zilmosat/json_helper.py](https://github.com/zilmosat/json_helper.py)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/zilmosat/json_helper.py.svg?style=for-the-badge
[contributors-url]: https://github.com/zilmosat/json_helper.py/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/zilmosat/json_helper.py.svg?style=for-the-badge
[forks-url]: https://github.com/zilmosat/json_helper.py/network/members
[stars-shield]: https://img.shields.io/github/stars/zilmosat/json_helper.py.svg?style=for-the-badge
[stars-url]: https://github.com/zilmosat/json_helper.py/stargazers
[issues-shield]: https://img.shields.io/github/issues/zilmosat/json_helper.py.svg?style=for-the-badge
[issues-url]: https://github.com/zilmosat/json_helper.py/issues
[license-shield]: https://img.shields.io/github/license/zilmosat/json_helper.py.svg?style=for-the-badge
[license-url]: https://github.com/zilmosat/json_helper.py/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
