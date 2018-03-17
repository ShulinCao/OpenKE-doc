Datasets
========

:For training, datasets contain three files:

 - ``train2id.txt``: training file, the first line is the number of triples for training. Then the follow lines are all in the format (e1, e2, rel).

 - ``entity2id.txt``: all entities and corresponding ids, one per line. The first line is the number of entities.

 - ``relation2id.txt``: all relations and corresponding ids, one per line. The first line is the number of relations.

:For testing, datasets contain additional two files (totally five files):

 - ``test2id.txt``: testing file, the first line is the number of triples for testing. Then the follow lines are all in the format (e1, e2, rel).

 - ``valid2id.txt``: validating file, the first line is the number of triples for validating. Then the follow lines are all in the format (e1, e2, rel).
