# Все ссылки a
# Условие:
# Выведите все ссылки, которые находятся в тегах a:
#
# <a target="_blank" href="https://stepik.org/">Hyperlink</a>
# Должно вывести:
#
# https://stepik.org/
# Что нужно сделать:
# Нужно найти последовательности, подходящие по следующим условиям:
#
# Ссылка находится в теге a
# Слева и справа от ссылки стоят двойные или одинарные кавычки
# Перед левой кавычкой стоит href=
# Сама ссылка может состоять из любых символов
# Длина ссылки как минимум 1 символ
# Попробуйте сначала найти все теги a, и только потом извлекайте из них ссылку.
#
# Тестовые данные:
# Входные данные:
# На вход программе подаётся 1 строка.


import re

test_case = [
    (
        '<html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Пролистай вниз</title><link rel="stylesheet" href="./css/normalize.css"><link rel="stylesheet" href="./css/style.css"><link rel="icon" href="./img/icon.jpg"></head><body><header><h1 class="privet">Привет!<br>Пролистай страничку вниз.</h1><img src="./img/photo.jpg" alt="" class="logo_icon"></header><main><p class="paragraph">Чтобы продолжить - отправь боту любое фото.</p></main><footer><a class="link" href="./img/photo.jpg" download="">Фото</a><p class="link">id стикера - CAACAgIAAxkBAAIDxWITCaZnaUelQ0SNlHMTrjd2klAmAAIBAQACVp29CiK-nw64wuY0IwQ</p><a class="link" href="./img/tochno.txt" download="">Документ</a></footer></body></html>',
        ['./img/photo.jpg', './img/tochno.txt']),
    ('<a target="_blank" href="https://stepik.org/">Hyperlink</a>', ['https://stepik.org/']),
    (
        '<a class="gb_8d gb_Jc" aria-label="Google Переводчик" href="/?hl=ru&amp;tab=TT" title="Google Переводчик"><span class="gb_Nc gb_5d" aria-hidden="true" role="presentation"></span><span class="gb_od gb_fd">Переводчик</span></a>',
        ['/?hl=ru&amp;tab=TT']),
    (
    """<a class="gb_d" aria-label="Приложения Google" href="https://www.google.com.ua/intl/ru/about/products?tab=Th" aria-expanded="false" role="button" tabindex="0"><svg class="gb_h" focusable="false" viewbox="0 0 24 24"><path d="M6,8c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM12,20c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM6,20c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM6,14c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM12,14c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM16,6c0,1.1 0.9,2 2,2s2,-0.9 2,-2 -0.9,-2 -2,-2 -2,0.9 -2,2zM12,8c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM18,14c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM18,20c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2z"></path></svg></a></div></div></div><div class="gb_b gb_Qd gb_4f gb_x"><div class="gb_g gb_eb gb_4f gb_x"><a class="gb_d gb_Ha gb_x" aria-label="Аккаунт Google: Станислав Никитенко  &#10;(nstanislass@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=ru&amp;continue=https://translate.google.com.ua/%3Fhl%3Dru%26tab%3DTT%26sl%3Den%26tl%3Dru%26text%3Danswer%26op%3Dtranslate&amp;ec=GBRAMw" role="button" tabindex="0"><img class="gb_k gbii" src="https://lh3.googleusercontent.com/ogw/AGvuzYZrlJqiZh4NeNZDkf6Cv3gKH_FuB17Q2FIQSlZ5=s32-c-mo" srcset="https://lh3.googleusercontent.com/ogw/AGvuzYZrlJqiZh4NeNZDkf6Cv3gKH_FuB17Q2FIQSlZ5=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/AGvuzYZrlJqiZh4NeNZDkf6Cv3gKH_FuB17Q2FIQSlZ5=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""></a></div></div></div></div></div><div class="gb_yd gb_ld"></div></header><div class="gb_Wc gb_Uc" ng-non-bindable="" role="navigation"><div class="gb_6c"><div class="gb_Hc"><div class="gb_Ic"><a class="gb_8d gb_Jc" aria-label="Google Переводчик" href="/?hl=ru&amp;tab=TT" title="Google Переводчик"><span class="gb_Nc gb_5d" aria-hidden="true" role="presentation"></span><span class="gb_od gb_fd">Переводчик</span></a></div></div></div><div class="gb_2c" role="menu"><div><c-wiz jsrenderer="lJVV9" jsshadow jsdata="deferred-i1" jscontroller="GILUZe" jsaction="click:cOuCgd;RI2Xre:Vtdxob;" data-node-index="0;0" jsmodel="hc6Ubd" c-wiz><div jsaction="click:igH3i(MMRVdf),Q3Z9wc(wNMsOe),SA7gC(h9d3hd),u56up(abkpZe);" jscontroller="s2XCRc" data-language-code="ru" role="contentinfo"><div class="GR2kEe"><a class="yJWPX" tabindex="0" href="https://translate.google.com/about/?hl=ru" jsname="wNMsOe">О Переводчике Google</a></div><div class="GR2kEe"><a class="yJWPX" tabindex="0" href="https://policies.google.com/?hl=ru" jsname="abkpZe">Правила и принципы</a><a class="yJWPX" tabindex="0" href="https://support.google.com/translate/?hl=ru" jsname="h9d3hd" data-probe-id="help_menu_link">Справка</a><a class="yJWPX" tabindex="0" jsaction="click:AmrRnd,x0AZNc,wozWQb;" jsname="N7Eqid" role="button">Отправить отзыв</a><a class="yJWPX" tabindex="0" href="https://www.google.com/about?hl=ru" jsname="MMRVdf">О Google</a></div></div><c-data id="i1"></c-data></c-wiz><script aria-hidden="true" nonce="t_nRakFebGj-fSykBl1_Qg">window.wiz_progress&&window.wiz_progress();window.wiz_tick&&window.wiz_tick('lJVV9');</script></div></div></div></div><script nonce="t_nRakFebGj-fSykBl1_Qg">this.gbar_=this.gbar_||{};(function(_){var window=this; try{""",
    ['https://www.google.com.ua/intl/ru/about/products?tab=Th',
     'https://accounts.google.com/SignOutOptions?hl=ru&amp;continue=https://translate.google.com.ua/%3Fhl%3Dru%26tab%3DTT%26sl%3Den%26tl%3Dru%26text%3Danswer%26op%3Dtranslate&amp;ec=GBRAMw',
     '/?hl=ru&amp;tab=TT', 'https://translate.google.com/about/?hl=ru', 'https://policies.google.com/?hl=ru',
     'https://support.google.com/translate/?hl=ru', 'https://www.google.com/about?hl=ru'])

]
for i, (test, answer) in enumerate(test_case, 1):
    result = re.findall(r'<a.+?href=[\"\'](.+?)[\"\']', test)
    assert result == answer, f'TEST №{i}\nError in {test}\n{result} != {answer}'
    print(f'TEST №{i} - OK')
