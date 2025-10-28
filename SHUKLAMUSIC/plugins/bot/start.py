import asyncio
import random
import time
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from SHUKLAMUSIC import app
from SHUKLAMUSIC.misc import _boot_
from SHUKLAMUSIC.plugins.sudo.sudoers import sudoers_list
from SHUKLAMUSIC.utils import bot_sys_stats
from SHUKLAMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    get_served_chats,
    get_served_users,
    is_banned_user,
    is_on_off,
)
from SHUKLAMUSIC.utils.decorators.language import LanguageStart
from SHUKLAMUSIC.utils.formatters import get_readable_time
from SHUKLAMUSIC.utils.inline import help_pannel, private_panel, start_panel
from strings import get_string
from config import BANNED_USERS


BADNAAM_PIC = [
    "https://files.catbox.moe/4q7c4w.jpg",
    "https://files.catbox.moe/90z6sq.jpg",
    "https://files.catbox.moe/rdfi4z.jpg",
    "https://files.catbox.moe/6f9rgp.jpg",
    "https://files.catbox.moe/99wj12.jpg",
    "https://files.catbox.moe/ezpnd2.jpg",
    "https://files.catbox.moe/e7q55f.jpg",
    "https://files.catbox.moe/qyfsi7.jpg",
    "https://files.catbox.moe/kbke7s.jpg",
    "https://files.catbox.moe/7icvpu.jpg",
    "https://files.catbox.moe/4hd77z.jpg",
    "https://files.catbox.moe/yn7wje.jpg",
    "https://files.catbox.moe/kifsir.jpg",
    "https://files.catbox.moe/zi21kc.jpg",
    "https://files.catbox.moe/z0gh23.jpg",
    "https://files.catbox.moe/f2s4ws.jpg",
    "https://files.catbox.moe/26nzoq.jpg",
    "https://files.catbox.moe/fu6jk3.jpg",
    "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg",
]


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)

    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]

        if name.startswith("help"):
            keyboard = help_pannel(_)
            await message.reply_photo(
                random.choice(BADNAAM_PIC),
                caption=_['help_1'].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
                has_spoiler=True,
            )

        elif name.startswith("sud"):
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"❖ {message.from_user.mention} started to check <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ID:</b> <code>{message.from_user.id}</code>",
                )

        elif name.startswith("inf"):
            query = name.replace("info_", "", 1)
            results = VideosSearch(query, limit=1)
            result = (await results.next())["result"][0]
            title = result["title"]
            duration = result["duration"]
            views = result["viewCount"]["short"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            channellink = result["channel"]["link"]
            channel = result["channel"]["name"]
            link = result["link"]
            published = result["publishedTime"]

            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await message.reply_photo(
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
                has_spoiler=True,
            )
            if await is_on_off(2):
                await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"❖ {message.from_user.mention} checked <b>track info</b>.\n\n<b>ID:</b> <code>{message.from_user.id}</code>",
                )

    else:
        # ⚡ Super Smooth & Fast Animated Start
        baby = await message.reply_text("**__ᴅɪηɢ ᴅᴏηɢ.🥀__**")

        animation = [
            "ᴅɪηɢ ᴅᴏηɢ..🥀",
            "ᴅɪηɢ ᴅᴏηɢ...🥀",
            "ᴅɪηɢ ᴅᴏηɢ....🥀",
            "sᴛᴧʀᴛɪηɢ.❤️‍🔥",
            "sᴛᴧʀᴛɪηɢ..❤️‍🔥",
            "sᴛᴧʀᴛɪηɢ...❤️‍🔥",
            "ʙσᴛ sᴛᴧʀᴛєᴅ.💤",
            "ʙσᴛ sᴛᴧʀᴛєᴅ..💤",
            "ʙσᴛ sᴛᴧʀᴛєᴅ...💤"
        ]

        for text in animation:
            await asyncio.sleep(0.3)
            try:
                await baby.edit_text(f"**__{text}__**")
            except Exception:
                pass

        await asyncio.sleep(0.2)
        try:
            await baby.delete()
        except:
            pass

        # 📊 Stats + Info
        out = private_panel(_)
        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        UP, CPU, RAM, DISK = await bot_sys_stats()
        await message.reply_photo(
            random.choice(BADNAAM_PIC),
            caption=_["start_2"].format(
                message.from_user.mention,
                app.mention,
                UP,
                DISK,
                CPU,
                RAM,
                served_users,
                served_chats,
            ),
            reply_markup=InlineKeyboardMarkup(out),
            has_spoiler=True,
        )

        if await is_on_off(2):
            await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"❖ {message.from_user.mention} started the bot.\n\n<b>ID:</b> <code>{message.from_user.id}</code>",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        random.choice(BADNAAM_PIC),
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
        has_spoiler=True,
    )
    await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)

            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass

            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)

                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    random.choice(BADNAAM_PIC),
                    caption=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                    has_spoiler=True,
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
