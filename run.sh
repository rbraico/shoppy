#!/bin/bash
gunicorn -w 2 -b 0.0.0.0:9193 wsgi:app