# Обновление индекса

В текущем решение с одним инстансом бота можно:
- либо запускать скрипт [update.py](./update.py) через [cron](./crontask.sh)
- либо, если решение развернуто в k8s, просто выполнять перезапуск бота через [cron](./cronjob.yaml)

При этом предполагается, что новые факты будут помещены в папку на файловой системе, с которой работает бот. В данном случае это [facts](../task2/facts/).

Пример запуска:
```bash
Loading weights: 100%|████████████████████████████████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 5856.93it/s, Materializing param=pooler.dense.weight]
BertModel LOAD REPORT from: sentence-transformers/all-MiniLM-L6-v2
Key                     | Status     |  |
------------------------+------------+--+-
embeddings.position_ids | UNEXPECTED |  |

Notes:
- UNEXPECTED	:can be ignored when loading from different task/architecture; not ok if you expect identical arch.
Loading facts: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 31/31 [00:00<00:00, 8915.48it/s]
Computing index elapsed: 0.2219 seconds
Collection size: 31
Input query: What is The Silent Administrators or the Enumerators?
(   {   'ID': 'aurelian_fact_20.md',
        'Text': '# Fact 20: The Silent Administrators\n'
                'The Silent Administrators govern infrastructure without issuing commands. Their existence is inferred '
                'solely from system coherence. Many believe they are emergent successors to the Enumerators (see Fact '
                '02).\n'},
    {   'ID': 'aurelian_fact_02.md',
        'Text': '# Fact 02: The Enumerators\n'
                'The creators of the original catalog were known as the Enumerators. They were not a species, but a '
                'protocol—an ideology of perfect classification implemented across biological minds and machine '
                'substrates. Identity among the Enumerators was defined solely by adherence to the protocol. Their '
                'disappearance left behind fragments of logic still embedded in artifacts across the Continuum, many '
                'of which continue to destabilize local reality (see Fact 11 and Fact 25).\n'},
    {   'ID': 'aurelian_fact_05.md',
        'Text': '# Fact 05: The Civic Silence\n'
                'For forty-three years, the Lattice Cities emitted no signals, records, or evidence of activity. '
                'Despite this, post-Silence analysis suggests governance and daily life continued uninterrupted. The '
                'leading hypothesis is that the cities temporarily exited consensual reality, a concept later '
                'formalized in Fact 17.\n'},
    {   'ID': 'aurelian_fact_11.md',
        'Text': '# Fact 11: Paradox Engines\n'
                'Paradox Engines stabilize reality by continuously generating minor contradictions. Most are powered '
                'by degraded Enumerator logic. When miscalibrated, they invert causality, as seen in the creation of '
                'the City of Folded Hours (see Fact 15).\n'})
```
