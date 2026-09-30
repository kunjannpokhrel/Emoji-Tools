<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <h3 align="center">Emoji Tools</h3>
  <p align="center">
    A Python program for working with emojis.
    <br />
    <a href="https://github.com/kunjannpokhrel/Emoji-Tools"><strong>Explore the project »</strong></a>
    <br /><br />
    <a href="https://github.com/kunjannpokhrel/Emoji-Tools/issues">Report Bug</a>
    &middot;
    <a href="https://github.com/kunjannpokhrel/Emoji-Tools/issues">Request Feature</a>
  </p>
</div>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project
Emoji Tools is a Python program that provides three different emoji tools in one program.

### Features
* 🔤 **Emoji → Text** — Convert emojis into their text descriptions.
* 🔎 **Text → Emoji** — Search for emojis using text.
* 🧩 **Emoji Combiner** — Combine two emojis using Emoji Kitchen.
The program uses `demoji` for emoji-to-text conversion, the Emoji Family API for text-to-emoji searching, and `emojiData.json` for finding Emoji Kitchen combinations.
This project was created to practice working with APIs, JSON data, Unicode, functions, HTTP requests, and dynamically generated URLs in Python.

### Built With
<p align="left">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://requests.readthedocs.io/">
    <img src="https://img.shields.io/badge/Requests-2.x-2E7D32?style=for-the-badge&logo=python&logoColor=white" alt="Requests">
  </a>
  <a href="https://www.json.org/">
    <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white" alt="JSON">
  </a>
  <a href="https://github.com/bsolomon1124/demoji">
    <img src="https://img.shields.io/badge/Demoji-000000?style=for-the-badge" alt="Demoji">
  </a>
  <img src="https://img.shields.io/badge/Unicode-0F0F0F?style=for-the-badge" alt="Unicode">
  <img src="https://img.shields.io/badge/REST%20API-009688?style=for-the-badge" alt="REST API">
  <a href="https://github.com/">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/MIT%20License-8A2BE2?style=for-the-badge" alt="MIT License">
</p>

## Getting Started
To get a local copy up and running, follow these simple steps.

### Prerequisites
Make sure Python is installed on your computer.
You can check your Python installation with:
```sh
python --version
```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/kunjannpokhrel/Emoji-Tools.git
   ```
2. Enter the project directory
   ```sh
   cd Emoji-Tools
   ```
3. Install the required packages
   ```sh
   pip install requests demoji
   ```

## Usage
Run the program with:
```sh
python main.py
```
Choose one of the available options:
```text
[1] Emoji --> Text
[2] Text ---> Emoji
[3] Combine Two Emojis
CHOOSE ONE:
```

### 1. Emoji → Text
Enter an emoji to find its text description.
```text
Enter The Emoji: 😘
😘 ---> face blowing a kiss
```

### 2. Text → Emoji
Enter text to search for matching emojis.
```text
Enter The Text: heart
❤️ 🧡 💛 💚 💙 💜
```

### 3. Combine Two Emojis
Enter two emojis to generate their Emoji Kitchen combination.
```text
First emoji: 😘
Second emoji: 💕
```
The generated image is saved as:
```text
combined.png
```
When the process is complete, the program displays:
```text
THE FACTORY IS DONE COMBINING !!!
```

## Contributing
Contributions are what make the open source community an amazing place to learn, inspire, and create.
If you have a suggestion that would improve this project, feel free to fork the repo and create a pull request. You can also open an issue with the `enhancement` label.
1. fork the Project
2. create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. commit your Changes (`git commit -b feature/AmazingFeature`)
4. push to the Branch (`git push origin feature/AmazingFeature`)
5. open a Pull Request

### Top contributors:
<a href="https://github.com/kunjannpokhrel/Emoji-Tools/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kunjannpokhrel/Emoji-Tools" alt="top contributors" />
</a>

## License
This project is licensed under the **MIT License**.
Copyright (c) 2026 Kunjan Pokhrel
See the [LICENSE](LICENSE) file for the full license text.

## Contact
**Kunjan Pokhrel**
📧 email: [kunjannpokhrel@gmail.com](mailto:kunjannpokhrel@gmail.com)<br>
🔗 linkedin: [www.linkedin.com/in/kunjanpokhrel](https://www.linkedin.com/in/kunjanpokhrel)<br>
💻 project: https://github.com/kunjannpokhrel/Emoji-Tools

## Acknowledgments
* [Google Emoji Kitchen](https://www.google.com/search?q=Google+Emoji+Kitchen)
* [Emoji Family](https://www.emoji.family/)
* [Python](https://www.python.org/)
* [Requests](https://requests.readthedocs.io/)
* [Demoji](https://github.com/bsolomon1124/demoji)
* [GitHub](https://github.com/)

[contributors-shield]: https://img.shields.io/github/contributors/kunjannpokhrel/Emoji-Tools.svg?style=for-the-badge
[contributors-url]: https://github.com/kunjannpokhrel/Emoji-Tools/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kunjannpokhrel/Emoji-Tools.svg?style=for-the-badge
[forks-url]: https://github.com/kunjannpokhrel/Emoji-Tools/network/members
[stars-shield]: https://img.shields.io/github/stars/kunjannpokhrel/Emoji-Tools.svg?style=for-the-badge
[stars-url]: https://github.com/kunjannpokhrel/Emoji-Tools/stargazers
[issues-shield]: https://img.shields.io/github/issues/kunjannpokhrel/Emoji-Tools.svg?style=for-the-badge
[issues-url]: https://github.com/kunjannpokhrel/Emoji-Tools/issues
[license-shield]: https://img.shields.io/github/license/kunjannpokhrel/Emoji-Tools.svg?style=for-the-badge
[license-url]: https://github.com/kunjannpokhrel/Emoji-Tools/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/kunjanpokhrel
