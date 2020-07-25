# Sourcehut Uploader

Sourcehut uploader is a tool that uploads my projects to sourcehut.

This project is part of my initiative to take control over my data and code.

## Installation

First, clone this repository:

```git clone https://github.com/jamesgoca/sourcehut-uploader```

Next, set up a Python virtual environment and install the required dependencies:

```
python3 -m venv venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Finally, configure the environmental variables for this project in the .env file:

```
sourcehut_username=Your sourcehut username (i.e. "jamesgoca", without the tilde).
github_username=Your GitHub username (i.e. "jamesgoca").
sourcehut_api_key=Your sourcehut API key.
```

You can retrieve a sourcehut API key by following their guide on [authenticating with the sourcehut API](https://man.sr.ht/git.sr.ht/api.md#authentication).

To run this project, execute:

```python3 sourcehut_mirror.py```

## Screenshot

![Image of sourcehut uploader](https://github.com/jamesgoca/sourcehut-uploader/blob/master/screenshot.png?raw=true)

## License

This project is licensed using an MIT license. See more information in [LICENSE.md](https://github.com/jamesgoca/sourcehut-uploader/blob/master/LICENSE.md).

## Authors

- James Gallagher