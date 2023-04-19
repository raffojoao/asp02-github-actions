# !/bin/sh

send_msg () {
    curl -s -X POST $telegram_bot_url -d chat_id=$telegram_chat_id \
        -d text="$1" -d parse_mode=$telegram_parse_mode
}

# Send message to the bot with some pertinent details about the job
# Note that for Markdown, you need to escape any backtick (inline-code)
# characters, since they're reserved in bash
send_msg "
-------------------------------------
Hello João! Github build *succeded!*
\`Repository:  $repository\`
*Commit Msg:*
$commit_message
--------------------------------------
"
