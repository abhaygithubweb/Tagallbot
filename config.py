from os import getenv
from dotenv import load_dotenv

load_dotenv()

#Necessary Variables 
API_ID = int(getenv("API_ID", "29400566")) 
API_HASH = getenv("API_HASH", "8fd30dc496aea7c14cf675f59b74ec6f")
BOT_TOKEN = getenv("BOT_TOKEN", "7183295941:AAE0-CcUNxRb7qJVlgJmTz-QIH1n8IbAt18") #Put your bot token here
LOG_ID = int(getenv("LOG_ID", "-1002022578109"))
SUDOERS = list(map(int, getenv("SUDOERS", "6717765982").split()))


TXT = [
    "Kaha busy rehte ho😒",
    "Ye lo Mera dil torna mt🙈",
    "Kaise h aap to baat hi nhi krte🥹💔",
    "Insta I'd ky h aapki?",
    "Me garib hu kuchh donate kr do🫠",
    "ajao vc pr gany sunty han🥲",
    "Ye lo Mera dil❤️‍🔥 bhut kimti h ye",
    "Aapse mil kr khushu Hui",
    "Khana kha liya aapne? 🍲",
    "Kya aapne naye gaane suney? 🎶",
    "Aaj mausam kaisa hai? 🌦",
    "Kya aapne kuch interesting padha hai aajkal? 📚",
    "Aapka weekend kaisa raha? 🎉",
    "Aapka favorite movie kaunsi hai? 🎬",
    "Kya aapne aaj kuch naya try kiya? 🆕",
    "Kya aapne kisi ko muskurahat di aaj? 😊",
    "Aapka favorite vacation spot kahan hai? 🏖",
    "Aapne kya socha aaj subah uthkar? 🌅",
    "Kya aapko ghar ka khana yaad aata hai kabhi? 🏡🍲",
    "Aapka favorite book kaunsi hai? 📖",
    "Kya aapne aaj kisi ko help kiya? 🤝",
    "Aapne kya socha aaj ka din kaise guzrega? 💭",
    "Kya aapne aaj kisi ko yaad kiya? ❤️",
    "Vc chalo bate krte h kuchh kuchh",
    "Do u know who is my owner?",
    "Kuchh bol q na rhe ho?",
    "Kaha se ho aap?",
    "Mene aapko bhut Miss kiya aaj🥹❤️‍🔥",
    "Aao aak party krte h😁⚡️",
    "Saam ko park me chale ?",
    "Love garden kidhar h? Mujhe aapke sath Jana h🙈",
    "Aapne Mera dil churaya h",
    "Aap kitne sweet h🤭🥰",
    "Oye online q na aate ho aap?",
    "Aaj itni late se q uthe?",
    "Aaj mene tumhe bar me dekha tha😒",
    "Aap itne chup q rehte h?",
    "Ghar me sab kaise h ji?",
    "Mere sath long drive me chalogi?",
    "Aapki hairstyle mujhe bhut achhi lgti h",
    "Suno ek baat batani thi tumhe",
    "I love u 🙈",
    "Ky aapke v dost garib h😁😆",
    "Aap grp me na aate to Mera dil hi na lgta🥹",
    "on aja bhai",
    "kitna soye ga bhai tu",
    "gali q di thi kal muje",
    "paisa dede thora",
    "chlo datepr chlyn",
    "where are you babe",
    "hello",
    "good morning my love",
    "good night babe",
    "good afternoon",
    "sb soty rhty han idhr",
    "ankhy khol le bhai",
    "uth jao ab to babe",
]
