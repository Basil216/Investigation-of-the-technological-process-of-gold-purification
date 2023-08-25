#!/usr/bin/env python
# coding: utf-8

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# Привет, Алексей. 03.06.23 жесткий дэдлайн. можешь проверять мою работу немного быстрее? заранее спасибо.
# </font>

# In[1]:





# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# <b> Василий, привет!👋</b>
# 
# Меня зовут Алексей Гриб, и я буду ревьюером твоего проекта. 
# 
# Сразу хочу предложить в дальнейшем общаться на "ты" - надеюсь, так будет комфортнее:) Но если это неудобно, обязательно дай знать, и мы придумаем что-нибудь ещё!
#     
# Цель ревью - не искать ошибки в твоём проекте, а помочь тебе сделать твою работу ещё лучше, устранив недочёты и приблизив её к реальным задачам аналитика. Поэтому не расстраивайся, если что-то не получилось с первого раза - это нормально, и это поможет тебе вырасти!
#     
# Ты можешь найти мои комментарии, обозначенные <font color='green'>зеленым</font>, <font color='gold'>желтым</font> и <font color='red'>красным</font> цветами, например:
# 
# <br/>
# 
# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> похвала, рекомендации «со звёздочкой», полезные лайфхаки, которые сделают и без того красивое решение ещё более элегантным.
# </div>
# 
# <br/>
# 
# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> некритичные ошибки или развивающие рекомендации на будущее. 
# </div>
# 
# 
# <br/>
# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Критичные ошибки, которые обязательно нужно исправить.
# </div>
# 
# Я не смогу принять проект, если в нём будет хотя бы одна критичная ошибка или несколько некритичных ошибок - тогда проект нужно будет немного доработать. Но это нестрашно - я обязательно дам тебе подсказку или укажу верное направление.
#     
# Пожалуйста, не удаляй мои комментарии, они будут особенно полезны для нашей работы в случае повторной проверки проекта. 
#     
# Ты также можешь задавать свои вопросы, реагировать на мои комментарии, делать пометки и пояснения - полная творческая свобода! Но маленькая просьба - пускай они будут отличаться от моих комментариев, это поможет избежать путаницы в нашем общении:)
# Например, вот так:
#     
# <div class="alert alert-info">
# <h2> Комментарий студента <a class="tocSkip"> </h2>
# 
# *твой текст*
# </div>
#     
# Давай посмотрим на твой проект!

# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
#         Привет. меня зовут Василий Польской. 
# </b></font>
# </div>

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fffdd0'>привет Алексей. рад знакомству. ты конечно от души написал, за раз столько не осилить.</font>
# </div>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Давай смотреть, всё ли получилось:)

# <h1>Содержание<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Подготовка-данных" data-toc-modified-id="Подготовка-данных-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Подготовка данных</a></span><ul class="toc-item"><li><span><a href="#знакомимся-с-data_full" data-toc-modified-id="знакомимся-с-data_full-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>знакомимся с data_full</a></span></li><li><span><a href="#знакомимся-с-data_train" data-toc-modified-id="знакомимся-с-data_train-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>знакомимся с data_train</a></span></li><li><span><a href="#знакомимся-с-data_test" data-toc-modified-id="знакомимся-с-data_test-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>знакомимся с data_test</a></span></li><li><span><a href="#MAE-между-вашими-расчётами-и-значением-rougher.output.recovery" data-toc-modified-id="MAE-между-вашими-расчётами-и-значением-rougher.output.recovery-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>MAE между вашими расчётами и значением rougher.output.recovery</a></span></li></ul></li><li><span><a href="#Анализ-данных" data-toc-modified-id="Анализ-данных-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Анализ данных</a></span><ul class="toc-item"><li><span><a href="#изменение-концентрации-элементов-на-каждом-этапе" data-toc-modified-id="изменение-концентрации-элементов-на-каждом-этапе-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>изменение концентрации элементов на каждом этапе</a></span></li><li><span><a href="#почистим-данные" data-toc-modified-id="почистим-данные-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>почистим данные</a></span></li><li><span><a href="#распределения-размеров-гранул-на-обучающей-и-тестовой-выборках" data-toc-modified-id="распределения-размеров-гранул-на-обучающей-и-тестовой-выборках-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>распределения размеров гранул на обучающей и тестовой выборках</a></span></li><li><span><a href="#&quot;лишние&quot;-колонки-в-data_train" data-toc-modified-id="&quot;лишние&quot;-колонки-в-data_train-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>"лишние" колонки в data_train</a></span></li><li><span><a href="#обработка-пропусков" data-toc-modified-id="обработка-пропусков-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>обработка пропусков</a></span></li><li><span><a href="#восстановление-целевых-признаков" data-toc-modified-id="восстановление-целевых-признаков-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>восстановление целевых признаков</a></span></li></ul></li><li><span><a href="#Модель" data-toc-modified-id="Модель-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Модель</a></span><ul class="toc-item"><li><span><a href="#sMAPE-функция" data-toc-modified-id="sMAPE-функция-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>sMAPE функция</a></span></li><li><span><a href="#Итоговая-sMAPE-функция" data-toc-modified-id="Итоговая-sMAPE-функция-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Итоговая sMAPE функция</a></span></li><li><span><a href="#подготовим-данные-для-обучения-моделей" data-toc-modified-id="подготовим-данные-для-обучения-моделей-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>подготовим данные для обучения моделей</a></span></li><li><span><a href="#проверим-модели-на-кросс-валидации" data-toc-modified-id="проверим-модели-на-кросс-валидации-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>проверим модели на кросс-валидации</a></span></li><li><span><a href="#случайный-лес-(target_train_rougher_output_recovery)" data-toc-modified-id="случайный-лес-(target_train_rougher_output_recovery)-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>случайный лес (target_train_rougher_output_recovery)</a></span></li><li><span><a href="#случайный-лес-(target_train_final_output_recovery)" data-toc-modified-id="случайный-лес-(target_train_final_output_recovery)-3.6"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>случайный лес (target_train_final_output_recovery)</a></span></li><li><span><a href="#проверка-на-тестовой-выборке" data-toc-modified-id="проверка-на-тестовой-выборке-3.7"><span class="toc-item-num">3.7&nbsp;&nbsp;</span>проверка на тестовой выборке</a></span></li><li><span><a href="#Считаем-итоговое-sMAPE" data-toc-modified-id="Считаем-итоговое-sMAPE-3.8"><span class="toc-item-num">3.8&nbsp;&nbsp;</span>Считаем итоговое sMAPE</a></span></li><li><span><a href="#dummy-model" data-toc-modified-id="dummy-model-3.9"><span class="toc-item-num">3.9&nbsp;&nbsp;</span>dummy model</a></span></li></ul></li><li><span><a href="#Вывод" data-toc-modified-id="Вывод-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Вывод</a></span></li></ul></div>

# # Восстановление золота из руды

# Подготовьте прототип модели машинного обучения для «Цифры». Компания разрабатывает решения для эффективной работы промышленных предприятий.
# 
# Модель должна предсказать коэффициент восстановления золота из золотосодержащей руды. Используйте данные с параметрами добычи и очистки. 
# 
# Модель поможет оптимизировать производство, чтобы не запускать предприятие с убыточными характеристиками.
# 
# Вам нужно:
# 
# 1. Подготовить данные;
# 2. Провести исследовательский анализ данных;
# 3. Построить и обучить модель.
# 
# Чтобы выполнить проект, обращайтесь к библиотекам *pandas*, *matplotlib* и *sklearn.* Вам поможет их документация.

# # Цель - подобрать лучшую модель.
# подобрать модель и гиперпараметры для нее для получения самых точных предсказаий коэффициента восстановления золота из руды.

# исходя из задачи
# `
# Модель должна предсказать коэффициент восстановления золота из золотосодержащей руды. В вашем распоряжении данные с параметрами добычи и очистки.
# `
# колонки с информацией о других ископаемых, кроме золота, нам не нужны.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Хорошее вступление!
#     
# В нём есть всё, что необходимо, чтобы понять суть проекта с первых строк отчёта!

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score, make_scorer

from IPython.core.display import display, HTML


# In[5]:


get_ipython().run_line_magic('pinfo', 'pd.is_monotonic')


# In[2]:


#display(HTML("<style>.container { width:80% !important; }</style>"))
pd.options.display.max_columns = 100
pd.options.display.max_rows = 100

