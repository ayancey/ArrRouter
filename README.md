# ArrRouter

Open sourcing this dumb, half-baked idea because why not. The Plex Watch Together feature is pretty nice, but watching a syncronized video on a site like [WatchParty](https://www.watchparty.me/) is easier and faster.

This script queries your movies and TV shows from Radarr and Sonarr respectively. It presents a web interface for making a selection, and upon selection re-encodes the video into H264 video and AAC audio in an .mp4 container (easily the best supported format for browsers), then uploads it to S3 so you can put the link into WatchParty.
