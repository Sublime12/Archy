module "dev" {
  source      = "../../modules"
  src_dir     = "../../../src"
  environment = "dev"

  secrets = [
    "DISCORD_TOKEN",
    "TENOR_API_TOKEN",
  ]

  http_functions = {
    describe : {
      description = "Describe a user"
      runtime     = "python39"
      entry_point = "describe"
      timeout     = 15
      memory      = 256
      secrets     = []
    }
    hello : {
      description = "Template of a function in Python"
      runtime     = "python39"
      entry_point = "hello"
      timeout     = 15
      memory      = 256
      secrets     = []
    }
    java : {
      description = "Template of a function in Java"
      runtime     = "java17"
      entry_point = "functions.Java"
      timeout     = 15
      memory      = 256
      secrets     = []
    }
    js : {
      description = "Template of a function in Javascript"
      runtime     = "nodejs16"
      entry_point = "js"
      timeout     = 15
      memory      = 256
      secrets     = ["DISCORD_TOKEN"]
    }
    level : {
      description = "Return the level of a user using the NextJS function"
      runtime     = "go119"
      entry_point = "Level"
      timeout     = 15
      memory      = 256
      secrets     = []
    }
    froge : {
      description = "Return a random froge from the server"
      runtime     = "go119"
      entry_point = "SendRandomFroge"
      timeout     = 15
      memory      = 256
      secrets     = ["DISCORD_TOKEN"]
    }
    gif : {
      description = "Return the requested gif"
      runtime     = "python39"
      entry_point = "gif"
      timeout     = 15
      memory      = 256
      secrets     = ["DISCORD_TOKEN", "TENOR_API_TOKEN"]
    }
    go : {
      description = "Template of a function in Golang"
      runtime     = "go119"
      entry_point = "SendMessageWithReaction"
      timeout     = 15
      memory      = 256
      secrets     = ["DISCORD_TOKEN"]
    },
    ban : {
      description = "Admin only: Ban a user"
      runtime     = "go119"
      entry_point = "BanUser"
      timeout     = 15
      memory      = 256
      secrets     = ["DISCORD_TOKEN"]
    }
    help : {
      description = "Describe all active commands"
      runtime     = "python39"
      entry_point = "help"
      timeout     = 15
      memory      = 256
      secrets     = []
    },
    leaderboard : {
      description = "Return the leaderboard of the server"
      runtime     = "go119"
      entry_point = "GetLeaderboardUrl"
      timeout     = 15
      memory      = 256
      secrets     = []
    },
    warn : {
      description = "Admin only: Warn a user and take action if needed"
      runtime     = "go119"
      entry_point = "WarnUser"
      timeout     = 15
      memory      = 256
      secrets     = ["DISCORD_TOKEN"]
    },
    listwarn : {
      description = "Admin only: List all warn of that server"
      runtime     = "go119"
      entry_point = "ListWarn"
      timeout     = 15
      memory      = 256
      secrets     = ["DISCORD_TOKEN"]
    },
    answer : {
      description = "Return a random answer based on the game '8 Ball'"
      runtime     = "python39"
      entry_point = "answer"
      timeout     = 15
      memory      = 256
      secrets     = []
    },
    merch : {
      description = "Return the merch website"
      runtime     = "go119"
      entry_point = "Merch"
      timeout     = 15
      memory      = 256
      secrets     = ["DISCORD_TOKEN"]
    },
  }

  pubsub_topics = [
    "channel_message_discord",
    "cloud_function_error_log",
    "froge_of_the_day",
    "private_message_discord",
    "update_user_role",
    "exp_discord",
    "generate_level_image",
    "generate_welcome_image"
  ]

  pubsub_functions = {
    exp : {
      description   = "Increase the experience of a user"
      runtime       = "go119"
      entry_point   = "Exp"
      timeout       = 15
      memory        = 256
      trigger_event = "exp_discord"
      secrets       = []
    },
    privateMessage : {
      description   = "Send a private message to a user"
      runtime       = "go119"
      entry_point   = "PrivateMessage"
      timeout       = 15
      memory        = 256
      trigger_event = "private_message_discord"
      secrets       = ["DISCORD_TOKEN"]
    },
    frogeOfTheDay : {
      description   = "Publish the froge of the day"
      runtime       = "python39"
      entry_point   = "publish_froge_of_the_day"
      timeout       = 15
      memory        = 256
      trigger_event = "froge_of_the_day"
      secrets       = ["DISCORD_TOKEN"]
    },
    channelMessage : {
      description   = "Send a message to a channel"
      runtime       = "go119"
      entry_point   = "ChannelMessage"
      timeout       = 15
      memory        = 256
      trigger_event = "channel_message_discord"
      secrets       = ["DISCORD_TOKEN"]
    },
    cloudErrorLog : {
      description   = "Send the Google Cloud error log from pubsub to a specific channel"
      runtime       = "go119"
      entry_point   = "UnmarshalPubsubMessage"
      timeout       = 15
      memory        = 256
      trigger_event = "cloud_function_error_log"
      secrets       = ["DISCORD_TOKEN"]
    },
    updateUserRole : {
      description   = "Add roles to a user based on his level"
      runtime       = "go119"
      entry_point   = "UserRole"
      timeout       = 15
      memory        = 256
      trigger_event = "update_user_role"
      secrets       = ["DISCORD_TOKEN"]
    },
    generateLevelImage : {
      description   = "Generate the level image of a user"
      runtime       = "nodejs16"
      entry_point   = "generateLevelImage"
      timeout       = 15
      memory        = 1024
      trigger_event = "generate_level_image"
      secrets       = []
    },
    generateWelcomeImage : {
      description   = "Generate the Welcome image of a user"
      runtime       = "nodejs16"
      entry_point   = "generateWelcomeImage"
      timeout       = 15
      memory        = 1024
      trigger_event = "generate_welcome_image"
      secrets       = []
    },
  }
}