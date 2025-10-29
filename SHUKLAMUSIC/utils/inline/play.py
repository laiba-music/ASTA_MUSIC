import math
from pyrogram.types import InlineKeyboardButton
from SHUKLAMUSIC import app
import config
from SHUKLAMUSIC.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
                url="https://t.me/Queen_XMusic_Bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="• ᴏᴡɴᴇʀ •", url="https://t.me/icxasta"),
            InlineKeyboardButton(text="• sυᴘᴘσʀᴛ •", url="https://t.me/ixasta1"),
        ],
        [InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="close")],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    buttons = [
        [
            InlineKeyboardButton(
                text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
                url="https://t.me/Queen_XMusic_Bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="• ᴏᴡɴᴇʀ •", url="https://t.me/icxasta"),
            InlineKeyboardButton(text="• sυᴘᴘσʀᴛ •", url="https://t.me/ixasta1"),
        ],
        [InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
                url="https://t.me/Queen_XMusic_Bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="• ᴏᴡɴᴇʀ •", url="https://t.me/icxasta"),
            InlineKeyboardButton(text="• sυᴘᴘσʀᴛ •", url="https://t.me/ixasta1"),
        ],
        [InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"SHUKLAPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"SHUKLAPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
                url="https://t.me/Queen_XMusic_Bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="• ᴏᴡɴᴇʀ •", url="https://t.me/icxasta"),
            InlineKeyboardButton(text="• sυᴘᴘσʀᴛ •", url="https://t.me/ixasta1"),
        ],
        [InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="close")],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
                url="https://t.me/Queen_XMusic_Bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="• ᴏᴡɴᴇʀ •", url="https://t.me/icxasta"),
            InlineKeyboardButton(text="• sυᴘᴘσʀᴛ •", url="https://t.me/ixasta1"),
        ],
        [InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="close")],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="close"),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
                url="https://t.me/ilmamusicbot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="• ᴏᴡɴᴇʀ •", url="https://t.me/icxasta"),
            InlineKeyboardButton(text="• sυᴘᴘσʀᴛ •", url="https://t.me/ixasta1"),
        ],
    ]
    return buttons
