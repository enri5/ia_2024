import sys
sys.path.append("C:/Users/enrig/OneDrive/Escritorio/UIB/TERCERO/IA/ia_2024")
from quiques import agent_amplada, agent_profunditat, joc


def main():
    barca = agent_amplada.BarcaAmplada()
    illes = joc.Joc([barca])
    illes.comencar()


if __name__ == "__main__":
    main()
