# TBVDownloader
Terminal Based Video Downloader

Usage:

`python3 tbvd.py -u <URL> -t <video or audio> -r <resolution for videos (144p,240p, etc.)> -na`
(-na for downloads video without audio)

Required python modules:

	pytube

	argparse


******
### NOTE
If you are constantly getting the "check your URL" message and if you see this error when you remove the Try Except block: "pytube.exceptions.RegexMatchError: get_ytplayer_config: could not find match for config_patterns"

This error is due to Pytube known issue: https://github.com/nficano/pytube/issues/614#issuecomment-724326141

And it is fixed with update, you can update or reinstall your pytube library: python3 -m pip install git+https://github.com/nficano/pytube.git
******
