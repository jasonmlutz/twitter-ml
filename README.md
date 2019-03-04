# twitter-ml

This app will access recent Tweets and produce predictions of which users
will interact with a particular fixed Twitter account. The predictions will
be made using machine learning algorithms produced by the Python library
scikit-learn.

*Project in progress.* 

Current goals:
1. build script to repeatedly fetch tweets to build up a stock of 1000 (or so) unique tweets containing search string
1. exclude tweets with truncated = true
1. build script to fetch tweets which __do not__ contain search string
1. __Big step:__ build the machine learning algorithm(s) using scikit-learn
