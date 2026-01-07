# Подготовка индекса

Для индекса фактов используется ChromaDB с персистентным локальным хранилищем. Эмбеддинги фактов вычисляются с помощью модели sentence-transformers/all-MiniLM-L6-v2.

## Запуск

Из корневой директории проекта вызвать

```bash
make install
make compute-index
```

## Пример вывода

```bash
Loading weights: 100%|████████████████████████████████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 5723.47it/s, Materializing param=pooler.dense.weight]
BertModel LOAD REPORT from: sentence-transformers/all-MiniLM-L6-v2
Key                     | Status     |  |
------------------------+------------+--+-
embeddings.position_ids | UNEXPECTED |  |

Notes:
- UNEXPECTED	:can be ignored when loading from different task/architecture; not ok if you expect identical arch.
Loading facts: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 30/30 [00:00<00:00, 10833.33it/s]
Computing index elapsed: 0.2168 seconds
Collection size: 30
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