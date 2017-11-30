from el_scheme import Scheme, Diod
from knowledge_accumulator import KnowledgeAccumulator


def main():
    scheme = Scheme(name='Однокаскадный усилитель')
    d = Diod()

    KnowledgeAccumulator(scheme).learning()


if __name__ == '__main__':
    main()
