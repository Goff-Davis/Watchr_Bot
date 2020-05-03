# Watchr_Bot

![License](https://img.shields.io/github/license/Goff-Davis/Watchr_Bot?style=flat-square)

A reddit search bot I created to search r/watchexchange for watches that I want. Currently it searches for broken watches or parts and the Raketa Kopernic. It messages my personal reddit user when it finds something.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See usage/deployment for notes on how to deploy the project on a live system.

### Prerequisites

#### Software

* [Python 3.6+](https://www.python.org/)
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
	"search_category": "<Name of what you are searching for (for message formatting)>"
	"user": "<the username of the person you want to message>",
	"subreddit": "<the subreddit you want to search>",
	"time_filter": "<what time frame you want to search for>"
}
```

## Usage/Deployment

This script can be run manually. Alternatively you can execute it programmatically, for example as a cronjob. I personally am running it on a [Digital Ocean](https://www.digitalocean.com/) droplet as a cronjob once per hour.

## Example of found results message

```
# New Listings Found

Watches in the categories: **parts**, **repair**, **for repair** have been found.

Links to the postings:

## parts
- [[WTS] Orient Ray Gen 1, Timex E-Compass (T49531), Seiko Compatible Modded Bezel Part](/r/Watchexchange/comments/gch45v/wts_orient_ray_gen_1_timex_ecompass_t49531_seiko/) (05-02-2020 20:24)


## repair
- [[WTS] Vostok, Dumai and Gameboy Watch + Clocks for Repair](/r/Watchexchange/comments/gcr69z/wts_vostok_dumai_and_gameboy_watch_clocks_for/) (05-03-2020 10:07)


## for repair
- [[WTS] Vostok, Dumai and Gameboy Watch + Clocks for Repair](/r/Watchexchange/comments/gcr69z/wts_vostok_dumai_and_gameboy_watch_clocks_for/) (05-03-2020 10:07)
```

## Built With

* [Python](https://www.python.org/)
* [praw](https://praw.readthedocs.io/en/latest/) - Python wrapper for the Reddit API
* [Reddit API](https://www.reddit.com/dev/api/)

## Authors

* **Davis Goff** - [Goff-Davis](https://github.com/Goff-Davis)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
