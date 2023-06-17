Use stream.py to start recording camera feed and store in segments. The shorter the segment the shorter the delay between live feed and live feed playback, because segments are loaded from start.
Once segment generation has begun, serve the index.m3u8 and its segment via http. 
Simple way to do that would be to use "python3 -m http.server 3333" in the directy where m3u8 lives to serve entire directory.
Once http server is up, use 'http://0.0.0.0:3333/index.m3u8' as video src and open the html file in browser