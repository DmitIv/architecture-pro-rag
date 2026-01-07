# Оценка качества работы бота

RAG бот во время своей работы записывает результаты обращений в файл [logs.csv](../logs.csv). Скрипт [eval.py](eval.py) сравнивает результаты работы с примерами из [golden_questions.txt](../golden_questions.txt). Оценка производится по косинусному сходству двух векторов: первый от ожидаемого результата, второй - от полученного ответа. При превышении порога в 0.7 ответ считается успешным. В данном случае производится e2e оценка работы всей RAG системы с переиспользованием модели эмбеддингов (исходим из предположения, что она обладает достаточным качеством и отдельно ее тестировать не надо).

- [draw](./RAG%20acc.drawio.png)

# Пример запуска
```bash
❯ make evaluate-accuracy
poetry install --no-root --no-interaction --no-ansi
Installing dependencies from lock file

No dependencies to install or update
poetry run task7/eval.py
Loading weights: 100%|████████████████████████████████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 7339.43it/s, Materializing param=pooler.dense.weight]
BertModel LOAD REPORT from: sentence-transformers/all-MiniLM-L6-v2
Key                     | Status     |  |
------------------------+------------+--+-
embeddings.position_ids | UNEXPECTED |  |

Notes:
- UNEXPECTED	:can be ignored when loading from different task/architecture; not ok if you expect identical arch.
what difference between navigator hale and the weight census? navigator hale is a debated individual or identity appearing across time while the weight census is a recurring measurement of reality weights across the continuum  ai message 1 aurelianfact14md aurelianfact18md2 navigator hale is a debated individual or identity appearing across time while the weight census is a recurring measurement of reality weights across the continuum 0.88259435
what do you know about aurelian? the aurelian continuum is a selfsustaining reality born from a failed cataloguing attempt has conditional time contains fauna with narrative awareness and its potential for selfconsistency is an unresolved open question  ai message 1 aurelianfact01md aurelianfact03md aurelianfact30md aurelianfact13md2 the aurelian continuum is a selfsustaining reality that emerged from a failed classification project its time is conditional and nonlinear a central question is whether it can achieve selfconsistency and its native lifeforms exhibit narrative awareness 0.83278656
what do you think about dart vader? i dont know i dont know 1.0
what are the main points of the containment doctrines? the containment doctrines prioritize the stabilization of highweight anchors over broad corrections  ai message 1 aurelianfact24md2 containment doctrines prioritize the stabilization of highweight anchors over making broad corrections 0.8346422
Accuracy: 100.0000%
```