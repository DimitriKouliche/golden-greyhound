# Golden Greyhound

This project is a virtual scavenger hunt designed for John Paul employees. I developed it as a farewell gift. It uses Django with a postgresql database and is fully dockerized.

## Installation

- Install [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/)
- Copy  .env.dist and rename it .env, fill in the values
- Run `docker-compose up`

You can run `./backup.sh` to store a json file with all current data in backups