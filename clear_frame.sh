#!/bin/bash

# To clear all the frames 
echo "============ Warning Clearing all the Frames =============="

cd ./assets/frames
find  . -name 'frame*' -exec rm {} \;

echo "=======Cleared================================"
