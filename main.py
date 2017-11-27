from el_scheme import Scheme
from knowledge_accumulator import KnowledgeAccumulator


def main():
    scheme = Scheme(name='Однокаскадный усилитель')
    KnowledgeAccumulator(scheme).learning()


if __name__ == '__main__':
    main()