Данные находятся в трёх файлах:
gold_industry_train.csv — обучающая выборка;
gold_industry_test.csv — тестовая выборка;
gold_industry_full.csv — исходные данные.
# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Библиотеки импортировали - отлично!

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Я вижу, исполнение твоего кода начинается в ячейке с номером, который отличается от единицы. Перед отправкой проекта стоит проверять работоспособность кода — это можно сделать, нажав на панели Jupiter Hub ``Kernel`` и ``Restart & Run All`` (см скриншот ниже).
# 
# ![](https://i.postimg.cc/yd19rYf6/Screenshot-428.png)
#         
# Важно также убедиться, что все ячейки проекта исполнились - можно просто пролистать работу до конца и убедиться, что последняя ячейка исполнена. Такая проверка поможет тебе убедиться, что твоё решение будет должным образом воспроизведено во время ревью или во время передачи его заказчику - это очень важный этап, пренебрегать которым не стоит:)

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Актуально.

# ## Подготовка данных

# In[3]:


# загрузим данные из файлов

data_train = pd.read_csv('/datasets/gold_industry_train.csv')
data_test = pd.read_csv('/datasets/gold_industry_test.csv')
data_full = pd.read_csv('/datasets/gold_industry_full.csv')


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍</b> 
#     
# Данные загрузили.
#     
# При считывании данных из файла здорово перестраховывать себя от ошибок, связанных, например, с неверным указанием пути к файлу. А иногда бывает, что работаешь с файлом локально, выгружаешь его на сервер, ожидая, что он будет принимать данные, которые лежат на том же сервере, а код падает с ошибкой, потому что путь к файлу не поменялся с локального на серверный.
#     
# Для этого, например, можно использовать конструкцию `try-except`: сначала пробуешь локальный путь, при возникновении ошибки используется серверный путь (подробнее можешь почитать тут: https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html).
#     
# Но еще лучше использовать библиотеку `os` - её использование позволит тебе проверять существование указанных директорий (что может быть актуально при одновременной работа на локальном и сетевом окружении) и загружать данные из существующей директории, избегая ошибок. Как пример:
#     
#     import os
# 
#     pth1 = '/folder_1/data.csv'
#     pth2 = '/folder_2/data.csv'
#     
#     if os.path.exists(pth1):
#         query_1 = pd.read_csv(pth1)
#     elif os.path.exists(pth2):
#         query_1 = pd.read_csv(pth2)
#     else:
#         print('Something is wrong')
# 
# Ещё на этапе считывания данных можно спарсить дату: за это действие отвечает параметр `parse_dates` метода `read_csv()`, в него нужно передать список с названием полей-дат, и в большинстве случаев дата будет корректно преобразована в нужный формат сразу:)
# Также на этапе считывания данных задать индекс-столбец- за это действие отвечает параметр `index_col`.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fffdd0'>посмотрю на досуге. встречал уже подобный подход но не вникал.</font>
# </div>

# In[4]:


def data_tester(df):
    '''
    функция получает на вход дата фрейм и выводит информацию о нем, ту что нам надо.
    '''
    display(df.info())
    display(df.head())
    display(df.shape)
    display('наличие понных дубликатов', df.duplicated().sum())
    # display('describe анализ', df.describe())
    # display('считаем пропуски', df.isna().sum())    


# In[5]:


def pass_value_barh(df): # спасибо Ринату Хисамову
    '''
    функция получает на вход датафрейм и возвращает график с пропусками в данных.
    симпотичное решение повседневной задачи.
    '''
    try:
        (
            (df.isna().sum())
            .to_frame()
            .rename(columns = {0:'space'})
            .query('space > 0')
            .sort_values(by = 'space', ascending = True)
            .plot(kind = 'barh', figsize = (40,40), legend = False, fontsize = 40)
            .set_title("\n" + 'Пропуски' + "\n", fontsize = 70)

        ); 
        plt.xlabel('Количество пропусков, шт.', fontsize = 40);
        plt.ylabel('Колонки с пропусками', fontsize = 40);
    except:
        print('пропусков не осталось :) или произошла ошибка в первой части функции ')


# ### знакомимся с data_full

# In[6]:


data_tester(data_full)


# In[7]:


pass_value_barh(data_full)


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 
# На графиках нужно подписать оси Х и Y.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fffdd0'>добавил.</font>
# </div>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
# data_full
#         
# количество строк / стобцов - 19439 / 87
#         
# очень много пропусков в данных. 
#         
# больше всего пропусков в `secondary_cleaner.output.tail_sol` - 1748. если эти данные не пригодятся - трогать не буду или удалю весь столбец
#         
#         
#         
# </b></font>
# </div>

# ### знакомимся с data_train

# In[8]:


data_tester(data_train)


# In[9]:


pass_value_barh(data_train)


# 
# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
# data_train
#         
# количество строк / стобцов - 14579 / 87 
#         
# очень много пропусков в данных. 
#         
# нужно посмотреть что внутри других таблиц. потом подумать что делать с пропусками.....
# </b></font>
# </div>
# 

# ### знакомимся с data_test

# In[10]:


data_tester(data_test)


# In[11]:


pass_value_barh(data_test)


# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
# data_test
#         
# количество строк / стобцов - 4860 / 53 
#         
# по сравнению с data_full и data_train в тестовой выборке 53 столбца.
# надо понять каких не хватает и удалить из трейна лишнее
#         
# как заполнять пропуски все еще не понятно
# </b></font>
# </div>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍</b> 
#     
# Данные осмотрели - интересное решение для анализа таблиц:)

# ### MAE между вашими расчётами и значением rougher.output.recovery

# 1.2. Проверьте, что эффективность обогащения рассчитана правильно.
# Вычислите её на обучающей выборке для признака `rougher.output.recovery`.
# Найдите MAE между вашими расчётами и значением признака. Опишите выводы.
# 

# для расчета `rougher.output.recovery` используем значения 'rougher.output.concentrate_au', 'rougher.input.feed_au', 'rougher.output.tail_au'

# ![image.png](attachment:image.png)

# где:
# - C — доля золота в концентрате после флотации/очистки (`rougher.output.concentrate_au`);
# - F — доля золота в сырье/концентрате до флотации/очистки (`rougher.input.feed_au`);
# - T — доля золота в отвальных хвостах после флотации/очистки (`rougher.output.tail_au`).
# 
# Для прогноза коэффициента нужно найти долю золота в концентратах и хвостах. Причём важен не только финальный продукт, но и черновой концентрат.

# In[12]:


def recovery_calculat(df):
    '''
    функция получает на вход датафрейм
    возвращает значение recovery
    recovery = (c * (f - t))/(f * (c - t))*100
    где:
    C — доля золота в концентрате после флотации/очистки (`rougher.output.concentrate_au`);
    F — доля золота в сырье/концентрате до флотации/очистки (`rougher.input.feed_au`);
    T — доля золота в отвальных хвостах после флотации/очистки (`rougher.output.tail_au`).
    '''
    try:
        c = df['rougher.output.concentrate_au']
        f = df['rougher.input.feed_au']
        t = df['rougher.output.tail_au']
        recovery = (c * (f - t))/(f * (c - t))*100
        return recovery
    except:
        print('параметры recovery_calculat заданы не верно')


# In[13]:


print(recovery_calculat(data_train).head())
# тестим функцию. работает.


# In[14]:


# посчитаем МАЕ для 'rougher.output.recovery' и расчетных значении

mae = mean_absolute_error(data_train['rougher.output.recovery'], recovery_calculat(data_train))
print('Среднеквадратичное отклонение:', mae)


# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
#         Среднеквадратичное отклонение: 9.83758577644259e-15 - очень маленькое число, для здравого смысла можно прировнять его к нулю.
# 
# следовательно, между данными таблицы и расчетными данными разницы нет, мы смело можем доверять цифрам из таблицы. 
# </b></font>
# </div>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Оценили `MAE` между исходным и расчётным значением эффективности обогащения и убедились, что эффективность обогащения рассчитана правильно - отлично!
# </div>

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Здесь заканчивается стрктурный блок работы - стоит делать промежуточные выводы о проделанной работе, это довольно полезная практика, которая имеет большую ценность для получателя отчёта.
#         
# Достаточно будет двух-трёх тезисных предложений об основных шагах и полученных выводах.
#         
# </div>

# ## Анализ данных

# ### изменение концентрации элементов на каждом этапе

# In[15]:


