"""
main.py — Entry Point for AutoBots Generator

🎯 Orchestrates Ken bot onboarding, vault health checks, GitHub sync, and recovery logic.
"""

import logging
from config import config
from config.token_vault import load_token, is_token_valid, mask_token
from config.safeguard import run_preflight
from bots.ken.onboarding import register_user, check_activation_status
from bots.ken.handlers.github import validate_github_token
from bots.ken.utils.recovery import trigger_recovery

LOG_LEVEL = logging.DEBUG if config.DEBUG else logging.INFO
logging.basicConfig(level=LOG_LEVEL, format='[%(levelname)s] %(message)s')
logger = logging.getLogger("AutoBotsLauncher")

def vault_health_check():
    token = load_token()
    if not token:
        logger.error("❌ Vault token missing.")
        return False
    if not is_token_valid(token):
        logger.warning("⚠️ Vault token appears invalid.")
        return False
    logger.info(f"✅ Vault token OK: {mask_token(token)}")
    return True

def init_ken_bot(user_id: str):
    logger.info(f"🔄 Starting onboarding for {config.BOT_ALIAS} [{user_id}]")

    if not check_activation_status(user_id):
        logger.warning("⛔ Access blocked: Bot license inactive.")
        return

    register_user(user_id)

    if validate_github_token():
        logger.info("🔐 GitHub token verified. Repo ops ready.")
    else:
        logger.error("🚫 GitHub token failed validation. Sync aborted.")

def recovery_flow(user_id: str):
    logger.info(f"🧼 Triggering recovery for {user_id}")
    trigger_recovery(user_id)

if __name__ == "__main__":
    user_id = "user_ken_demo_001"
    logger.info("🚀 AutoBots Generator Launcher initiated.")
    run_preflight()
    if vault_health_check():
        init_ken_bot(user_id)
    else:
        logger.warning("🛑 Aborting bot launch due to vault issues.")