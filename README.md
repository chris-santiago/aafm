# Table Of Contents

* [Getting Started - Overview](#Getting%20Started%20-%20Overview)
    * [Getting Started - Without Docker](#Getting%20Started%20-%20Without%20Docker)
    * [Getting Started -  With Docker](#Getting%20Started%20-%20With%20Docker)
* [Getting Started - ETL](#Getting%20Started%20-%20ETL)


# Getting Started - Overview

This project can be developed locally in two ways (primarily).
1) By installation of all code/tools/data/etc. locally on your machine (this is currently the most common workflow).
2) By installing Docker, then installing all code/tool/etc. into a Docker container, treating the new Docker container as your isolated development environment.

Why do we need two ways of doing things? The short answer is that we don't _need_ two ways of doing things, but there are pros and cons to each approach. [This document](https://www.ibm.com/cloud/learn/containerization) by IBM covers containerization and why someone would consider leveraging it (it's a bit long, but the following table hits on someone of the differences). The introductory sections of this video are quite helpful as well https://www.youtube.com/watch?v=KFyRLxiRKAc

|Aspect|Without Containers|With Containers|
|---|---|---|
|Largely Avoids "Works On My Machine"|No|**Yes**|
|Complexity|**Low**|Medium|
|Getting Started|**Fast**|**Medium-Slow then becomes Fast**|
|Portability|More Work|**Low Work**|
|Consistency|High Work|**Low Work**|
|Agility|Low|**High**|
|Isolation|Low|**High**|

For me (Collin), I chose dockerized development because I can run different versions of software in isolation.

Once you've chosen which style of development you would like to persue, go to [Getting Started - Without Docker](#Getting%20Started%20-%20Without%20Docker) xor [Getting Started -  With Docker](#Getting%20Started%20-%20With%20Docker) which ever matches your needs.


# Getting Started - Without Docker

Clone this repo and then install the project package:

```bash
cd aafm
pip install -e .
```


# Getting Started - With Docker

_This section assumes you're using VS Code for development_

1) Go through this document or vidoe to familiarize yourself with containerized development https://code.visualstudio.com/docs/remote/containers or https://www.youtube.com/watch?v=KFyRLxiRKAc 
2) Add the `Remote - Containers` extension to VS Code (https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 
2) Clone this repository
3) Open the root folder (aafm) in a container. See: https://code.visualstudio.com/docs/remote/containers#_quick-start-open-an-existing-folder-in-a-container or the video in step 1.
    * The container has been configured to include Python 3.8, and Jupyter, meaning both of those will work out of the box without further configuration.


# Getting Started - ETL

ETL (Extract Transform Load) basically just means data prep. Load some data from somewhere, transform it into a useful shape, then store it somewhere else.

1) From Microsoft Teams, navigate to Files, then the Data Folder, then download `data.7z`
    * You will need a utility (or library) such as 7-zip to decompress the file.
    * Why 7z? Because it has much better compression (LZMA2) than zip (DEFLATE).
2) Extract the contents of `data.7z` into this project at `./data/raw/daily/`.
3) Open `./notebooks/extract.ipynb` using Jupyter Notebooks or VS Code Notebooks.
    * If you're using our Docker Container for development, the right tools have already been added.
      Simply open `extract.ipynb` in VS Code and wait for the proper UI to load.
4) Run each notebook cell on it's own to see how they work, or run them all.