display(list(data_train.columns))


# 1. 'date' - дата записи строки - потом преобразуется в индекс строки
# 2. 'rougher.input.feed_au' - содержание золота в начальном сырье
# 3. 'rougher.input.feed_ag' - содержание серебра в начальном сырье
# 4. 'rougher.input.feed_pb' - содержание свинца в начальном сырье
# 5. 'rougher.input.feed_sol' - содержание солей (или минералов?) в начальном сырье
# 6. 'rougher.input.feed_rate'- скорость подачи...??
# 7. 'rougher.input.feed_size' - размер гранул чего-то...
# 8. 'rougher.input.floatbank10_sulfate',
# 9. 'rougher.input.floatbank10_xanthate',
# 10. 'rougher.state.floatbank10_a_air',
# 11. 'rougher.state.floatbank10_a_level',
# 12. 'rougher.state.floatbank10_b_air',
# 13. 'rougher.state.floatbank10_b_level',
# 14. 'rougher.state.floatbank10_c_air',
# 15. 'rougher.state.floatbank10_c_level',
# 16. 'rougher.state.floatbank10_d_air',
# 17. 'rougher.state.floatbank10_d_level',
# 18. 'rougher.state.floatbank10_e_air',
# 19. 'rougher.state.floatbank10_e_level',
# 20. 'rougher.state.floatbank10_f_air',
# 21. 'rougher.state.floatbank10_f_level',
# 22. 'rougher.input.floatbank11_sulfate',
# 23. 'rougher.input.floatbank11_xanthate',
# 24. 'rougher.calculation.sulfate_to_au_concentrate',
# 25. 'rougher.calculation.floatbank10_sulfate_to_au_feed',
# 26. 'rougher.calculation.floatbank11_sulfate_to_au_feed',
# 27. 'rougher.calculation.au_pb_ratio',
# 28. 'rougher.output.concentrate_au' - содержание золота в сырье после флотации
# 29. 'rougher.output.concentrate_ag' - содержание серебра в сырье после флотации
# 30. 'rougher.output.concentrate_pb' - содержание свинца в сырье после флотации
# 31. 'rougher.output.concentrate_sol' - содержание солей в сырье после флотации
# 32. 'rougher.output.recovery',
# 33. 'rougher.output.tail_au' - содержание золота в хвостах после флотации
# 34. 'rougher.output.tail_ag' - содержание серебра в хвостах после флотации
# 35. 'rougher.output.tail_pb' - содержание свинца в хвостах после флотации
# 36. 'rougher.output.tail_sol' - содержание солей в хвостах после флотации
# 37. 'primary_cleaner.input.sulfate' - количество сульфата при первичной очистке
# 38. 'primary_cleaner.input.depressant',
# 39. 'primary_cleaner.input.feed_size' - размер гранул после первичной очистки
# 40. 'primary_cleaner.input.xanthate',
# 41. 'primary_cleaner.state.floatbank8_a_air',
# 42. 'primary_cleaner.state.floatbank8_a_level',
# 43. 'primary_cleaner.state.floatbank8_b_air',
# 44. 'primary_cleaner.state.floatbank8_b_level',
# 45. 'primary_cleaner.state.floatbank8_c_air',
# 46. 'primary_cleaner.state.floatbank8_c_level',
# 47. 'primary_cleaner.state.floatbank8_d_air',
# 48. 'primary_cleaner.state.floatbank8_d_level',
# 49. 'primary_cleaner.output.concentrate_au' - содержание золота в сырье после первичной очистки
# 50. 'primary_cleaner.output.concentrate_ag' - содержание серебра в сырье после первичной очистки
# 51. 'primary_cleaner.output.concentrate_pb' - содержание свенца в сырье после первичной очистки
# 52. 'primary_cleaner.output.concentrate_sol' - содержание солей в сырье после первичной очистки
# 53. 'primary_cleaner.output.tail_au' - содержание золота в хвостах после первичной очистки
# 54. 'primary_cleaner.output.tail_ag' - содержание серебра в хвостах после первичной очистки
# 55. 'primary_cleaner.output.tail_pb' - содержание свинца в хвостах после первичной очистки
# 56. 'primary_cleaner.output.tail_sol' - содержание солей в хвостах после первичной очистки
# 57. 'secondary_cleaner.state.floatbank2_a_air',
# 58. 'secondary_cleaner.state.floatbank2_a_level',
# 59. 'secondary_cleaner.state.floatbank2_b_air',
# 60. 'secondary_cleaner.state.floatbank2_b_level',
# 61. 'secondary_cleaner.state.floatbank3_a_air',
# 62. 'secondary_cleaner.state.floatbank3_a_level',
# 63. 'secondary_cleaner.state.floatbank3_b_air',
# 64. 'secondary_cleaner.state.floatbank3_b_level',
# 65. 'secondary_cleaner.state.floatbank4_a_air',
# 66. 'secondary_cleaner.state.floatbank4_a_level',
# 67. 'secondary_cleaner.state.floatbank4_b_air',
# 68. 'secondary_cleaner.state.floatbank4_b_level',
# 69. 'secondary_cleaner.state.floatbank5_a_air',
# 70. 'secondary_cleaner.state.floatbank5_a_level',
# 71. 'secondary_cleaner.state.floatbank5_b_air',
# 72. 'secondary_cleaner.state.floatbank5_b_level',
# 73. 'secondary_cleaner.state.floatbank6_a_air',
# 74. 'secondary_cleaner.state.floatbank6_a_level',
# 75. 'secondary_cleaner.output.tail_au' - содержание золота в хвостах после вторичной очистки
# 76. 'secondary_cleaner.output.tail_ag' - содержание серебра в хвостах после вторичной очистки
# 77. 'secondary_cleaner.output.tail_pb' - содержание свинца в хвостах после вторичной очистки
# 78. 'secondary_cleaner.output.tail_sol' - содержание солей в хвостах после вторичной очистки
# 79. 'final.output.concentrate_au' - содержание золота после вторичной очистки
# 80. 'final.output.concentrate_ag' - содержание серебра после вторичной очистки
# 81. 'final.output.concentrate_pb' - содержание свинца после вторичной очистки
# 82. 'final.output.concentrate_sol' - содержание солей после вторичной очистки
# 83. 'final.output.recovery' - финальный коэффициент восстановления золота из руды
# 84. 'final.output.tail_au' - содержание золота в хвостах
# 85. 'final.output.tail_ag' - содержание веребра в хвостах
# 86. 'final.output.tail_pb' - содержание свинца в хвостах
# 87. 'final.output.tail_sol' - содержание солей в хвостах

# In[16]:


# золото поэтапно

data_au_out_train = data_train[
    [
        'rougher.input.feed_au', # содержание золота в начальном сырье
        'rougher.output.concentrate_au', # содержание золота в сырье после флотации
        'primary_cleaner.output.concentrate_au', # содержание золота в сырье после первичной очистки
        'final.output.concentrate_au' # содержание золота после вторичной очистки
    ]
]
data_au_out_train.head()


# In[17]:


for i in data_au_out_train.columns:
    data_au_out_train[i].to_frame().boxplot(vert = False, figsize = (20, 3));
    title = f'значение показателя {i}'
    plt.title(title + "\n", fontsize = 20)
    plt.xlabel('коэффициент содержания золота' + "\n", fontsize = 20);
    plt.show()


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 
# Тут и далее на графиках удно полписать ось Х, а также сделать более информативные названия.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fffdd0'>вот как-то так смог.</font>
# </div>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
# на боксплотах хорошо видно что после каждого этапа концентрация золота в руде увеличивается
# </b></font>
# </div>

# In[18]:


# серебро по этапно

data_ag_out_train = data_train[
    [
        'rougher.input.feed_ag', # содержание серебра в начальном сырье
        'rougher.output.concentrate_ag', # содержание серебра в сырье после флотации
        'primary_cleaner.output.concentrate_ag', # содержание серебра в сырье после первичной очистки
        'final.output.concentrate_ag' # содержание серебра после вторичной очистки
    ]
]
data_ag_out_train.head()


# In[19]:


for i in data_ag_out_train.columns:
    data_ag_out_train[i].to_frame().boxplot(vert = False, figsize = (20, 3));
    title = f'значение показателя {i}'
    plt.title(title + "\n", fontsize = 20)
    plt.xlabel('коэффициент содержания серебра' + "\n", fontsize = 20);
    plt.show()


# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
# про серебро видим что к финалу обработки руды его стало почти в двое меньше начального
# </b></font>
# </div>

# In[20]:


# посмотрим что со свинцом

data_pb_out_train = data_train[
    [
        'rougher.input.feed_pb', # содержание свинца в начальном сырье
        'rougher.output.concentrate_pb', # содержание свинца в сырье после флотации
        'primary_cleaner.output.concentrate_pb', # содержание свинца в сырье после первичной очистки
        'final.output.concentrate_pb' # содержание свинца после вторичной очистки
    ]
]
data_pb_out_train.head()


# In[21]:


for i in data_pb_out_train.columns:
    data_pb_out_train[i].to_frame().boxplot(vert = False, figsize = (20, 3));
    title = f'значение показателя {i}'
    plt.title(title + "\n", fontsize = 20)
    plt.xlabel('коэффициент содержания свинца' + "\n", fontsize = 20);
    plt.show()


# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
# концентрация свинца к концу обработки увеличилась. возможно это связано с близким к золоту молекулярным составом
# </b></font>
# </div>

# In[22]:


# соль, соли, минералы??

data_sol_out_train = data_train[
    [
        'rougher.input.feed_sol',
        'rougher.output.concentrate_sol',
        'primary_cleaner.output.concentrate_sol',
        'final.output.concentrate_sol'
    ]
]
data_sol_out_train.head()


# In[23]:


for i in data_sol_out_train.columns:
    data_sol_out_train[i].to_frame().boxplot(vert = False, figsize = (20, 3));
    title = f'значение показателя {i}'
    plt.title(title + "\n", fontsize = 20)
    plt.xlabel('коэффициент содержания солей' + "\n", fontsize = 20);
    plt.show()


# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
# концентрация соли оочень сильно снизилась к финалу обработки.
# </b></font>
# </div>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Исследована концентрация металлов на разных стадиях обработки, проанализирована динамика концентрации в зависимости от этапа техпроцесса - отлично, тут всё верно.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# На данном этапе следует также избавиться от аномалий: давай обратим внимание на левую сторону графика по оси Х - все ли значения, которые мы там видим, кажутся адекватными?

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fffdd0'>по боксплотам видно что есть прям аномальные выбросы в некоторых колонках. я их специально не стал удалять, думается мне что это не помешает обучению модели. поправь если я не прав.
#     </font>
# </div

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Нужно удалить аномалии как минимум в виде нулевых значений - содержание металла в породе не должно быть нулевым для корректной работы модели. В идеале - почистить от выбросов в принципе, используя тот же `boxplot()`, персентили или межквартильный размах.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# ### почистим данные
# удалим нулевые значения из колонок с содержанием металлов

# In[24]:


data_train = data_train[
    (data_train['rougher.input.feed_au'] > 1) &
    (data_train['rougher.output.concentrate_au'] > 5) &
    (data_train['primary_cleaner.output.concentrate_au'] > 10) &
    (data_train['final.output.concentrate_au'] > 10) &
    (data_train['rougher.input.feed_ag'] > 1) &
    (data_train['rougher.output.concentrate_ag'] > 2) &
    (data_train['primary_cleaner.output.concentrate_ag'] > 1) &
    (data_train['final.output.concentrate_ag'] > 0.5) &
    (data_train['rougher.input.feed_pb'] > 0.5) &
    (data_train['rougher.output.concentrate_pb'] > 0.5) &
    (data_train['primary_cleaner.output.concentrate_pb'] > 0.5) &
    (data_train['final.output.concentrate_pb'] > 1)
]

# проверка
display((data_train['rougher.input.feed_au'] <= 0).sum())
display((data_train['rougher.output.concentrate_au'] <= 0).sum())
display((data_train['primary_cleaner.output.concentrate_au'] <= 0).sum())
display((data_train['final.output.concentrate_au'] <= 0).sum())
display((data_train['rougher.input.feed_ag'] == 0).sum())
display((data_train['rougher.output.concentrate_ag'] == 0).sum())
display((data_train['primary_cleaner.output.concentrate_ag'] == 0).sum())
display((data_train['final.output.concentrate_ag'] == 0).sum())
display((data_train['rougher.input.feed_pb'] == 0).sum())
display((data_train['primary_cleaner.output.concentrate_pb'] == 0).sum())
display((data_train['final.output.concentrate_pb'] == 0).sum())
# ### распределения размеров гранул на обучающей и тестовой выборках

# размер гранул хранится в колонках '....feed_size'

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Анализ этапа первичной очистки не требуется по условию проекта.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fffdd0'>понял. поправил.
#     </font>
# </div

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# In[25]:


# размер гранул в тренировочной выборке

data_feed_size_train = data_train.filter(like='feed_size').reset_index(drop=True)
data_feed_size_train['rougher.input.feed_size'].to_frame().boxplot(
    vert = False, figsize = (20, 3));
title = f'размер гранул в тренировочной выборке'
plt.title(title + "\n", fontsize = 20)
plt.xlabel('значение показателя' + "\n", fontsize = 20);
plt.show()


# In[26]:


data_feed_size_train = data_train.filter(like='feed_size')
data_feed_size_train['rougher.input.feed_size'].to_frame().boxplot(
    vert = False, figsize = (20, 3));
title = f'размер гранул в тренировочной выборке'
plt.title(title + "\n", fontsize = 20)
plt.xlabel('значение показателя' + "\n", fontsize = 20);
plt.xlim(-10, 150);

data_feed_size_train['rougher.input.feed_size'].hist(bins=50, figsize=(10, 5));
# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 
# 1. Здесь мы имеем дело с непрерывной величиной - для анализа её распределения стоит использовать график распределения плотности `kde` (например, `sns.kdeplot`) вместо обычной гистограммы, она позволяет нивелировать разницу в размерах выборок при анализе распределений. Обрати также внимание, что при использовании `kdeplot()` по оси Y будет уже не частота значений, а плотность распределения.
# 2. Также один и тот же признак на разных выборках стоит отрисовать на одном графике (подписав при этом легенду, так как две меры) - так разница или отсутствие разницы между выборками будет очевиднее.
# 3. Гистограммы также нужно оформить.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fffdd0'>добавил ниже.
#     </font>
# </div

# In[27]:


# размер гранул в тестовой выборке

data_feed_size_test = data_test.filter(like='feed_size')
data_feed_size_test['rougher.input.feed_size'].to_frame().boxplot(
    vert = False, figsize = (20, 3));
title = f'размер гранул в тестовой выборке'
plt.title(title + "\n", fontsize = 20)
plt.xlabel('значение показателя' + "\n", fontsize = 20);
plt.show()


# In[28]:


data_feed_size_test['rougher.input.feed_size'].to_frame().boxplot(
    vert = False, figsize = (20, 3));
title = f'размер гранул в тестовой выборке'
plt.title(title + "\n", fontsize = 20)
plt.xlabel('значение показателя' + "\n", fontsize = 20);
plt.xlim(-10, 150);


# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 
# Ящики с усами не оформлены. И зачем-то дублируются - зачем две одинаковые секции графиков?

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fffdd0'>они разные - тренировочная и тестовая выборки, разный маштаб, что б удобно было смотреть/видеть.
#     </font>
# </div

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Окей, принято.

# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
# на графиках видно, что изначально признак rougher.input.feed_size в тренировочной и тестовой выборках был распределен нормально со здвигом влево и с большим количеством выбросов справа.
# 
# после первичной обработки признаки получили нормально распределение с незначительным отличием медианного значения.
# </b></font>
# </div>

# In[29]:


feed_size = pd.concat(
    [
    data_feed_size_train['rougher.input.feed_size'],
    data_feed_size_test['rougher.input.feed_size']
],
    sort=False, axis=1)


# In[30]:


feed_size.columns = ['feed_size_train', 'feed_size_test']


# In[31]:


feed_size.columns


# In[32]:


for i in feed_size.columns:
    sns.kdeplot(data=feed_size);
    title = f'плотность показателя {"rougher.input.feed_size"}'
    plt.title(title + "\n", fontsize = 20)
    plt.ylabel('плотность распределения значений' + "\n", fontsize = 10);


# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fffdd0'>приналичии такого графика отдельные гистограммы не нужны. такой вариант более информативен. тут сразу видно что в тренировочной и тестовой выборках значения распределены нормально.
#     </font>
# </div

# In[33]:


