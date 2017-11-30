from el_scheme import Scheme, Diod
from knowledge_accumulator import KnowledgeAccumulator


def main():
    scheme = Scheme(name='Однокаскадный усилитель')
    d = Diod(symbol='R1')
    d1 = Diod(symbol='R2')

    scheme.add_component(d1)
    scheme.add_component(d)
    scheme.save_to_db()

    # KnowledgeAccumulator(scheme).learning()


if __name__ == '__main__':
    main()
