#coding=utf-8

## basic settings
# you can also change Finale settings in the web portal

PROXY_PORT = 8848
PORTAL_PORT = 8844
FINALE_URL = 'http://127.0.0.1:4446/finale'
PASSWORD = 'rdfzyjy'
TIMEOUT = 30 # in seconds
OPENSSL_BIN = None # for who prefers a custom openssl executable

## optimizations
# designed for advanced users. change it at your own risk.

CHUNKSIZE = 64*1024
# the response streams are sent back in chunks.
# a small chunksize will limit download speed; a large chunksize will increase TTFB.

POOLSIZE = 128
# tiro uses requests's connection pool mechanism.
# improve concurrency but will consume more RAM.

SSL_WILDCARD = True
# tiro ssl module will sign wildcard ssl certificate for sub-domains.
# turn on for better efficiency. turn off if you encounter ssl certificate errors.

COMPRESS_THRESHOLD = 32*1024
# tiro uses gzip to compress large Finale request data.
# increase the threshold for better upload speed. decrease the threshold for shorter TTFB.

PROXY_MODE = 2
# 0: Completely Direct / 1: Decided by GFWList (experimental) / 2: Completely Finale
# for mode 1, tiro will use GFWList to determine whether to use Finale proxy or make the request directly.

REUSE_SESSION = True
# tiro will reuse the requests sessions of direct requests.
# recommended. DRAMATICALLY improve efficiency, but have potential security vulnerability.

## internal arguments
# undocumented. DO NOT CHANGE unless you know exactly what your are doing.

TEST_URL = 'http://example.com/not_exist/tiro_finale_test.page'
PORTAL_CALLBACK = '___callback_tf_proxy_running'