print('среднее значение гранул в трейне', feed_size['feed_size_train'].mean())
print('медеанное значение гранул в трейне', feed_size['feed_size_train'].median())
print()
print('среднее значение гранул в тесте', feed_size['feed_size_test'].mean())
print('медеанное значение гранул в тесте', feed_size['feed_size_test'].median())


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Сравнили размеры гранул сырья на обучающей и тестовой выборках для этапа `rougher.input.feed_size` - отлично.
#     
# Чуть более интересным решением было бы использование статистического теста (например, `ttest`) для сравнения распределений в выборках.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# 
# Нужно сделать вывод о схожести распределения между выборками.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
#     
# среднее значение гранул в трейне 58.92271219189511
#     
# медеанное значение гранул в трейне 54.36118656996395
# 
# среднее значение гранул в тесте 59.11339962327545
#     
# медеанное значение гранул в тесте 55.50948105654558
#     
# средние и медианы отличаются минимально, данные распределены нормально с небольшим сдвигом влево. выборки похожи по распределению, в трейне больший разброс по величине значении.
# </font>

# ### "лишние" колонки в data_train

# In[34]:


data_train_columns = data_train.columns
data_test_columns = data_test.columns
display(len(data_train_columns))
display(len(data_test_columns))
print('разница в количестве столбцов:', len(data_train_columns) - len(data_test_columns))


# In[35]:


# тут получим список столбцов не попавших в тестовую выборку

column_difference = []
for i in range(len(data_train_columns)):
    if data_train_columns[i] not in data_test_columns:
        column_difference.append(data_train_columns[i])
        
print(len(column_difference))
display(column_difference)


# **перечень показателей, котрые отсутствуют в тестовой выборке.**
# 
# 
# 1. 'rougher.calculation.sulfate_to_au_concentrate' - расчетное значение - соотношение сульфата к концентрации золота
# 2. 'rougher.calculation.floatbank10_sulfate_to_au_feed' - расчетное значение - floatbank10 соотношение сульфата к концентрации золота
# 3. 'rougher.calculation.floatbank11_sulfate_to_au_feed' - расчетное значение - floatbank11 соотношение сульфата к концентрации золота
# 4. 'rougher.calculation.au_pb_ratio' - расчетное значение - соотношение золота к свенцу
# 5. 'rougher.output.concentrate_au' - выход концентрата золота после флотации
# 6. 'rougher.output.concentrate_ag' - выход концентрата серебра после флотации
# 7. 'rougher.output.concentrate_pb' - выход концентрата свенца после флотации
# 8. 'rougher.output.concentrate_sol' - выход концентрата солей после флотации
# 9. 'rougher.output.recovery' - коэффициент восстановления после флотации
# 10. 'rougher.output.tail_au' - содержание золота в хвостах после флотации
# 11. 'rougher.output.tail_ag' - содержание серебра в хвостах после флотации
# 12. 'rougher.output.tail_pb' - содержание свенца в хвостах после флотации
# 13. 'rougher.output.tail_sol' - содержание солей в хвостах после флотации
# 14. 'primary_cleaner.output.concentrate_au' - содержание золота после первичной очистки
# 15. 'primary_cleaner.output.concentrate_ag' - содержание серебра после первичной очистки
# 16. 'primary_cleaner.output.concentrate_pb' - содержание свенца после первичной очистки
# 17. 'primary_cleaner.output.concentrate_sol' - содержание солей после первичной очистки
# 18. 'primary_cleaner.output.tail_au' - содержание золота в хвостах после первичной очистки
# 19. 'primary_cleaner.output.tail_ag' - содержание серебра в хвостах после первичной очистки
# 20. 'primary_cleaner.output.tail_pb' - содержание свенца в хвостах после первичной очистки
# 21. 'primary_cleaner.output.tail_sol' - содержание солей в хвостах после первичной очистки
# 22. 'secondary_cleaner.output.tail_au' - содержание золота после вторичной очистки
# 23. 'secondary_cleaner.output.tail_ag' - содержание серебра после вторичной очистки
# 24. 'secondary_cleaner.output.tail_pb' - содержание свенца после вторичной очистки
# 25. 'secondary_cleaner.output.tail_sol' - содержание солей после вторичной очистки
# 26. 'final.output.concentrate_au' - содержание золота в конечном концентрате
# 27. 'final.output.concentrate_ag' - содержание серебра в конечном концентрате
# 28. 'final.output.concentrate_pb' - содержание свенца в конечном концентрате
# 29. 'final.output.concentrate_sol' - содержание солей в конечном концентрате
# 30. 'final.output.recovery' - финальный коэффициент восстановления золота
# 31. 'final.output.tail_au' - содержание золота в хвостах
# 32. 'final.output.tail_ag' - содержание серебра в хвостах
# 33. 'final.output.tail_pb' - содержание свенца в хвостах
# 34. 'final.output.tail_sol' - содержание солей в хвостах

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Проанализировали разницу в признаках между выборками.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b> Здесь стоит вспомнить разницу между онлайн и оффлайн метриками: исходя из понимания, что тестовая выборка имитирует работу модели в реальных условиях протекания технологического процесса, давай подумаем, почему в `train` есть признаки, которые недоступны в `test`?
#     
# Нужно сделать вывод о причине расхожедния количества признаков между `train` и `test`.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# расчетные значения понятно не нужны, нужны только факты. в тесте остались только парметры входного сырья и настройки параметров обогащения. собственно то что и нужно для настройки модели - нам надо получить корректные предсказания для сырья.
# </font>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.
# удалим лишние столбцы

# как улучшить этот код??? как передать в drop готовый список???

data_train_ch1 = data_train.drop(['rougher.calculation.sulfate_to_au_concentrate',
                                   'rougher.calculation.floatbank10_sulfate_to_au_feed',
                                   'rougher.calculation.floatbank11_sulfate_to_au_feed',
                                   'rougher.calculation.au_pb_ratio',
                                   'rougher.output.concentrate_au',
                                   'rougher.output.concentrate_ag',
                                   'rougher.output.concentrate_pb',
                                   'rougher.output.concentrate_sol',
                                   'rougher.output.recovery',
                                   'rougher.output.tail_au',
                                   'rougher.output.tail_ag',
                                   'rougher.output.tail_pb',
                                   'rougher.output.tail_sol',
                                   'primary_cleaner.output.concentrate_au',
                                   'primary_cleaner.output.concentrate_ag',
                                   'primary_cleaner.output.concentrate_pb',
                                   'primary_cleaner.output.concentrate_sol',
                                   'primary_cleaner.output.tail_au',
                                   'primary_cleaner.output.tail_ag',
                                   'primary_cleaner.output.tail_pb',
                                   'primary_cleaner.output.tail_sol',
                                   'secondary_cleaner.output.tail_au',
                                   'secondary_cleaner.output.tail_ag',
                                   'secondary_cleaner.output.tail_pb',
                                   'secondary_cleaner.output.tail_sol',
                                   'final.output.concentrate_au',
                                   'final.output.concentrate_ag',
                                   'final.output.concentrate_pb',
                                   'final.output.concentrate_sol',
                                   'final.output.recovery',
                                   'final.output.tail_au',
                                   'final.output.tail_ag',
                                   'final.output.tail_pb',
                                   'final.output.tail_sol'],
                                 axis=1)
# In[36]:


data_train_ch1 = data_train.drop(list(column_difference), axis=1)


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Код можно улучшить, используя, например, свойства множеств - хранение уникальных элементов и возможность вычитания одного из другого:
#     
#     col_list = list(set(train.columns) - set(test.columns))
#     
# Альетрнатива - итерироваться по столбцам из `train` и проверять наличие в `test`:
#     
#     col_list = [train_col for train_col in train.columns if train_col in test.columns]

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# у меня есть `column_difference` уже готовый. как его передать в drop??
# </font>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> В целом ровно так же, как ты сейчас передаёшь список, но сформированный руками:
#     
#     df = df.drop(columns_list, axis=1)
#     

# In[37]:


data_tester(data_train_ch1)


# In[38]:


pass_value_barh(data_train_ch1)


# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
# нет лишних столбцов - нет лишних пропусков
# </b></font>
# </div>

# ### обработка пропусков

# In[39]:


data_train_ch1.isna().sum()


# сумма всех пропусков 1420 
# 
# всего строк 14579 - 1420 это меньше 10%
# 
# удалю строки с пропусками, посмтрю что останется

# In[40]:


