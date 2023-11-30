#!/bin/bash
# should takes in a URL, sends a POST request to the passed URL
# variable email must be sent with the value test@gmail.com
# variable subject must be sent with the value I will always be here for PLD
# should use curl

curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
