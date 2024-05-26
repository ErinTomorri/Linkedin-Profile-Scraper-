# LinkedIn Profile Scraper

## Overview

This project is a LinkedIn Profile Scraper designed to extract publicly available information from LinkedIn profiles using only HTTP requests and proxy servers. Given LinkedIn's stringent anti-scraping measures, this project demonstrates the effectiveness of bypassing such defenses.

## Features

- **Profile Data Extraction**: Retrieve publicly available data such as names, job titles, and company details from LinkedIn profiles.
- **Anti-Scraping Bypass**: Implement strategies to circumvent LinkedIn's sophisticated anti-scraping algorithms.
- **Anonymity**: Use rotating proxies to maintain anonymity and avoid IP blocking.
- **Rate Limiting**: Mimic human browsing behavior to reduce the risk of detection.

## Installation

To use this scraper, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/linkedin-profile-scraper.git
cd linkedin-profile-scraper
pip install -r requirements.txt
```

## Usage

1. **Set Up Proxies**: Prepare a list of proxy servers. You can use free proxies or a paid proxy service for better reliability.
2. **Configure Settings**: Edit the `config.py` file to include your proxy list and any other configuration settings.

## Configuration

The `config.py` file includes the following settings:

- **PROXY_LIST**: A list of proxy servers to be used for making requests.
- **REQUEST_HEADERS**: HTTP headers to mimic a real browser.
- **RATE_LIMIT**: Controls the delay between requests to mimic human behavior.

## Challenges

- **Anti-Scraping Measures**: LinkedIn employs robust anti-scraping measures including rate limiting, IP blocking, and CAPTCHAs.
- **Proxy Management**: Ensuring a continuous pool of working proxy servers to avoid detection and maintain scraping efficiency.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