data_train_ch1 = data_train_ch1.dropna()


# In[41]:


data_train_ch1.isna().sum()


# In[42]:


data_train_ch1.info()


# In[43]:


14579 - 13371


# таблица стала короче на 1208 строк. это 8.29% данных. ИМХО не критичные потери.

# In[44]:


data_test.isna().sum()


# In[45]:


data_test.info()


# в data_test 375 пропусков в 4860 строках, это примерно 8%
# удалим пропуски

# In[46]:


data_test = data_test.dropna()


# In[47]:


data_test.info()


# In[48]:


4860 - 4537 


# строк стало меньше на 323 это 7,7%

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Окей, пропуски вполне можно удалить:)

# In[ ]:





# ### восстановление целевых признаков

# по условию задачи надо спрогнозировать две величины:
# - эффективность обогащения чернового концентрата `rougher.output.recovery`
# - эффективность обогащения финального концентрата `final.output.recovery`
# 
# в `data_train_ch1` и `data_test` этих данных нет. необходимо подтянуть их из `data_full`
# 
# для этого нам нужна сквознаю индексация во всех трех таблицах.

# In[49]:


data_train_ch1.head(3)


# в каждой таблице есть признак `date` это дата и время записи строки в таблицу. надо проверить насколько эти записи уникальны и в случае "успеха" использовать их в качестве индекса при заполнении целевых признаков.

# In[50]:


data_train_ch1.shape


# In[51]:


len(data_train_ch1.date.unique())


# 12732

# количество уникальных признаков `date` совпадает с размерностью таблицы. гипотеза подтвердилсь (немного не корректно сформулировано, но суть понятна).
# 
# `date` имеет строковый тип данных, надо их конвертировать в дату и время.

# In[52]:


data_train_ch1['date'] = pd.to_datetime(data_train_ch1['date'], format='%Y-%m-%d %H:%M:%S')
data_full['date'] = pd.to_datetime(data_full['date'], format='%Y-%m-%d %H:%M:%S')
data_test['date'] = pd.to_datetime(data_test['date'], format='%Y-%m-%d %H:%M:%S')
display(data_train_ch1.info())
display(data_full.info())
display(data_test.info())


# In[53]:


data_full[['date', 'rougher.output.recovery', 'final.output.recovery']]


# стлбец `date` придется сделать индексом во всех таблицах, а то чет не получается добавть таргеты

# In[54]:


data_train_ch1.set_index('date', inplace=True)
data_full.set_index('date', inplace=True)
data_test.set_index('date', inplace=True)


# In[55]:


data_full[['rougher.output.recovery', 'final.output.recovery']]


# In[56]:


data_train_ch1 = data_train_ch1.join(data_full[['rougher.output.recovery',
                                                'final.output.recovery']])


# In[57]:


display(data_train_ch1.head(4))
display(data_train_ch1.isna().sum())


# добавим таргеты в `data_test`

# In[58]:


data_test = data_test.join(data_full[['rougher.output.recovery', 'final.output.recovery']])


# In[59]:


display(data_test.info())
display(data_test.isna().sum())


# данные готовы к дальнейшим манипуляциям

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> В `test` добавили целевые признаки из `full`, используя дату как ключ при соединении - отлично!

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# 
# Здесь заканчивается стрктурный блок работы - стоит сделать промежуточные выводы о проделанной работе в блоке.

# ## Модель

# ### sMAPE функция

# ![image.png](attachment:image.png)

# smape = (1/n) * Σ(|прогноз – фактический| / ((|фактический| + |прогноз|)/2) * 100
# 
# прогноз - predict
# факт - fact
# 
# smape = (1/n) * Σ(|predict – fact| / ((|fact| + |predict|)/2) * 100
# 

# In[60]:


def smape_calculat(fact, predict):
    smape = 1 / len(fact) * (np.abs(predict - fact) / ((np.abs(predict) + np.abs(fact)) / 2)).sum() * 100
    return smape   


# ### Итоговая sMAPE функция

# ![image.png](attachment:image.png)

# In[5]:


def final_smape_calculat(smape_rougher, smape_final):
    final_smape = 0.25 * smape_rougher + 0.75 * smape_final
    return final_smape


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Есть функции для частного и взвешенного `sMAPE` - супер!
# </div>

# как я понимаю перед нами задача регресии.
# для исследования обучим модели:
# 1. RandomForestRegressor
# 2. LinearRegression
# 
# проверим качество каждой, выберем лучшую для нашей задачи.

# решающее дерево не будем пробовать по причине его низкой "производительности"

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Окей, звучит как план:)

# ### подготовим данные для обучения моделей

# In[62]:


data_train_ch1.head()


# In[63]:


# разобьем датасет на features и target

features_train = data_train_ch1.drop(['rougher.output.recovery', 'final.output.recovery'], axis=1)
target_train_rougher_output_recovery = data_train_ch1['rougher.output.recovery']
target_train_final_output_recovery = data_train_ch1['final.output.recovery']


# In[64]:


features_test = data_test.drop(['rougher.output.recovery', 'final.output.recovery'], axis=1)
target_test_rougher_output_recovery = data_test['rougher.output.recovery']
target_test_final_output_recovery = data_test['final.output.recovery']


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Выделили признаки для обучения и целевые признаки - отлично!
# </div>

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
#     
# <b>Некоторые замечания и рекомендации⚠️:</b> 
# Дополнительно стоит выполнить масштабирование непрерывных переменных - это важно для линейной регрессии, которую ты используешь.

# ### проверим модели на кросс-валидации

# In[65]:


# подготовим метрику
smape_score = make_scorer(smape_calculat, greater_is_better=False)


# In[66]:


get_ipython().run_cell_magic('time', '', '\nprint(abs(cross_val_score(RandomForestRegressor(random_state=216),\n                      features_train, target_train_rougher_output_recovery,\n                      scoring=smape_score, cv=5).mean()))')


# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# результат RandomForestRegressor для rougher_output 6.331170158352381 - огонь!!
# </font>

# In[67]:


get_ipython().run_cell_magic('time', '', '\nprint(abs(cross_val_score(RandomForestRegressor(random_state=216),\n                      features_train, target_train_final_output_recovery,\n                      scoring=smape_score, cv=5).mean()))')


# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# результат RandomForestRegressor для final_output 9.095969344986715 - тоже лучше
# </font>

# In[68]:


get_ipython().run_cell_magic('time', '', '\nlr_r = abs(cross_val_score(LinearRegression(), features_train, target_train_rougher_output_recovery,\n                      scoring=smape_score, cv=5).mean())\nprint(lr_r)')


# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# результат LinearRegression для rougher_output 6.759949614853258
# </font>

# In[69]:


get_ipython().run_cell_magic('time', '', '\nlr_f = abs(cross_val_score(LinearRegression(), features_train, target_train_final_output_recovery,\n                      scoring=smape_score, cv=5).mean())\nprint(lr_f)')


# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# результат LinearRegression для final_output 8.935299356414598
# </font>

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# по данным кросс-валидации LinearRegression выдает более точный результат по сравнению с RandomForestRegressor.
#     что странно.
# </font>

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# результаты кросс-валидвции после удаления выбросов стали сильно лучше - RandomForestRegressor 6.33 победа над LinearRegression.
#     ништяк!!!
# </font>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Случайный лес с ненастроенными гиперпараметрами работает не очень хорошо.

# ### случайный лес (target_train_rougher_output_recovery)

# подберем гиперпараметры для модели rougher.output.recovery

# In[70]:


model_rfr = RandomForestRegressor(random_state=216, n_jobs=-1)


# In[71]:


parametrs = {
    'n_estimators': range(10, 150, 10),
    'max_depth': range(1, 7),
              }


# In[72]:


get_ipython().run_cell_magic('time', '', '\ngrid_r = GridSearchCV(model_rfr, parametrs, scoring=smape_score, cv=3)\ngrid_r.fit(features_train, target_train_rougher_output_recovery)')

CPU times: user 25min 56s, sys: 2.15 s, total: 25min 58s
Wall time: 26min 1s
GridSearchCV(cv=3, estimator=RandomForestRegressor(n_jobs=-1, random_state=216),
             param_grid={'max_depth': range(1, 7),
                         'n_estimators': range(10, 150, 10)},
             scoring=make_scorer(smape_calculat, greater_is_better=False))
# In[73]:


display(grid_r.best_params_)
display(abs(grid_r.best_score_))

