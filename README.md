# System Resource Monitor and Telegram Notifier  

This repository contains a Python script for monitoring system resources (CPU, memory, and disk usage) on a Linux server and sending notifications via Telegram when certain thresholds are reached.

## Overview  

The script periodically checks the system's resource usage and sends a message via Telegram if any of the following thresholds are exceeded:  
- CPU usage exceeds 84%  
- Memory usage exceeds 69%  
- Disk usage exceeds 77%  

## Requirements  

- Python 3.x  
- `psutil` library for system monitoring  
- `requests` library for making HTTP requests to the Telegram Bot API  

Install the required dependencies using pip:
`pip install psutil requests`  

## Configuration  

Before running the script, you need to set up a Telegram bot and obtain the bot token and chat ID. Replace the placeholder values (`XXX`) in the script with your actual bot token and chat ID.

## Usage  

1. **Run the Script**: Execute the script on your Linux server.  
   ```bash
   python3 resource_monitor.py

Monitoring: The script continuously monitors system resources and prints the resource usage to the console.   
Telegram Notifications: If any of the resource thresholds are exceeded, the script sends a notification message to the specified Telegram chat.    

## Example Output
 `CPU Usage: 50%, Memory Usage: 60%, Disk Usage: 30%`  
`CPU Usage: 75%, Memory Usage: 70%, Disk Usage: 60%`    
`Message sent successfully!`  

This readme.md is provided by ai.  
