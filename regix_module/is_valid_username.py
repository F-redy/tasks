# Стена, верни Дурова!
# Условие:
# У Дурова отжали ВКонтакте, но он не сдался и создал уже не социальную сеть, а мессенджер - Телеграм.
# Вы наверное знаете, что в Телеграме любой пользователь может выбрать себе username, чтобы его было легче искать.
# Давайте поможем Паше и напишем регулярное выражение, которое будет проверять валидность username.
#
# Что нужно найти:
# username, в котором выполняются следующие условия:
# Используются символы a-z, A-Z, 0-9, _, -
# Длина от 5 до 32 символов включительно
# Не может начинаться с цифры или _ или -
# Не может заканчиваться на _ или -

# На самом деле есть ещё одно условие: username не может содержать в себе __, или --
# но на данный момент сделать такое будет трудновато.

import re


def is_valid_username(entered_username: str):
    pattern = r"(?<!\S)[a-zA-Z][a-zA-Z0-9_-]{3,30}[a-zA-Z0-9](?!\S)"
    entered_username = re.match(pattern, entered_username.strip())

    return entered_username.group(0) if entered_username else False


usernames = ['hazzus', 'tegmilan', 'lordvladtheimpalertransylvania', 'anxkhn', 'cksnb', 'tatotan', 'plashspeed',
             'mikesew1320', 'i_am_just_as_cringe', 'meertkrts', 'megajoy', 'hexwrty', 'yltned', 'origincode',
             'freedomnesss', 'sayakamiki', 'mohammedbablasi', 'posi_farmer_ranjan', 'lesikvip', 'th_bst', 'aryansamra',
             'necrowitch', 'xxkhanxx', 'nome_tg', 'aless1010', 'sudo_nautilus', 'try2prog', 'devonpython', 'the_jug',
             'databankco', 'du3ei', 'lenni_builder', 'aemangar', 'uwuth', 'hz_lucifer', 'kangaroointernational',
             'scagionare', 'mahi747', 'andrey_rucvc', 'joker_asd_s', 'alk_is_noob', 'o_osp_bcf_offi', 'haiz_me',
             'xtremeornob', 'skiduchiha', 'meizishandev', 'nitrovenom', 'plankff', 'glocktwentyone', 'faizbastomi',
             'antihallobst', 'erdils', 'helledryn', 'kircheiss', 'av7m7x', 'tarbless', 'i0i#r', 'kigd@2',
             'taaphli-octoandri', 'crypticfrоg', 'тест', 'suDhAsa010', 'Thematdev', 'oo?om09', 'ooo>m11', 'sac<charose',
             'thekillerbun$ny12341', 'shuse!kagari', 'du%eru42', 'hy&perterminal', 'su*theta', 'adb(reboot)bootloader',
             'marb=ololo', 'theminidev', 'a_e_i_o_u_hacker143', 'aldyhk', 'bio_chain_2_bot', 'miiiiiyt', 'bederke',
             'barry021', 'aikaravinu', 'romangraef', 'awidok', 'mechanarutosucks', 'SpamBot', 'GroupAnonymousBot']

allowed_usernames = ['hazzus', 'tegmilan', 'lordvladtheimpalertransylvania', 'anxkhn', 'cksnb', 'tatotan', 'plashspeed',
                     'mikesew1320', 'i_am_just_as_cringe', 'meertkrts', 'megajoy', 'hexwrty', 'yltned', 'origincode',
                     'freedomnesss', 'sayakamiki', 'mohammedbablasi', 'posi_farmer_ranjan', 'lesikvip', 'th_bst',
                     'aryansamra', 'necrowitch', 'xxkhanxx', 'nome_tg', 'aless1010', 'sudo_nautilus', 'try2prog',
                     'devonpython', 'the_jug', 'databankco', 'du3ei', 'lenni_builder', 'aemangar', 'uwuth',
                     'hz_lucifer', 'taaphli-octoandri', 'mechanarutosucks', 'SpamBot', 'GroupAnonymousBot',
                     'kangaroointernational', 'scagionare', 'mahi747', 'andrey_rucvc', 'joker_asd_s', 'alk_is_noob',
                     'o_osp_bcf_offi', 'haiz_me', 'xtremeornob', 'skiduchiha', 'meizishandev', 'nitrovenom', 'plankff',
                     'glocktwentyone', 'faizbastomi', 'antihallobst', 'erdils', 'helledryn', 'kircheiss', 'av7m7x',
                     'tarbless', 'suDhAsa010', 'Thematdev', 'theminidev', 'a_e_i_o_u_hacker143', 'aldyhk',
                     'bio_chain_2_bot', 'miiiiiyt', 'bederke', 'barry021', 'aikaravinu', 'romangraef', 'awidok',
                     ]

for test_username in usernames:
    allowed_username = is_valid_username(test_username)
    if allowed_username:
        assert allowed_username in allowed_usernames, f'{allowed_username} not allowed ✘'
        print(f'{allowed_username} - allowed ✔')