df111 = pd.DataFrame.from_dict(grid_r.cv_results_, orient='index').reset_index()
display(df111)


# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# ну вот так отработал GridSearchCV. сказать что это хорошо - нет. полный отстой. думаю мой подход был лучше.
# </font>

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# С выбранной сеткой гиперпараметров - неудивительно:) Обрати, пожалуйста, внимание на то, какой диапазон значений я советовал ниже для `max_depth` и какой ты выбрал по итогу - твоя модель уже на первых итерациях подбора начинает уходить в сильное переобучение и ожидаемо даёт низкий результат.
#     
# В целом можно не рассматривать такое большое количество деревьев: интервал от 10 до 100-150 вполне подойдёт для экономии времени.
#     
# Также не выведена оценка на кросс-валидации.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# и снова мы видим что гиперпараметры подобраны фигово
#     
#     
#     с такими нстройками {'max_depth': 4, 'n_estimators': 100} Итоговое sMAPE: 6.615275488428664 на тестовой выборке, а было 5.414389602377232
# </font>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Гиперпараметры подобраны хорошо: лучше иметь модель, ошибающуюся чуть чаще, чем нестабильную модель, которая на сэмпле данных дала один результат, а на другом даст другой. Глубина дерева в 28 - это самое что ни на есть переобучение, ведущее к ошибкам при работе модели с новыми данными. 

# ### случайный лес (target_train_final_output_recovery)

# подберем гиперпараметры для модели final.output.recovery

# In[74]:


get_ipython().run_cell_magic('time', '', '\ngrid_f = GridSearchCV(model_rfr, parametrs, scoring=smape_score, cv=3)\ngrid_f.fit(features_train, target_train_final_output_recovery)')


# In[75]:


display(grid_f.best_params_)
display(abs(grid_f.best_score_))

df222 = pd.DataFrame.from_dict(grid_f.cv_results_, orient='index').reset_index()
display(df222)


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Для `RandomForestRegressor` оптимизировали гиперпараметры. Время работы 1 день - это, конечно, жуть:) Но ничего, подскажу по оптимизации:)

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Есть пара замечаний по сетке параметров:
# 1. Для гиперапараметра `n_estimators` оценивается очень короткая последовательность: по-настоящему этот алгоритм раскрывается при большом количестве деревьев. При поиске оптимального значения стоит исследовать более широкую последовательность с большим шагом - так шансы найти оптимальное количество деревьев выше, чем исследование короткой последовательности с маленьким шагом.
# 2. Для гиперпараметра `max_depth` рассматривается очень длинная последовательность: деревья с большой глубиной склонны к переобучению, а обучаются и предсказывают результат они дольше, поэтому делать их слишком глубокими не стоит - оптимальное значение почти всегда лежит в диапазоне от 2 до 5-6. Кроме того, можно попробовать значение `None` - в итоге оптимальная последовательность может выглядеть как `[None] + [i for i in range(2, 7)]`.
#     
# Также замечание по промежуточной оценке - для промежуточной оценки используется `test` выборка, это некорректное решение, так как на `test` выборке мы тестируем только одну, финальную модель, выбранную из нескольких в ходе промежуточной оценки.
#     
# Для промежуточной оценки нужно использовать кросс-валидацию. Можно использовать `cross_val_score()` в сочетании с циклом для оптимизации гиперпараметров, можно использовать `GridSearchCV` или `RandomizedSearchCV` для совмещения поиска гиперпараметров и проведения кросс-валидации. 
#     
# Тут важным моментом будет использование `smape` как метрики для оптимизации. За это отвечает настройка параметра `scoring` - именно он отвечает за метрику, которая будет оценивать качество моделей в ходе кросс-валидации (в том числе при оптимизации гиперпараметров). Если не настроить его, оценка моделей на кросс-валидации будет выполнена по дефолтной метрике регрессионных моделей - `R2`.
#     
# Метрика нашего проекта - `sMAPE`, и в базовом наборе метрик `sklearn` она отсутствует - нам придётся сделать свой скорринг. Для этого можно использовать инструмент `make_scorer` (https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html).
#     
# Так как метрика `sMAPE` применяется для задач регрессии, то она тем лучше, чем ниже - это нужно учитывать при создании скорринга для кросс-валидации, так как по умолчанию инструменты кросс-валидации вроде `cross_val_score` и `GridSearchCV/RandomizedSearchCV` умеют только максимизировать метрику качества. Поэтому при создании скорринга с помощью `make_scorer` важно настроить параметр `greater_is_better=False`, чтобы оптимизируемая метрика минимизировалась, а не максимизировалась - таким образом задача максимизации будет решаться через задачу минимизации обратной функции.
#     
# Также при настройке этого параметра получаемая метрика будет отрицательной: это особеность работы `make_scorer` с настроенным параметром `greater_is_better=False`. Поэтому при выводе метрики на экран её стоит сделать положительной: взять по модулю, домножить на `-1` или просто указать `-` при выводе на экран, вроде `print(-a)`.
#     
# По итогу из двух метрик на кросс-валидации нужно посчитать итоговое `sMAPE` для каждой модели и по ней выбирать лучшую модель для оценки на `test`.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Метрики с кросс-валидации отрицательные.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# **Также при настройке этого параметра получаемая метрика будет отрицательной: это особеность работы `make_scorer`**
#     
# я так понимаю это не проблема, надо просто понимать почему так. или прям критично модуль метрики вывести?
# </font>

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Выше ведь написано: `Поэтому при выводе метрики на экран её стоит сделать положительной`:) Поэтому да, критично - важно, чтобы метрика ошибки не была отрицательной при демонстрации решения заказчику, иначе будут вопросы. 
#     
# Сейчас код проекта не исполнен, поэтому нет возможности проверить учёт замечания - контроль на следующем этапе.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# Алексей, мне очень жаль что ты не обратил внимание на то что я вставил модуль во всех выводах отрицательной метрики выше.
# Мой конечно косяк.
#     </font>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Василий, модуль я видел, но замечание с последней итерации не к тому, что вывод отрицательный (про отрицательную метрику - это ответ на твой вопрос, который ты задал), а к тому, что твой код не исполнен и что результат исполнения замечания будет проверен на следующей итерации - выше я неоднократно актентировал внимание на важности перезапуска проекта, чтобы в ячейках вывода были актуальные результаты, у тебя результатов не было. Сейчас с кодом всё в норме, и я вижу, что замечание было исправлено корректно. Спасибо, что внёс правки.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Оценили линейную регрессию - отлично!

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Аналогично нужно выполнить оценку модели на кросс-валидации.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# А зачем тут оценка на `test`?

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# а мне больше не на чем проверить....
# </font>

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# На `test` оценивается только одна модель, лучшая на кросс-валидации. Соответственно все остальные оценки моделей должны быть промежуточными с кросс-валидации. 

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# 3.7 переделал. оценил LinearRegression на кросс-валидации, без использования тестовой выборки. результат не подходящий для дальнейшей работы. 
# </font>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
# из резульптатов предсказаний различных моделей, можно сделать вывод, что RandomForestRegressor справляется лучше чем LinearRegression. данные предсказаний RandomForestRegressor более точные.
# 3.3884954035582964 и 6.089687668650211 против 5.593416047068724 и 7.799537392405231
#         </b></font>
# </div>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Выбрали лучшую модель - отлично!

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Оценивать модели нужно по итоговой метрике, а не по двум частным.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# Итоговая метрика LinearRegression 6.809431980558748
#     
#     забегая в немного в будущее это лучше чем результат dummy (8.35354805182361) но хуже чем RandomForestRegressor (6.615275488428664)
# </font>

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Нужна также итоговая метрика для случайного леса для сравнения.

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Метрики нужно посчитать в коде, а не только в выводе, иначе они быстро потеряют актуальность.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# поскольку я не проверяю LinearRegression на тестовой выборке - предыдущие выводы по ней не актуальны. модель не прошла тесты на кросс-валидыции, показав низкое качество предсказаний.
# </font>

# In[6]:


print('Линейная регрессия:', final_smape_calculat(lr_r, lr_f))


# In[8]:


print('Случайный лес:' final_smape_calculat(abs(grid_r.best_score_), abs(grid_f.best_score_)))


