from typing import List, Optional, Union

from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    InlineQueryHandler,
    MessageHandler,
)
from telegram.ext.filters import MessageFilter

from HOKAGE import LOGGER
from HOKAGE import dispatcher as d
from HOKAGE.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler


class HOKAGEHandler:
    def __init__(self, d):
        self._dispatcher = d

    def command(
        self,
        command: str,
        filters: Optional[MessageFilter] = None,
        admin_ok: bool = False,
        pass_args: bool = False,
        pass_chat_data: bool = False,
        run_async: bool = True,
        can_disable: bool = True,
        group: Optional[Union[int, str]] = 40,
    ):
        def _command(func):
            try:
                if can_disable:
                    self._dispatcher.add_handler(
                        DisableAbleCommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            admin_ok=admin_ok,
                        ),
                        group,
                    )
                else:
                    self._dispatcher.add_handler(
                        CommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                        ),
                        group,
                    )
                LOGGER.debug(
                    f"[ʜᴏᴋᴀɢᴇ ᴄᴍᴅ] ʟᴏᴀᴅᴇᴅ ʜᴀɴᴅʟᴇʀ {command} ғᴏʀ ғᴜɴᴄᴛɪᴏɴ {func.__name__} ɪɴ ɢʀᴏᴜᴘ {group}"
                )
            except TypeError:
                if can_disable:
                    self._dispatcher.add_handler(
                        DisableAbleCommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            admin_ok=admin_ok,
                            pass_chat_data=pass_chat_data,
                        )
                    )
                else:
                    self._dispatcher.add_handler(
                        CommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            pass_chat_data=pass_chat_data,
                        )
                    )
                LOGGER.debug(
                    f"[ʜᴏᴋᴀɢᴇ ᴄᴍᴅ] Loaded handler {command} for function {func.__name__}"
                )

            return func

        return _command

    def message(
        self,
        pattern: Optional[str] = None,
        can_disable: bool = True,
        run_async: bool = True,
        group: Optional[Union[int, str]] = 60,
        friendly=None,
    ):
        def _message(func):
            try:
                if can_disable:
                    self._dispatcher.add_handler(
                        DisableAbleMessageHandler(
                            pattern, func, friendly=friendly, run_async=run_async
                        ),
                        group,
                    )
                else:
                    self._dispatcher.add_handler(
                        MessageHandler(pattern, func, run_async=run_async), group
                    )
                LOGGER.debug(
                    f"[ʜᴏᴋᴀɢᴇ ᴍsɢ] Loaded filter pattern {pattern} for function {func.__name__} in group {group}"
                )
            except TypeError:
                if can_disable:
                    self._dispatcher.add_handler(
                        DisableAbleMessageHandler(
                            pattern, func, friendly=friendly, run_async=run_async
                        )
                    )
                else:
                    self._dispatcher.add_handler(
                        MessageHandler(pattern, func, run_async=run_async)
                    )
                LOGGER.debug(
                    f"[ʜᴏᴋᴀɢᴇ ᴍsɢ] ʟᴏᴀᴅᴇᴅ ғɪʟᴛᴇʀ ᴘᴀᴛᴛᴇʀɴ {pattern} ғᴏʀ ғᴜɴᴄᴛɪᴏɴ {func.__name__}"
                )

            return func

        return _message

    def callbackquery(self, pattern: str = None, run_async: bool = True):
        def _callbackquery(func):
            self._dispatcher.add_handler(
                CallbackQueryHandler(
                    pattern=pattern, callback=func, run_async=run_async
                )
            )
            LOGGER.debug(
                f"[ʜᴏᴋᴀɢᴇ ᴄᴀʟʟʙᴀᴄᴋ] ʟᴏᴀᴅᴇᴅ ᴄᴀʟʟʙᴀᴄᴋǫᴜᴇʀʏ ʜᴀɴᴅʟᴇʀ ᴡɪᴛʜ ᴘᴀᴛᴛᴇʀɴ {pattern} ғᴏʀ ғᴜɴᴄᴛɪᴏɴ {func.__name__}"
            )
            return func

        return _callbackquery

    def inlinequery(
        self,
        pattern: Optional[str] = None,
        run_async: bool = True,
        pass_user_data: bool = True,
        pass_chat_data: bool = True,
        chat_types: List[str] = None,
    ):
        def _inlinequery(func):
            self._dispatcher.add_handler(
                InlineQueryHandler(
                    pattern=pattern,
                    callback=func,
                    run_async=run_async,
                    pass_user_data=pass_user_data,
                    pass_chat_data=pass_chat_data,
                    chat_types=chat_types,
                )
            )
            LOGGER.debug(
                f"[ʜᴏᴋᴀɢᴇ ɪɴʟɪɴᴇ] ʟᴏᴀᴅᴇᴅ ɪɴʟɪɴᴇǫᴜᴇʀʏ ʜᴀɴᴅʟᴇʀ ᴡɪᴛʜ ᴘᴀᴛᴛᴇʀɴ {pattern} ғᴏʀ ғᴜɴᴄᴛɪᴏɴ {func.__name__} | ᴘᴀssᴇs ᴜsᴇʀ ᴅᴀᴛᴀ: {pass_user_data} | ᴘᴀssᴇs ᴄʜᴀᴛ ᴅᴀᴛᴀ: {pass_chat_data} | ᴄʜᴀᴛ ᴛʏᴘᴇs: {chat_types}"
            )
            return func

        return _inlinequery


HOKAGEcmd = HOKAGEHandler(d).command
HOKAGEmsg = HOKAGEHandler(d).message
HOKAGEcallback = HOKAGEHandler(d).callbackquery
HOKAGEinline = HOKAGEHandler(d).inlinequery
