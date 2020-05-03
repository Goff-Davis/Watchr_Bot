# Watchr_Bot

A reddit search bot I created to search r/watchexchange for watches that I want. Currently it searches for broken watches or parts and the Raketa Kopernic.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See usage/deployment for notes on how to deploy the project on a live system.

### Prerequisites

#### Software

* [Python 3.5+](https://www.python.org/)
* [praw](https://praw.readthedocs.io/en/latest/)

```
pip install praw
```

Depending on your system you may need to do

```
pip3 install praw
```

#### Configuration

You will need a `praw.ini` file with the following information:

```
[watcher]
client_id=<Your reddit client id>
client_secret=<Your reddit secret>
username=<Yours or your bot's reddit username>
password=<Yours or your bot's reddit password>
```

To obtain a client id and secret you will need to [register your app with reddit.](https://www.reddit.com/prefs/apps) Notify them [here.](https://docs.google.com/forms/d/e/1FAIpQLSezNdDNK1-P8mspSbmtC2r86Ee9ZRbC66u929cG2GX0T9UMyw/viewform)


You will also need a `config.json` file with the following structure:

```
{
	"search_strings": ["<array of strings you want to search for>"],
	"user": "<the username of the person you want to message>",
	"subreddit": "<the subreddit you want to search>",
	"time_filter": "<what time frame you want to search for>"
}
```

## Usage/Deployment

This script can be run manually. Alternatively you can execute it programmatically, for example as a cronjob. I personally am running it on a [Digital Ocean](https://www.digitalocean.com/) droplet as a cronjob once per hour.

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Authors

* **Davis Goff** - [Goff_Davis](https://github.com/Goff-Davis)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