# ### проверка на тестовой выборке

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Гиперпараметры лучшей модели будут другими.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# писал выше что GridSearchCV не смог подобрать гиперпараметры лучше моих
# </font>

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Отметил выше ошибочность текущего подхода к оптимизации гиперпараметров.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# я все еще не доволен работой GridSearchCV в части результата. то что она работает быстро - тут конечно плюсую.
# </font>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Ответил выше.

# In[77]:


get_ipython().run_cell_magic('time', '', '# sMAPE наилучшей модели: 3.3884954035582964 | Количество деревьев: 87 | лучшая глубина: 28\n\nmodel_random_forest = RandomForestRegressor(random_state=216, n_estimators=100, max_depth=4)\nmodel_random_forest.fit(features_train, target_train_rougher_output_recovery)\npredictions = model_random_forest.predict(features_test)\nresult_rougher = smape_calculat(target_test_rougher_output_recovery, predictions)\n\nprint("sMAPE rougher_output_recovery на тестовой выборке:", result_rougher)')


# sMAPE rougher_output_recovery на тестовой выборке: 3.9485239680008326

# In[78]:


get_ipython().run_cell_magic('time', '', "# sMAPE наилучшей модели: 6.089687668650211 | Количество деревьев: 88 | лучшая глубина: 42\n\nmodel_random_forest = RandomForestRegressor(random_state=216, n_estimators=100, max_depth=4)\nmodel_random_forest.fit(features_train, target_train_final_output_recovery)\npredictions = model_random_forest.predict(features_test)\nresult_final = smape_calculat(target_test_final_output_recovery, predictions)\n\nprint('sMAPE final_output_recovery на тестовой выборке:', result_final)")


# sMAPE final_output_recovery на тестовой выборке: 7.504192661904609

#  <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
#     GridSearchCV снова меня подвел.
#     это хуже того что было в первый раз
#     
# n_estimators=70, max_depth=2 - sMAPE final_output_recovery на тестовой выборке: 8.287720402502512
#     
# n_estimators=100, max_depth=4 - sMAPE final_output_recovery на тестовой выборке: 7.504192661904609
# </font>

# ### Считаем итоговое sMAPE

# In[79]:


final_smape_calculat(result_rougher, result_final)


# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Лучшую модель оценили на `test` - отличный результат!

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Очень важно также проверить лучшую модель на адекватность, сравнив качество её предсказаний с качеством модели, которая предсказывала бы константу - вдруг окажется, что не было бы большого смысла заниматься созданием новых признаков, тюнингом и кросс-валидацией моделей, если можно было бы просто предсказывать среднее значение тренировочной выборки? 
#     
# В качестве константной модели можно использовать `DummyRegressor` (https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html) -  эта модель как раз создана для генерирования константных предсказаний.
#     
# Важно, чтобы результат тестирования нашей модели на тествой выборке был лучше, чем результат константной модели - в противном случае наша модель является бесполезной, так как все наши усилия над проектом не принесли результата, а можель, просто предсказывющая среднее на `train`, делает нашу работу лучше.
#         </div>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# ### dummy model

# In[80]:


dummy_regr = DummyRegressor(strategy="mean")
dummy_regr.fit(features_train, target_train_rougher_output_recovery)
predictions_r = dummy_regr.predict(features_test)

dummy_regr.fit(features_train, target_train_final_output_recovery)
predictions_f = dummy_regr.predict(features_test)

final_smape_calculat(smape_calculat(target_test_rougher_output_recovery, predictions_r),
                     smape_calculat(target_test_final_output_recovery, predictions_f))


# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# dummy model хороша, можно пользоваться ей и не париться)))
# 
# при такой не большой разнице в прогнозе (8.65 дамми и 5.41 итог проекта) жалко сил потраченных на работу. утешает только одно - получены новые знания и опыт.
# </font>

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# шучу конечно.
# </font>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Ну, это только частный случай - в этой задаче сильно оторваться от константы не получается. Но разрыв между метриками хороший:)

# ## Вывод

# <div style="background: #f0b720; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
#     <font color='fbff94'><b> 
# Для решения поставленной задачи я пробовал обучить Линейную регрессию и Случайный лес (дерево брать не стал из-за его низкой точности)
# 
# я нашел модель подходящую для предсказаний предсказания коэффициента восстановления залота из золотосодержащей руды. в моем проекте это СлучайныйЛес. 
# 
# результат Итогового sMAPE 5.414389602377232 - модель предсказания результата работает достаточно точно.
# 
# Теперь данную модель можно использовать для прогнозирования коэффициент восстановления залота из золотосодержащей руды!
#         </b></font>
# </div>
# 

# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Молодец, что не забываешь про итоговый вывод - отлично!

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Нужно будет его скорректирвоать по мере исправления замечаний.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# на текущей итерации без изменений.
# </font>

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.2 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# На следующей должны быть.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# в этот раз получилось все значительно быстрее благодаря GridSearchCV, но результат работы лучшей модели RandomForestRegressor (6.615275488428664) стал хуже. первоначальный результат был 5.414389602377232 на тестовой выборке
# </font>

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v.3 <a class="tocSkip"></h2>
# 
#     
# <b>На доработку❌:</b>
# Сейчас в проекте немножечко беспорядок: много закомментированного кода, ячейки кода не исполнены. Приведи, пожалуйста, проект в презентабельный вид на следующей итерации - мы всё-таки делаем решение для заказчика.
#     
# Законмментированный код, не несущий справочной информации, нужно удалить, ячейки с кодом должны быть исполнены.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
# вроде все лишнее почистил. если браузер не упадет за ночь - то все ячейки будут исполнены.
# </font>

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v.4 <a class="tocSkip"> </h2>
# 
# <b>Все отлично!👍:</b> Учтено.

# <div style="background: #385c7e ; padding: 5px; border: 1px solid SteelBlue; border-radius: 1px;">
# <font color='fffdd0'>
#     исправленный вывод:
#     
# Для решения поставленной задачи я пробовал обучить Линейную регрессию и Случайный лес (дерево брать не стал из-за его низкой точности)
# я нашел модель подходящую для предсказаний предсказания коэффициента восстановления залота из золотосодержащей руды. в моем проекте это СлучайныйЛес.
# 
# результат Итогового sMAPE 6.615275488428664 - модель предсказания результата работает достаточно точно.
# 
# Теперь данную модель можно использовать для прогнозирования коэффициент восстановления залота из золотосодержащей руды!
# </font>

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# # Комментарий ревьюера: общий вывод по проекту.
# 
# Василий, проект получился на довольно хорошем уровне - отличная работа над проектом, молодец!
# 
# Мне нравится твой аналитический подход к выполнению проекта, ты соблюдаешь структуру работы, выполняешь её последовательно - это очень хорошо! Шаги проекта выполнены по порядку согласно плану проекта, нет смысловых и структурных ям. Важно, что не забываешь про выводы.
# 
# Работа с моделями также выполнена отлично: исследовано несколько алгоритмов, проведён подбор гиперпараметров, выполнена промежуточная оценка моделей - молодец!
#     
# Над проектом ещё стоит поработать - есть рекомендации по дополнению некоторых твоих шагов проекта. Такие рекомендации я отметил жёлтыми комментариями. Будет здорово, если ты учтёшь их - так проект станет структурно и содержательно более совершенным.
#     
# Также в работе есть критические замечания. К этим замечаниям я оставил пояснительные комментарии красного цвета, в которых перечислил возможные варианты дальнейших действий. Уверен, ты быстро с этим управишься:)
#     
# Если о том, что нужно сделать в рамках комментариев, будут возникать вопросы - оставь их, пожалуйста, в комментариях, и я отвечу на них во время следующего ревью.
#     
# Также буду рад ответить на любые твои вопросы по проекту или на какие-либо другие, если они у тебя имеются - оставь их в комментариях, и я постараюсь ответить:)
#     
# Жду твой проект на повторном ревью. До встречи:)

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# # Комментарий ревьюера: общий вывод по проекту v.2.
# 
# Василий, продолжаем работу над проектом - актуальные замечания отмечены комментариями с меткой `v.2`.
#     
# Жду тебя снова:)

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# # Комментарий ревьюера: общий вывод по проекту v.3.
# 
# Василий, продолжаем работу над проектом - актуальные замечания отмечены комментариями с меткой `v.3`.
#     
# Жду тебя снова:)

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# # Комментарий ревьюера: общий вывод по проекту v.4.
# 
# Василий, все замечания учтены - проект принят!
#     
# Спасибо за хорошую работу над проектом, желаю успехов в дальнейшем обучении:)
