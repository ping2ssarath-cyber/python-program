"""
Seeker - Python README Format
Converted from Markdown README to Python documentation style.

Concept:
Seeker is a proof-of-concept educational project demonstrating how websites
can request browser geolocation permissions and collect device/browser metadata
when users allow access.

The project highlights privacy and security awareness by showing what
information a website may gather from a visitor.

============================================================
FEATURES
============================================================

Location Information (when permission is granted):
- Longitude
- Latitude
- Accuracy
- Altitude (not always available)
- Direction (only available if the device is moving)
- Speed (only available if the device is moving)

Device Information:
- Canvas fingerprint ID
- Device model
- Operating system
- Platform
- CPU cores
- RAM information
- Screen resolution
- GPU information
- Browser name and version
- Public IP address
- Local IP address
- Local port

============================================================
IMPORTANT NOTICE
============================================================

This project is intended for:
- Educational purposes
- Security awareness
- Privacy demonstrations
- Learning how browser permissions work

Do not use this project against individuals without explicit consent.
Unauthorized collection of personal or location data may violate laws,
privacy regulations, and ethical guidelines.

============================================================
HOW IT DIFFERS FROM IP GEOLOCATION
============================================================

Traditional IP geolocation:
- Uses ISP information
- Provides approximate area only
- Often inaccurate

Browser geolocation API:
- Uses GPS hardware when available
- More accurate on smartphones
- Can achieve accuracy within ~30 meters
- Falls back to IP-based estimation if GPS is unavailable

Accuracy depends on:
- Device hardware
- Browser support
- GPS calibration
- Permission settings

============================================================
AVAILABLE TEMPLATES
============================================================

Templates included:
- NearYou
- Google Drive
- WhatsApp
- Telegram
- Zoom
- Google reCAPTCHA

Users can create custom templates following the project's template guide.

============================================================
SUPPORTED PLATFORMS
============================================================

Tested on:
- Kali Linux
- BlackArch Linux
- Ubuntu
- Fedora
- Kali NetHunter
- Termux
- Parrot OS
- macOS Monterey

============================================================
INSTALLATION
============================================================

Linux / Ubuntu / Fedora / Termux:

    git clone https://github.com/thewhiteh4t/seeker.git
    cd seeker/
    chmod +x install.sh
    ./install.sh

BlackArch Linux:

    sudo pacman -S seeker

Docker:

    docker pull thewhiteh4t/seeker

macOS:

    git clone https://github.com/thewhiteh4t/seeker.git
    cd seeker/
    python3 seeker.py

============================================================
NGROK SETUP
============================================================

Install ngrok:

    brew install ngrok/ngrok/ngrok

Run tunnel:

    ngrok http 8080

============================================================
USAGE
============================================================

Help Menu:

    python3 seeker.py -h

Common Options:

    -h, --help
        Show help menu

    -k, --kml
        Export KML file

    -p, --port
        Specify web server port

    -u, --update
        Check for updates

    -v, --version
        Show version

    -t, --template
        Choose template

    -d, --debugHTTP
        Disable HTTPS redirection for testing

============================================================
ENVIRONMENT VARIABLES
============================================================

Supported variables:
- DEBUG_HTTP
- PORT
- TEMPLATE
- TITLE
- REDIRECT
- IMAGE
- DESC
- SITENAME
- DISPLAY_URL
- MEM_NUM
- ONLINE_NUM
- TELEGRAM
- WEBHOOK

============================================================
USAGE EXAMPLES
============================================================

Start application:

    python3 seeker.py

Start ngrok tunnel:

    ngrok http 8080

Use custom port:

    python3 seeker.py -p 1337

Use template:

    python3 seeker.py -t 1

============================================================
DOCKER USAGE
============================================================

Create network:

    docker network create ngroknet

Run container:

    docker run --rm -it --net ngroknet --name seeker thewhiteh4t/seeker

Run ngrok container:

    docker run --rm -it --net ngroknet --name ngrok \
        wernight/ngrok ngrok http seeker:8080

============================================================
LOCAL TUNNELS
============================================================

Alternative tunnel command:

    ssh -R 80:localhost:8080 nokey@localhost.run

============================================================
DEMO
============================================================

Video Demo:
https://odysee.com/@thewhiteh4t:2/seeker_v126_demo:e

============================================================
OFFICIAL LINKS
============================================================

GitHub Repository:
https://github.com/thewhiteh4t/seeker

Blog:
https://thewhiteh4t.github.io

Twitter:
https://twitter.com/thewhiteh4t

Website:
https://twc1rcle.com/

============================================================
END OF DOCUMENT
============================================================
"""


def main():
    print("Seeker README loaded successfully.")
    print("This file contains the converted Python-style README documentation.")


if __name__ == "__main__":
    main()
