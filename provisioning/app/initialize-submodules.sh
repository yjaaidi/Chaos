#!/bin/bash

if [ ! -e .built_protobufs ]
then
    git submodule init
    git submodule update
fi