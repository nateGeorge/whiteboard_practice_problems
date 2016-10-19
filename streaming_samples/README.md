You have a stream of items of large and unknown length that we can only iterate over once. Assume that the stream is large enough that it doesn't fit into main memory. For example, a list of search queries in Google or interactions on Facebook.

1. Given a data stream of unknown size `n`, write a function that picks an entry uniformly at random. This is, each entry has a `1/n` chance of being chosen.

2. Extend the algorithm to pick `k` samples from this stream such that each item is equally likely to be selected.
