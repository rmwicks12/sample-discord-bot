# 🤖 Discord Moderation Bot (Legacy 2021)

![Status](https://img.shields.io/badge/Status-Archived-red) ![Python](https://img.shields.io/badge/Python-3.6.12-blue) ![Library](https://img.shields.io/badge/discord.py-v1.7.3-orange)

> ⚠️ **ARCHIVAL NOTICE:** This repository contains code written in **2021**. It relies on an outdated version of the Discord API and legacy Python versions. **This code will not run today** due to significant changes in Discord's infrastructure and library updates.

## 📜 About
This project was a custom Discord bot created to manage server moderation and utility. It was originally designed to run on **Heroku** using a `Procfile`.

The bot features a custom activity status watching **"ESPORTS"** and utilizes prefix-based commands (`^`).

## 💾 Environment & Dependencies
This project is frozen on the following specific versions found in `runtime.txt` and `requirements.txt`:

* **Python:** `3.6.12` (EOL: Dec 2021)
* **Library:** `discord.py==1.7.3` (Pre-2.0 rewrite)

## 🛠️ Features (Historical)
* **Auto-Moderation:** Automatically assigned a specific role to new members upon joining.
* **Admin Tools:** `^kick`, `^ban`, and `^unban` commands.
* **Blacklist System:** Custom role-based blacklisting (`^blacklist` / `^removeblacklist`).
* **Server Utility:**
    * `^ping`: Checked API latency.
    * `^serverinfo`: Displayed detailed server stats (Member count, creation date, channel breakdown).

## 💀 Why this code is Obsolete
If you are looking to learn from this code, please note the following breaking changes that have occurred since 2021:

1.  **Discriminators are dead:** The unban command relies on `member.split('#')`. Discord has replaced `#1234` discriminators with unique usernames, rendering this logic invalid.
2.  **Library Updates:** Properties like `ctx.guild.icon_url` have been renamed (e.g., to `ctx.guild.icon.url`) in modern `discord.py` versions (2.0+).
3.  **Hosting:** This project includes a `Procfile` for Heroku. Heroku ended their free tier in late 2022.
4.  **Youtube_dl:** The import `youtube_dl` is present in the code. This library is abandoned and has been replaced by `yt-dlp`.

## 📂 File Structure
* `bot.py`: The main application logic.
* `Procfile`: Legacy Heroku deployment configuration.
* `runtime.txt`: Specifies Python 3.6.12.
* `requirements.txt`: Specifies library versions.

---
*This repository exists for portfolio and archival purposes only.*
